from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas as pd
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

import zomatopy

zomato_key = "9f60f6d560754fcd24e4a93ca3b6f501"


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):

        global restaurants
        response = 'Showing you top rated restaurants:\n'
        config = {"user_key": zomato_key}
        zomato = zomatopy.initialize_app(config)
        budget_min = tracker.get_slot('budget_min')
        budget_max = tracker.get_slot('budget_max')
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        cuisines_dict = {'chinese': 25, 'south indian': 85, 'american': 1, 'north indian': 50, 'italian': 55,
                         'mexican': 73}
        results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 80)
        data = json.loads(results)
        d = data['restaurants']
        print(d)
        restaurants = pd.DataFrame()
        if data['results_found'] == 0:
            response = "Sorry! We are not able to find any restaurant for your preferences. " \
                       "Please search for some other preferences."
        else:
            restaurants = pd.DataFrame([{'restaurant_name': x['restaurant']['name'],
                                         'restaurant_rating': x['restaurant']['user_rating']['aggregate_rating'],
                                         'restaurant_address': x['restaurant']['location']['address'],
                                         'average_cost_for_two': x['restaurant']['average_cost_for_two']}
                                        for x in d])
            restaurants = restaurants[
                restaurants['average_cost_for_two'] >= budget_min & restaurants['average_cost_for_two'] <= budget_max]
            restaurants = restaurants.sort_values(['restaurant_rating'], ascending=False)
            counter = 1
            for index, row in restaurants.head(5).iterrows():
                response = response + str(counter) + '. ' + str(row["restaurant_name"]) + " in " + \
                           row['restaurant_address'] + " has been rated " + \
                           row['restaurant_rating'] + "\n"
        dispatcher.utter_message(response)


class ActionCheckLocation(Action):

    def name(self):
        return 'action_chk_location'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')

        cities = ['Ahmedabad', 'Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Pune',
                  'Agra', 'Ajmer', 'Aligarh', 'Amravati', 'Amritsar', 'Asansol', 'Aurangabad', 'Bareilly',
                  'Belgaum', 'Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bokaro Steel City',
                  'Chandigarh', 'Coimbatore', 'Cuttack', 'Dehradun', 'Dhanbad', 'Durg-Bhilai Nagar', 'Durgapur',
                  'Erode', 'Faridabad', 'Firozabad', 'Ghaziabad', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Gurgaon',
                  'Guwahati', 'Gwalior', 'Hubli-Dharwad', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar', 'Jammu',
                  'Jamnagar', 'Jamshedpur', 'Jhansi', 'Jodhpur', 'Kannur', 'Kanpur', 'Kakinada', 'Kochi', 'Kottayam',
                  'Kolhapur', 'Kollam', 'Kota', 'Kozhikode', 'Kurnool', 'Lucknow', 'Ludhiana', 'Madurai', 'Malappuram',
                  'Mathura', 'Goa', 'Mangalore', 'Meerut', 'Moradabad', 'Mysore', 'Nagpur', 'Nanded', 'Nashik',
                  'Nellore', 'Noida', 'Palakkad', 'Patna', 'Pondicherry', 'Prayagraj', 'Raipur', 'Rajkot',
                  'Rajahmundry', 'Ranchi', 'Rourkela', 'Salem', 'Sangli', 'Siliguri', 'Solapur', 'Srinagar',
                  'Sultanpur', 'Surat', 'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli', 'Tirunelveli', 'Tiruppur',
                  'Ujjain', 'Bijapur', 'Vadodara', 'Varanasi', 'Vasai-Virar City', 'Vijayawada']

        cities_lower = [x.lower() for x in cities]

        if loc.lower() not in cities_lower:
            dispatcher.utter_message("Sorry, we don’t operate in this city. Can you please specify some other location")
            return [SlotSet('location', None)]
        return [SlotSet('location', loc)]


class SendEmail(Action):

    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        email = tracker.get_slot('email_id')
        restaurants_list = ''
        counter = 1
        for index, row in restaurants.head(10).iterrows():
            restaurants_list = restaurants_list + str(counter) + '. ' + str(row["restaurant_name"]) + " in " + \
                               str(row['restaurant_address']) + " has been rated " + \
                               str(row['restaurant_rating']) + "\n"

        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login('assignmentupgrad@gmail.com', 'Upgrad@123')

        msg = MIMEMultipart()
        message = '''
Hi, here is the list of the restaurants you searched for:

''' + restaurants_list + '''

Enjoy fooding :)

This is an auto generated email. Please dont reply to this email.
'''

        msg['From'] = 'assignmentupgrad@gmail.com'
        msg['To'] = email
        msg['Subject'] = "Foodie - Restaurant search"

        msg.attach(MIMEText(message, 'plain'))

        s.send_message(msg)
        del msg


class ActionVerifyCuisine(Action):

    def name(self):
        return 'action_verify_cuisine'

    def run(self, dispatcher, tracker, domain):
        cuisine = tracker.get_slot('cuisine')
        if cuisine.lower() not in ['chinese', 'south indian', 'american', 'north indian', 'italian', 'mexican']:
            dispatcher.utter_message("Sorry, we do not deliver "+cuisine+" food. Please select some other cuisine.")
            return [SlotSet('cuisine', None)]
        return [SlotSet('cuisine', cuisine)]

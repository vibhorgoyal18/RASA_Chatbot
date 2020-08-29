## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_chk_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget_min": "300", "budget_max": "700"}
    - slot{"budget_max": "700"}
    - slot{"budget_min": "300"}
    - action_search_restaurants
    - utter_email_conf
* restaurant_search{"email_id": "assignmentupgrad@gmail.com"}
    - slot{"email_id": "assignmentupgrad@gmail.com"}
    - action_send_email
    - utter_email_sent

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_chk_location
    - slot{"location": null}
* restaurant_search{"location": "Prayagraj"}
    - slot{"location": "Prayagraj"}
    - action_chk_location
    - slot{"location": "Prayagraj"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget_min": "700"}
    - slot{"budget_min": "700"}
    - action_search_restaurants
    - utter_email_conf
* restaurant_search{"email_id": "assignmentupgrad@gmail.com"}
    - slot{"email_id": "assignmentupgrad@gmail.com"}
    - action_send_email
    - utter_email_sent

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"location": "kolkota"}
    - slot{"location": "kolkota"}
    - action_chk_location
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_chk_location
    - slot{"location": "Kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget_max": "300"}
    - slot{"budget_max": "300"}
    - action_search_restaurants
    - utter_email_conf
* affirm
* restaurant_search{"email_id": "assignmentupgrad@gmail.com"}
    - slot{"email_id": "assignmentupgrad@gmail.com"}
    - action_send_email
    - utter_email_sent

## interactive_story_4_final
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_chk_location
    - slot{"location": null}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_chk_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget_min": "0", "budget_max": "300"}
    - slot{"budget_max": "300"}
    - slot{"budget_min": "0"}
    - action_search_restaurants
    - utter_email_conf
* affirm
    - utter_ask_email_id
    - action_send_email
* restaurant_search
    - utter_email_sent

## interactive_story_5
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_chk_location
    - slot{"location": "chandigarh"}
    - utter_ask_budget
* restaurant_search{"budget_max": "300"}
    - slot{"budget_max": "300"}
    - action_search_restaurants
    - utter_email_conf
* deny
    - utter_goodbye

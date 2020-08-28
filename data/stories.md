## Generated Story 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "benagaluru"}
    - slot{"location": "benagaluru"}
    - action_chk_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
	- action_chk_location
    - verify_location
    - slot{"location": "Bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_min": "300", "budget_max": "700"}
    - slot{"budget_max": "700"}
    - slot{"budget_min": "300"}
    - verify_budget
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "chennai"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "assignmentupgrad@gmail.com"}
    - slot{"email_id": "assignmentupgrad@gmail.com"}
    - action_send_email
    - utter_goodbye
	- action_restart

## Generated Story 2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_chk_location
    - verify_location
    - slot{"location": "chandigarh"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_max": "300"}
    - slot{"budget_max": "300"}
    - verify_budget
    - slot{"budget_min": 0}
    - slot{"budget_max": 300}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "chandigarh"}
    - slot{"restaurant_exist": false}
    - utter_goodbye
    - action_restart

## Generated Story -3
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_chk_location
    - verify_location
    - slot{"location": "chandigarh"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_max": "300"}
    - slot{"budget_max": "300"}
    - verify_budget
    - slot{"budget_min": 0}
    - slot{"budget_max": 300}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "chandigarh"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "assignmentupgrad@gmail.com"}
    - slot{"email_id": "assignmentupgrad@gmail.com"}
    - action_send_email
    - utter_goodbye
	- action_restart

## Generated Story -4
* greet{"location": "hola"}
    - slot{"location": "hola"}
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_chk_location
    - verify_location
    - slot{"location": "chandigarh"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_min": "300", "budget_max": "700"}
    - slot{"budget_max": "700"}
    - slot{"budget_min": "300"}
    - verify_budget
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "chandigarh"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* deny
    - utter_goodbye
	- action_restart

## Generated Story 5
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_chk_location
    - verify_location
    - slot{"location": "chandigarh"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_min": "700"}
    - slot{"budget_min": "700"}
    - verify_budget
    - slot{"budget_min": 700}
    - slot{"budget_max": 10000}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "chandigarh"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* deny
    - utter_goodbye
	- action_restart

## Generated Story 6
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - action_chk_location
    - verify_location
    - slot{"location": "allahabad"}
    - slot{"location_ok": true}
    - verify_location
    - slot{"location": "allahabad"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - verify_cuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_max": "1000"}
    - slot{"budget_max": "1000"}
    - verify_budget
    - slot{"budget_min": 0}
    - slot{"budget_max": 1000}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "allahabad"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "assignmentupgrad@gmail.com"}
    - slot{"email_id": "assignmentupgrad@gmail.com"}
    - action_send_email
    - utter_goodbye
	- action_restart

## Generated Story 7
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - action_chk_location
    - verify_location
    - slot{"location": "allahabad"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_min": "700"}
    - slot{"budget_min": "700"}
    - verify_budget
    - slot{"budget_min": 700}
    - slot{"budget_max": 10000}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "allahabad"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "assignmentupgrad@gmail.com"}
    - slot{"email_id": "assignmentupgrad@gmail.com"}
    - action_send_email
    - utter_goodbye
	- action_restart

## Generated Story -8
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - action_chk_location
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_min": "300", "budget_max": "700"}
    - slot{"budget_max": "700"}
    - slot{"budget_min": "300"}
    - verify_budget
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "mumbai"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* deny
    - utter_goodbye
	- action_restart

## Generated Story 9
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_ok": true}
    - utter_ask_location
* restaurant_search{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - action_chk_location
    - verify_location
    - slot{"location": "coimbatore"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_min": "700"}
    - slot{"budget_min": "700"}
    - verify_budget
    - slot{"budget_min": 700}
    - slot{"budget_max": 10000}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "coimbatore"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "assignmentupgrad@gmail.com"}
    - slot{"email_id": "assignmentupgrad@gmail.com"}
    - action_send_email
    - utter_goodbye
	- action_restart

## Generated Story -10
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kochi"}
    - slot{"location": "Kochi"}
    - action_chk_location
    - verify_location
    - slot{"location": "Kochi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_max": "700"}
    - slot{"budget_max": "700"}
    - verify_budget
    - slot{"budget_min": 0}
    - slot{"budget_max": 700}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "Kochi"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "assignmentupgrad@gmail.com"}
    - slot{"email_id": "assignmentupgrad@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye
	- action_restart

## Generated Story -11
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "majuli"}
    - slot{"location": "majuli"}
    - action_chk_location
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "madrid"}
    - slot{"location": "madrid"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "vijayawada"}
    - slot{"location": "vijayawada"}
    - verify_location
    - slot{"location": "vijayawada"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - verify_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_min": "700"}
    - slot{"budget_min": "700"}
    - verify_budget
    - slot{"budget_min": 700}
    - slot{"budget_max": 10000}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "vijayawada"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* deny
    - utter_goodbye
	- action_restart

## Generated Story -12
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "chennai", "budget_min": "300", "budget_max": "700"}
    - slot{"budget_max": "700"}
    - slot{"budget_min": "300"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "chennai"}
    - action_chk_location
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_ok": true}
    - verify_budget
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - slot{"budget_ok": true}
    - verify_budget
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "chennai"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "assignmentupgrad@gmail.com"}
    - slot{"email_id": "assignmentupgrad@gmail.com"}
    - action_send_email
    - utter_goodbye
	- action_restart
	
## Generated Story 13
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "lanka"}
    - slot{"location": "lanka"}
    - action_chk_location
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "oman"}
    - slot{"location": "oman"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "dubai"}
    - slot{"location": "dubai"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "lucknow"}
    - slot{"location": "lucknow"}
    - verify_location
    - slot{"location": "lucknow"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_min": "300", "budget_max": "700"}
    - slot{"budget_max": "700"}
    - slot{"budget_min": "300"}
    - verify_budget
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "lucknow"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* deny
    - utter_goodbye
	- action_restart
	
## Generated Story 14
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "budget_min": "300", "budget_max": "700"}
    - slot{"budget_max": "700"}
    - slot{"budget_min": "300"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_chk_location
    - verify_location
    - slot{"location": "jaipur"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_ok": true}
    - verify_budget
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "jaipur"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "assignmentupgrad@gmail.com"}
    - slot{"email_id": "assignmentupgrad@gmail.com"}
    - action_send_email
	- action_restart
	
## Generated Story -15
* greet
    - utter_greet
* restaurant_search{"location": "raipur", "budget_max": "300"}
    - slot{"budget_max": "300"}
    - slot{"location": "raipur"}
    - action_chk_location
    - verify_location
    - slot{"location": "raipur"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - verify_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"cuisine_ok": true}
    - verify_budget
    - slot{"budget_min": 0}
    - slot{"budget_max": 300}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "raipur"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "assignmentupgrad@gmail.com"}
    - slot{"email_id": "assignmentupgrad@gmail.com"}
    - action_send_email
    - utter_goodbye
	- action_restart

## Generated Story -16
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chk_location
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "arabian"}
    - slot{"cuisine": "arabian"}
    - verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_max": "300"}
    - slot{"budget_max": "300"}
    - verify_budget
    - slot{"budget_min": 0}
    - slot{"budget_max": 300}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "delhi"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "assignmentupgrad@gmail.com"}
    - slot{"email_id": "assignmentupgrad@gmail.com"}
    - action_send_email
    - utter_goodbye
	- action_restart

## Generated Story -17
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_chk_location
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "arabian"}
    - slot{"cuisine": "arabian"}
    - verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_max": "300"}
    - slot{"budget_max": "300"}
    - verify_budget
    - slot{"budget_min": 0}
    - slot{"budget_max": 300}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "mumbai"}
    - slot{"restaurant_exist": false}
    - utter_ask_email
* dont_send_email
    - utter_goodbye
	- action_restart

## Generated Story 18
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_chk_location
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "arabian"}
    - slot{"cuisine": "arabian"}
    - verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "arabian"}
    - slot{"cuisine": "arabian"}
    - verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "arabian"}
    - slot{"cuisine": "arabian"}
    - verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_min": "300", "budget_max": "700"}
    - slot{"budget_max": "700"}
    - slot{"budget_min": "300"}
    - verify_budget
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "mumbai"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "assignmentupgrad@gmail.com"}
    - slot{"email_id": "assignmentupgrad@gmail.com"}
    - action_send_email
	- action_restart

## Generated Story 19
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chk_location
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_max": "500"}
    - slot{"budget_max": "500"}
    - verify_budget
    - slot{"budget_min": 0}
    - slot{"budget_max": 10000}
    - slot{"budget_ok": false}
    - utter_ask_budget
* restaurant_search{"budget_max": "300"}
    - slot{"budget_max": "300"}
    - verify_budget
    - slot{"budget_min": 0}
    - slot{"budget_max": 300}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "delhi"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "assignmentupgrad@gmail.com"}
    - slot{"email_id": "assignmentupgrad@gmail.com"}
    - action_send_email
	- action_restart

## Generated Story -20
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "delhi", "budget_min": "300", "budget_max": "800"}
    - slot{"budget_max": "800"}
    - slot{"budget_min": "300"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "delhi"}
    - action_chk_location
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_ok": true}
    - verify_budget
    - slot{"budget_min": 300}
    - slot{"budget_max": 800}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "delhi"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "assignmentupgrad@gmail.com"}
    - slot{"email_id": "assignmentupgrad@gmail.com"}
    - action_send_email
	- action_restart

## Generated Story -21
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ajmer"}
    - slot{"location": "ajmer"}
    - action_chk_location
    - verify_location
    - slot{"location": "ajmer"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_max": "300"}
    - slot{"budget_max": "300"}
    - verify_budget
    - slot{"budget_min": 0}
    - slot{"budget_max": 300}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "ajmer"}
    - slot{"restaurant_exist": false}
    - utter_goodbye
	- action_restart

## Generated Story -22
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "ajmer", "budget_max": "300"}
    - slot{"budget_max": "300"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "ajmer"}
    - action_chk_location
    - verify_location
    - slot{"location": "ajmer"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_ok": true}
    - verify_budget
    - slot{"budget_min": 0}
    - slot{"budget_max": 300}
    - slot{"budget_ok": true}
    - verify_budget
    - slot{"budget_min": 0}
    - slot{"budget_max": 300}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "ajmer"}
    - slot{"restaurant_exist": false}
    - utter_goodbye
	- action_restart
    
## Generated Story 23
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - action_chk_location
    - verify_location
    - slot{"location": "chandigarh"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_min": "700"}
    - slot{"budget_min": "700"}
    - verify_budget
    - slot{"budget_min": 700}
    - slot{"budget_max": 10000}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "chandigarh"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "assignmentupgrad@gmail.com"}
    - slot{"email_id": "assignmentupgrad@gmail.com"}
    - action_send_email
    - utter_goodbye
	- action_restart

## Generated Story 24
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_chk_location
    - verify_location
    - slot{"location": "chandigarh"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_min": "300", "budget_max": "700"}
    - slot{"budget_max": "700"}
    - slot{"budget_min": "300"}
    - verify_budget
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "chandigarh"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "assignmentupgrad@gmail.com"}
    - slot{"email_id": "assignmentupgrad@gmail.com"}
    - action_send_email
    - utter_goodbye
	- action_restart

## Generated Story 25
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_chk_location
    - verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_ok": true}
    - utter_ask_location
* restaurant_search{"location": "pathankot"}
    - slot{"location": "pathankot"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "itanagar"}
    - slot{"location": "itanagar"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "ranchi"}
    - slot{"location": "ranchi"}
    - verify_location
    - slot{"location": "ranchi"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_min": "300", "budget_max": "700"}
    - slot{"budget_max": "700"}
    - slot{"budget_min": "300"}
    - verify_budget
    - slot{"budget_min": 300}
    - slot{"budget_max": 700}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "ranchi"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail{"email_id": "assignmentupgrad@gmail.com"}
    - slot{"email_id": "assignmentupgrad@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye
	- action_restart

## Generated Story -26
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_ok": true}
    - utter_ask_location
* restaurant_search{"location": "dehradun"}
    - slot{"location": "dehradun"}
    - action_chk_location
    - verify_location
    - slot{"location": "dehradun"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_max": "300"}
    - slot{"budget_max": "300"}
    - verify_budget
    - slot{"budget_min": 0}
    - slot{"budget_max": 300}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "dehradun"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* send_mail{"email_id": "assignmentupgrad@gmail.com"}
    - slot{"email_id": "assignmentupgrad@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye
	- action_restart

## Generated Story -27
* greet
    - utter_greet
* restaurant_search{"cuisine": "mughlai", "location": "asansol"}
    - slot{"cuisine": "mughlai"}
    - slot{"location": "asansol"}
    - action_chk_location
    - verify_location
    - slot{"location": "asansol"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "moroccan"}
    - slot{"cuisine": "moroccan"}
    - verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - verify_cuisine
    - slot{"cuisine": null}
    - slot{"cuisine_ok": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - verify_cuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_max": "500"}
    - slot{"budget_max": "500"}
    - verify_budget
    - slot{"budget_min": 0}
    - slot{"budget_max": 10000}
    - slot{"budget_ok": false}
    - utter_ask_budget
* restaurant_search{"budget_max": "300"}
    - slot{"budget_max": "300"}
    - verify_budget
    - slot{"budget_min": 0}
    - slot{"budget_max": 300}
    - slot{"budget_ok": true}    
    - action_restaurant
    - slot{"location": "asansol"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* deny
    - utter_goodbye
	- action_restart

## Generated Story 28
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bhubhaneshwar"}
    - slot{"location": "bhubhaneshwar"}
    - action_chk_location
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "amravati"}
    - slot{"location": "amravati"}
    - action_chk_location
    - verify_location
    - slot{"location": "amravati"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - verify_cuisine
    - slot{"cuisine": "american"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_min": "700"}
    - slot{"budget_min": "700"}
    - verify_budget
    - slot{"budget_min": 700}
    - slot{"budget_max": 10000}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "amravati"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "assignmentupgrad@gmail.com"}
    - slot{"email_id": "assignmentupgrad@gmail.com"}
    - action_send_email
* thankyou
    - utter_goodbye
	- action_restart
	
## Generated Story 29
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_chk_location
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - verify_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_min": "700"}
    - slot{"budget_min": "700"}
    - verify_budget
    - slot{"budget_min": 700}
    - slot{"budget_max": 10000}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "chennai"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart

## Generated Story -30
* 
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - verify_cuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_ok": true}
    - utter_ask_location
* 
* restaurant_search{"location": "warangal"}
    - slot{"location": "warangal"}
    - action_chk_location
    - verify_location
    - slot{"location": "warangal"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_min": "700"}
    - slot{"budget_min": "700"}
    - verify_budget
    - slot{"budget_min": 700}
    - slot{"budget_max": 10000}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "warangal"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* deny
    - utter_goodbye
	- action_restart

## Generated Story 31
* greet
    - utter_greet
* restaurant_search{"location": "colombo"}
    - slot{"location": "colombo"}
    - action_chk_location
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "vegas"}
    - slot{"location": "vegas"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - verify_location
    - slot{"location": "Bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_max": "300"}
    - slot{"budget_max": "300"}
    - verify_budget
    - slot{"budget_min": 0}
    - slot{"budget_max": 300}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "Bangalore"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* deny
    - utter_goodbye
	- action_restart

## Generated Story -32
* greet
    - utter_greet
* restaurant_search{"location": "Hubli-Dharwad"}
    - slot{"location": "Hubli-Dharwad"}
    - action_chk_location
    - verify_location
    - slot{"location": "Hubli-Dharwad"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_max": "300"}
    - slot{"budget_max": "300"}
    - verify_budget
    - slot{"budget_min": 0}
    - slot{"budget_max": 300}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "Hubli-Dharwad"}
    - slot{"restaurant_exist": false}
* 
	- action_restart

## Generated Story -33
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "Hubli-Dharwad"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Hubli-Dharwad"}
    - action_chk_location
    - verify_location
    - slot{"location": "Hubli-Dharwad"}
    - slot{"location_ok": true}
    - verify_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_min": "700"}
    - slot{"budget_min": "700"}
    - verify_budget
    - slot{"budget_min": 700}
    - slot{"budget_max": 10000}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "Hubli-Dharwad"}
    - slot{"restaurant_exist": false}
* goodbye
	- action_restart

## Generated Story -34
* greet
    - utter_greet
* restaurant_search{"location": "guwahati"}
    - slot{"location": "guwahati"}
    - action_chk_location
    - verify_location
    - slot{"location": "guwahati"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - verify_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budget_min": "700"}
    - slot{"budget_min": "700"}
    - verify_budget
    - slot{"budget_min": 700}
    - slot{"budget_max": 10000}
    - slot{"budget_ok": true}
    - action_restaurant
    - slot{"location": "guwahati"}
    - slot{"restaurant_exist": true}
    - utter_ask_email
* affirm
    - utter_ask_email_id
* send_mail{"email_id": "assignmentupgrad@gmail.com"}
    - slot{"email_id": "assignmentupgrad@gmail.com"}
    - action_send_email
    - utter_goodbye
* goodbye
	- action_restart
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* affirm{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_chk_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - verify_cuisine
    - utter_ask_budget
* restaurant_search{"budget_min": "300", "budget_max": "700"}
    - slot{"budget_max": "700"}
    - slot{"budget_min": "300"}
    - verify_budget
    - action_restaurant
    - utter_ask_email
* send_mail
    - action_send_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_2
* restaurant_search{"location": "New Delhi", "budget_min": "565", "budget_max": "678"}
    - slot{"budget_max": "678"}
    - slot{"budget_min": "565"}
    - slot{"location": "New Delhi"}

## interactive_story_3
* greet
    - utter_greet

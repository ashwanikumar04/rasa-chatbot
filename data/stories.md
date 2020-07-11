## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* affirm
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_goodbye

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - export


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* stop

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "mumbai"}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
    
    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - utter_ask_for_result_email
* affirm
    - utter_ask_email
* send_email{"emailid": "ashwanikumar04@gmail.com"}
    - slot{"emailid": "ashwanikumar04@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story: Search using a cuisine in an invalid city 
* greet
    - utter_greet
* restaurant_search{"price": "expensive"}
    - utter_ask_location
* restaurant_search{"location": "gaya"}
    - slot{"location": "gaya"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": null}
    - utter_goodbye

## interactive_story: Search in a valid city 
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_city
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - utter_ask_price
* goodbye{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_for_result_email
* affirm
    - utter_ask_email
* send_email{"emailid": "deepak4ev@gmail.com"}
    - slot{"emailid": "deepak4ev@gmail.com"}
    - action_send_email
    - slot{"emailid": "deepak4ev@gmail.com"}
    - slot{"email_body": null}
    - utter_goodbye

## interactive_story: Valid city and cuisine together
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"location": "delhi"}
    - slot{"is_valid_location": true}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"is_valid_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "expensive"}
    - slot{"price": "expensive"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_for_result_email
* send_email{"emailid": "deepak4ev@gmail.com"}
    - slot{"emailid": "deepak4ev@gmail.com"}
    - action_send_email
    - slot{"emailid": "deepak4ev@gmail.com"}
    - slot{"email_body": null}
    - utter_goodbye
    - action_restart

## interactive_story: Valid city, cuisine and price range all together
* greet
    - utter_greet
* restaurant_search{"price": "expensive", "cuisine": "american", "location": "pune"}
    - slot{"cuisine": "american"}
    - slot{"location": "pune"}
    - slot{"price": "expensive"}
    - action_validate_city
    - slot{"location": "pune"}
    - slot{"is_valid_location": true}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - slot{"is_valid_cuisine": true}
    - action_search_restaurants
    - slot{"location": "pune"}
    - utter_ask_for_result_email
* send_email{"emailid": "deepak4ev@gmail.com"}
    - slot{"emailid": "deepak4ev@gmail.com"}
    - action_send_email
    - slot{"emailid": "deepak4ev@gmail.com"}
    - slot{"email_body": null}
    - utter_goodbye
    - action_restart

## interactive_story: Search by Valid city in a price range
* greet
    - utter_greet
* restaurant_search{"price": "economic", "location": "chennai"}
    - slot{"location": "chennai"}
    - slot{"price": "economic"}
    - action_validate_city
    - slot{"location": "chennai"}
    - slot{"is_valid_location": true}
    - action_validate_cuisine
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"is_valid_cuisine": true}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_ask_for_result_email
* send_email{"emailid": "deepak4ev@gmail.com"}
    - slot{"emailid": "deepak4ev@gmail.com"}
    - action_send_email
    - slot{"emailid": "deepak4ev@gmail.com"}
    - slot{"email_body": null}
    - utter_goodbye
    - action_restart

## interactive_story: Invalid cuisine in valid city together
* restaurant_search{"cuisine": "french", "location": "mumbai"}
    - slot{"cuisine": "french"}
    - slot{"location": "mumbai"}
    - action_validate_city
    - slot{"location": "mumbai"}
    - slot{"is_valid_location": true}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - slot{"is_valid_cuisine": false}
    - utter_goodbye

## interactive_story: Valid city and price range specified in the query
* greet
    - utter_greet
* restaurant_search{"price": "expensive", "location": "Chennai"}
    - slot{"location": "Chennai"}
    - slot{"price": "expensive"}
    - action_validate_city
    - slot{"location": "chennai"}
    - slot{"is_valid_location": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - slot{"is_valid_cuisine": false}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_ask_for_result_email
* send_email{"emailid": "deepak4ev@gmail.com"}
    - slot{"emailid": "deepak4ev@gmail.com"}
    - action_send_email
    - slot{"emailid": "deepak4ev@gmail.com"}
    - slot{"email_body": null}
    - utter_goodbye
    - action_restart

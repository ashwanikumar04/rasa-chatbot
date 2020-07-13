#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## Basic TestCase
* greet: Hi
  - utter_greet
* restaurant_search: I want to find a restaurant
  - utter_ask_location
* restaurant_search: delhi
  - slot{"location": "delhi"}
  - action_validate_location
  - slot{"isServicedCity":true}
  - utter_ask_cuisine
* restaurant_search : chinese
  - slot{"cuisine": "chinese"}
  - utter_ask_pricerange
* restaurant_search : 900
  - slot{"pricerange": "900"}
  - action_search_restaurants
  - utter_ask_ifemailneeded
* affirm : yes
  - utter_ask_emailid
* send_email : "abc@xyz.com"
  - slot{"email": "abc@xyz.com"}
  - action_send_email
  - utter_goodbye


* greet: Hi
    - utter_greet
* restaurant_search: I want something to eat 
    - utter_ask_location
* notify: bengaluru
    - slot{"location": "bangalore"}
    - action_validate_city
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* notify: something in chineese
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* notify: <300
    - slot{"price": "economic"}
    - action_validate_price
    - slot{"price": "economic"}
    - action_validate_request_data
    - slot{"is_valid_search_request": true}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_data_found": true}
    - slot{"is_valid_search_request": null}
    - slot{"email_body": "Smogrill in Opposite Kayla Spa N Saloon, Jaladarshini Layout, New BEL Road, Bangalore has been rated 4.5 with price for two as 150.\n\n2 Mum's Kitchen in Marathahalli, Bangalore has been rated 4.4 with price for two as 200.\n\nAsha Tiffins in 1170, 5th Main Road, Sector 7, HSR, Bangalore has been rated 4.3 with price for two as 200."}
    - utter_ask_for_result_email
* send_email{"emailid": "ashwanikumar04@gmail.com"}
    - slot{"emailid": "ashwanikumar04@gmail.com"}
    - action_validate_email
    - slot{"emailid": "ashwanikumar04@gmail.com"}
    - slot{"is_valid_email": true}
    - action_send_email
    - slot{"emailid": null}
    - slot{"email_body": null}
    - slot{"is_data_found": null}
    - slot{"is_valid_email": null}
    - utter_goodbye
    - action_restart
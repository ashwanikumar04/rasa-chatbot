#### Some tests to test the bot
#### More info for testing at https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

* greet: Hi
  - utter_greet
* restaurant_search: I want something to eat 
  - utter_ask_location
* notify: anywhere in [bengaluru]{"entity": "location", "value": "bangalore"}
  - slot{"location": "bangalore"}
  - action_validate_city
  - slot{"location": "bangalore"}
  - utter_ask_cuisine
* restaurant_search: something in [chineese]{"entity": "cuisine", "value": "chinese"}
  - slot{"cuisine": "chinese"}
  - action_validate_cuisine
  - slot{"cuisine": "chinese"}
  - utter_ask_price
* notify: [<300]{"entity": "price", "value": "economic"}
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
* send_email: please send to my emailid [ashwanikumar04@gmail.com](emailid)
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
  
## price and cuisine together followed by location and send email

* greet: Hi
  - utter_greet
* restaurant_search: Please suggest some [Italian](cuisine) restaurants with price [>700]{"entity": "price", "value": "expensive"}
  - slot{"cuisine": "italian"}
  - slot{"price": "expensive"}
  - action_validate_cuisine
  - slot{"cuisine": "italian"}
  - action_validate_price
  - slot{"price": "expensive"}
  - utter_ask_location
* notify: anywhere in [pune](location)
  - slot{"location": "pune"}
  - action_validate_city
  - slot{"location": "pune"}
  - action_validate_request_data
  - slot{"is_valid_search_request": true}
  - action_search_restaurants
  - slot{"location": null}
  - slot{"cuisine": null}
  - slot{"price": null}
  - slot{"is_data_found": true}
  - slot{"is_valid_search_request": null}
  - slot{"email_body": "Level 5 Bistro and Bar in Survey 1365, 5th Floor, House of Nosh, Above Kalinga Veg Gourmet Kitchen, Opposite Mehendale Garage, Gulawani Maharaj Path, Erandwane, Pune has been rated 4.8 with price for two as 1200.\n\nLe Plaisir in Survey 759/125, Rajkamal, Opposite Kelkar Eye Hospital, Prabhat Road, Deccan Gymkhana, Pune has been rated 4.7 with price for two as 1000.\n\nGong in Shop 22/23, Balewadi High Street, Cummins India Office Campus, Baner- Balewadi Link Road, Baner, Pune has been rated 4.7 with price for two as 1700.\n\nCafe Paashh in Plot E1 & E2, Survey 211/2, Near Orange IVY School, Hiremath Park, Kalyani Nagar, Pune has been rated 4.7 with price for two as 1500.\n\nToit in Final Plot 88, Metro Compound, Besides Bishop Co-Ed School, Kalyani Nagar, Pune has been rated 4.7 with price for two as 1500.\n\nBarbeque Nation in Solitaire Building, Opposite Shree Hospital, Kalyani Nagar, Pune has been rated 4.7 with price for two as 1700.\n\nThe Urban Foundry in Shop 1, Balewadi High Street, Cummins India Office Campus, Baner-Balewadi Link Road, Baner, Pune has been rated 4.6 with price for two as 1600.\n\nEffingut in Shop 4, Deron Heights, Near Ranka Jewellers, Baner, Pune has been rated 4.6 with price for two as 2000.\n\nIndependence Brewing Company in 79/1, Zero One Complex, Pingale Vasti, Mundhwa, Pune has been rated 4.6 with price for two as 2300.\n\nFlechazo in 165, 3rd Floor, Vantagio, Near Silver Sports Club, Wakad, Pune has been rated 4.6 with price for two as 1400."}
  - utter_ask_for_result_email
* affirm: yes
  - utter_ask_email
* send_email: my emailId is [deepak.4ev@gmail.com](emailid)
  - slot{"emailid": "deepak.4ev@gmail.com"}
  - action_validate_email
  - slot{"emailid": "deepak.4ev@gmail.com"}
  - slot{"is_valid_email": true}
  - action_send_email
  - slot{"emailid": null}
  - slot{"email_body": null}
  - slot{"is_data_found": null}
  - slot{"is_valid_email": null}
  - utter_goodbye
  - action_restart
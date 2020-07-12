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
  
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "expensive", "cuisine": "chineese"}
    - slot{"cuisine": "chineese"}
    - slot{"price": "expensive"}
    - utter_ask_location
* notify{"location": "gaya"}
    - slot{"location": "gaya"}
    - action_validate_city
    - slot{"location": null}
    - slot{"is_valid_location": false}
    - utter_goodbye

## interactive_story: Search restaurant and send email. Location, Cuisine and price uttered one by one
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* notify{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_city
    - slot{"location": "bangalore"}
    - slot{"is_valid_location": true}
    - utter_ask_cuisine
* notify{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - slot{"is_valid_cuisine": true}
    - utter_ask_price
* notify{"price": "expensive"}
    - slot{"price": "expensive"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"cuisine": "italian"}
    - slot{"price": "expensive"}
    - slot{"email_body": "Chianti in 960, 12th Main, HAL 2nd Stage, Indiranagar, Bangalore has been rated 4.9 with price for two as 2000.\nTruffles in 28, 4th B Cross, Koramangala 5th Block, Bangalore has been rated 4.8 with price for two as 900.\nBiergarten in 4th B Cross, Koramangala 5th Block, Bangalore has been rated 4.8 with price for two as 2600.\nAB's - Absolute Barbecues in 100 Feet Road, 1st Phase, Near Jayadeva Flyover, 2nd Stage, BTM, Bangalore has been rated 4.8 with price for two as 1250.\nCaperberry in 203, 2nd Floor, UB City, 24 Vittal Mallya Road, Lavelle Road, Bangalore has been rated 4.8 with price for two as 2200.\nAB's - Absolute Barbecues in 90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore has been rated 4.7 with price for two as 1250.\nHard Rock Cafe in 4 & 16, St. Marks Road, Bangalore has been rated 4.7 with price for two as 2500.\nCommuniti in 67 & 68, Brigade Solitaire, Opposite Advaith Hyundai, Residency Road, Bangalore has been rated 4.7 with price for two as 1500.\nHere & Now in 28, MCH Society, Sector 4, HSR, Bangalore has been rated 4.7 with price for two as 900.\nSanté Spa Cuisine in 151, 2nd Cross, 2nd Stage, Domlur, Bangalore has been rated 4.7 with price for two as 1800."}
    - utter_ask_for_result_email
* affirm
    - utter_ask_email
* send_email{"emailid": "deepak4ev@gmail.com"}
    - slot{"emailid": "deepak4ev@gmail.com"}
    - action_send_email
    - slot{"emailid": "deepak4ev@gmail.com"}
    - slot{"email_body": null}
    - utter_goodbye

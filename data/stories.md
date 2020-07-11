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

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Tracker
from rasa_sdk import Action
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet
import zomatopy
import json
import email
from email.message import EmailMessage
import smtplib
import ssl
import os
port = 465  # For SSL
password = "rasa@2020"

cities = set()
fh = open('data/cities.txt')
for line in fh:
    cities.add(line.strip().lower())
fh.close()

cuisines_dict = {'maxican': 73, 'chinese': 25, 'american': 1,
                 'italian': 55,  'north indian': 50, 'south indian': 85}

price_dict = {'economic': (0, 299), 'moderate': (
    300, 700), 'expensive': (701, 9999)}

config = {"user_key": "50aadfe48ced3c06244a29a7381ac7eb"}
zomato = zomatopy.initialize_app(config)

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price = tracker.get_slot('price')
        restaurant_list = []
        try:
            restaurant_list = zomato.getTopRestaurants(
                loc, str(cuisines_dict.get(cuisine)), price_dict[price])
        except:
            dispatcher.utter_message("Sorry, we were not able to find the restaurants. Please try again")
            return [SlotSet('location', None), SlotSet('cuisine', None), SlotSet('price', None)]

        if len(restaurant_list) == 0:
            response = "Sorry, we were not able to find any restaurant with this criteria."
            dispatcher.utter_message("-----"+response)
            return [SlotSet('location', None), SlotSet('cuisine', None), SlotSet('price', None)]
        else:
            user_response_list = []
            for restaurant in restaurant_list[:5]:
                restaurant_details = '{0} in {1} has been rated {2}.'.format(
                    restaurant['name'], restaurant['address'], restaurant['rating'])
                user_response_list.append(restaurant_details)

            email_body_list = []
            for restaurant in restaurant_list:
                restaurant_details = '{0} in {1} has been rated {2} with price for two as {3}.'.format(
                    restaurant['name'], restaurant['address'], restaurant['rating'], restaurant["average_cost_for_two"])
                email_body_list.append(restaurant_details)

            dispatcher.utter_message("-----"+"\n".join(user_response_list))
            return [SlotSet('location', loc), SlotSet('cuisine', cuisine), SlotSet('price', price), SlotSet('email_body', "\n".join(email_body_list))]


class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        email = tracker.get_slot('emailid')
        email_body = tracker.get_slot('email_body')
        print('email', email)
        print('email_body', email_body)
        msg = EmailMessage()
        msg['Subject'] = 'Top restaurant from Zomato'
        msg['From'] = 'rasabot20@gmail.com'
        msg['To'] = email

        msg.set_content(email_body)
        with smtplib.SMTP_SSL('smtp.gmail.com', port) as smtp:
            smtp.login('rasabot20@gmail.com', password)
            smtp.send_message(msg)
        dispatcher.utter_message("Restaurant details have been sent.")
        return [SlotSet('emailid', email), SlotSet('email_body', None)]


class ActionValidateCity(Action):
    def name(self):
        return 'action_validate_city'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        if(loc.lower() not in cities):
            dispatcher.utter_message("We do not operate in that area yet.")
            return [SlotSet('location', None), SlotSet('is_valid_location', False)]

        return [SlotSet('location', loc.lower()), SlotSet('is_valid_location', True)]


class ActionValidateCuisine(Action):
    def name(self):
        return 'action_validate_cuisine'

    def run(self, dispatcher, tracker, domain):
        cuisine = tracker.get_slot('cuisine')
        if(cuisine.lower() not in cuisines_dict):
            dispatcher.utter_message(
                "The selected cuisine is not valid. Please select a valid cuisine")
            return [SlotSet('cuisine', None), SlotSet('is_valid_cuisine', False)]

        return [SlotSet('cuisine', cuisine.lower()), SlotSet('is_valid_cuisine', True)]

# Reference:  https://blog.rasa.com/building-contextual-assistants-with-rasa-formaction/
class RestaurantForm(FormAction):
    def name(self):
        return "restaurant_form"

	@staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["cuisine", "num_people", "outdoor_seating",
                "preferences", "feedback"]

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_sdk import Tracker
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted

import zomatopy
import json
import email
from email.message import EmailMessage
import smtplib
import ssl
import os
import re

port = 465  # For SSL
password = "rasa@2020"

cities = set()
fh = open('data/cities.txt')
for line in fh:
    cities.add(line.strip().lower())
fh.close()

email_pattern = re.compile(r"(\w+[.|\w])*@(\w+[.])*\w+")

cuisines_dict = {'mexican': 73, 'chinese': 25, 'american': 1,
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
        is_valid_search_request = tracker.get_slot('is_valid_search_request')
        restaurant_list = []
        print("Location: {} ", loc)
        print("Cuisine: {} ", cuisine)
        print("price: {} ", price)
        try:
            if not is_valid_search_request:
                raise Exception("Data not valid")
            restaurant_list = zomato.getTopRestaurants(
                loc, str(cuisines_dict.get(cuisine)), price_dict[price])
        except:
            dispatcher.utter_message(
                "Sorry, we were not able to find the restaurants. Please try again")
            return [SlotSet('location', None),
                    SlotSet('cuisine', None),
                    SlotSet('price', None),
                    SlotSet('is_valid_search_request', None),
                    SlotSet('is_data_found', False)]

        if len(restaurant_list) == 0:
            print("No results to return")
            response = "Sorry, we were not able to find any restaurant with this criteria."
            dispatcher.utter_message(response)
            return [SlotSet('location', None),
                    SlotSet('cuisine', None),
                    SlotSet('price', None),
                    SlotSet('is_valid_search_request', None),
                    SlotSet('is_data_found', False)]
        else:
            user_response_list = []
            for restaurant in restaurant_list[:5]:
                restaurant_details = '{0} in {1} has been rated {2}.'.format(
                    restaurant['name'], restaurant['address'], restaurant['rating'])
                user_response_list.append(restaurant_details)

            email_body_list = []

            restaurant_item_template = '''
                <h3>Restaurant #{4}</h3>
                <ul>
                    <li>Restaurant Name: {0}</li>
                    <li> Restaurant locality address: {1}</li>
                    <li> Average budget for two people: Rs. {2}</li>
                    <li> Zomato user rating: {3}</li>
               </ul>
            '''

            for count, restaurant in enumerate(restaurant_list, start=1):
                restaurant_details = restaurant_item_template.format(
                    restaurant['name'], restaurant['address'], restaurant["average_cost_for_two"], restaurant['rating'], count)
                email_body_list.append(restaurant_details)
            email_body = '<ul>' + "<br/>".join(email_body_list) + '</ul>'
            dispatcher.utter_message(
                "Here are some of the best match restaurants:\n\n")
            dispatcher.utter_message("\n\n".join(user_response_list))
            return [SlotSet('location', None),
                    SlotSet('cuisine', None),
                    SlotSet('price', None),
                    SlotSet('is_data_found', True),
                    SlotSet('is_valid_search_request', None),
                    SlotSet('email_body', email_body)]


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
        try:
            msg.set_content(email_body, subtype='html')
            with smtplib.SMTP_SSL('smtp.gmail.com', port) as smtp:
                smtp.login('rasabot20@gmail.com', password)
                smtp.send_message(msg)
            dispatcher.utter_message("Restaurant details have been sent.")
            return [SlotSet('emailid', None), SlotSet('email_body', None), SlotSet('is_data_found', None), SlotSet('is_valid_email', None)]
        except:
            dispatcher.utter_message(
                "Sorry, we were not able to end the email Please try again")
            return [SlotSet('emailid', email), SlotSet('email_body', email_body), SlotSet('is_valid_email', None)]


class ActionValidateEmail(Action):
    def name(self):
        return 'action_validate_email'

    def run(self, dispatcher, tracker, domain):
        email = tracker.get_slot('emailid')
        print('checking email', email)
        if(email and email_pattern.match(email)):
            return [SlotSet('emailid', email), SlotSet('is_valid_email', True)]
        else:
            return [SlotSet('emailid', None), SlotSet('is_valid_email', False)]


class ActionValidateCity(Action):
    def name(self):
        return 'action_validate_city'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        print("Checking city: ", loc)
        if not loc or (loc.lower() not in cities):
            return [SlotSet('location', None)]

        return [SlotSet('location', loc.lower())]


class ActionValidateCuisine(Action):
    def name(self):
        return 'action_validate_cuisine'

    def run(self, dispatcher, tracker, domain):
        cuisine = tracker.get_slot('cuisine')
        print("Checking cuisine: ", cuisine)
        if not cuisine or (cuisine.lower() not in cuisines_dict):
            return [SlotSet('cuisine', None)]

        return [SlotSet('cuisine', cuisine.lower())]


class ActionValidatePrice(Action):
    def name(self):
        return 'action_validate_price'

    def run(self, dispatcher, tracker, domain):
        price = tracker.get_slot('price')
        print("Checking price: ", price)
        if not price or (price.lower() not in price_dict):
            return [SlotSet('price', None)]

        return [SlotSet('price', price.lower())]


class ActionValidateRequestData(Action):
    def name(self):
        return 'action_validate_request_data'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price = tracker.get_slot('price')
        print("Location: {} ", loc)
        print("Cuisine: {} ", cuisine)
        print("price: {} ", price)

        if loc and cuisine and price:
            return [SlotSet('is_valid_search_request', True)]
        else:
            return [SlotSet('is_valid_search_request', False)]


class ActionFallback(Action):

    def name(self):
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            "I did not understand the previous response, please be more specific.")
        return [UserUtteranceReverted()]

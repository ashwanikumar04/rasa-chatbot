from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
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


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        config = {"user_key": "50aadfe48ced3c06244a29a7381ac7eb"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        results = zomato.restaurant_search(
            "", lat, lon, str(cuisines_dict.get(cuisine)), 5)
        d = json.loads(results)
        responseList = []
        if d['results_found'] == 0:
            response = "no results"
        else:
            # {restaurant_name} in {restaurant_address} has been rated {rating}.
            # for restaurant in d['restaurants']:
            #     restaurantDetails = "{0} in {1} has been rated {2}.".format(restaurant['restaurant']['name'], restaurant['restaurant']['location']['address'], restaurant['restaurant']['user_rating']['aggregate_rating'] )
            #     responseList.append()
            response = "result found"
        dispatcher.utter_message("-----"+response)
        return [SlotSet('location', loc)]


class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        email = tracker.get_slot('emailid')
        email_body = tracker.get_slot('email_body')
        print('email', email)
        print('email_body', email_body)
        msg = EmailMessage()
        msg['Subject'] = 'Top 5 restaurants'
        msg['From'] = 'rasabot20@gmail.com'  # sender's email address
        msg['To'] = email  # receiver's email address

        msg.set_content('test email from bot')
        with smtplib.SMTP_SSL('smtp.gmail.com', port) as smtp:
            # replace with your email and password
            smtp.login('rasabot20@gmail.com', password)
            smtp.send_message(msg)
        dispatcher.utter_message("email sent")
        return [SlotSet('email', email), SlotSet('top_5_restaurants', None)]


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



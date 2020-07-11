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
fh = open('cities.txt')
for line in fh:
    cities(line.strip().lower())
fh.close()

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
        cuisines_dict = {'bakery': 5, 'chinese': 25, 'cafe': 30,
                         'italian': 55, 'biryani': 7, 'north indian': 50, 'south indian': 85}
        results = zomato.restaurant_search(
            "", lat, lon, str(cuisines_dict.get(cuisine)), 5)
        d = json.loads(results)
        response = ""
        if d['results_found'] == 0:
            response = "no results"
        else:
            for restaurant in d['restaurants']:
                response = response + "Found " + \
                    restaurant['restaurant']['name'] + " in " + \
                    restaurant['restaurant']['location']['address']+"\n"

        # msg = EmailMessage()
        # msg['Subject'] = 'Days Off Request'
        # msg['From'] = 'rasabot20@gmail.com'  # sender's email address
        # msg['To'] = 'ashwanikumar04@gmail.com'  # receiver's email address

        # msg.set_content('Hi,\nOur member {} has submitted a days off request starting from {} to {} (if both dates are same, its a one day leave request). The reason for the leave request is \"{}\" currently \"{}\". Please acknowledge this request. \nYour\'s sincerely,\nYour-bot')

        # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        #     # replace with your email and password
        #     smtp.login('rasabot20@gmail.com', password)
        #     smtp.send_message(msg)
        dispatcher.utter_message("-----"+response)
        return [SlotSet('location', loc)]


class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        email = tracker.get_slot('email')
        top_5_restaurants = tracker.get_slot('top_5_restaurants')
        print('email', email)
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

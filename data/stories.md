## Valid data one by one followed by sending email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* notify{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_city
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* notify{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* notify{"price": "economic"}
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
* affirm
    - utter_ask_email
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

## price and cuisine together followed by location and send email

* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "price": "expensive"}
    - slot{"cuisine": "italian"}
    - slot{"price": "expensive"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - action_validate_price
    - slot{"price": "expensive"}
    - utter_ask_location
* notify{"location": "pune"}
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
* affirm
    - utter_ask_email
* send_email{"emailid": "deepak.4ev@gmail.com"}
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


## Search restaurant with valid location and price followed by valid cuisine with no email
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price": "moderate"}
    - slot{"location": "delhi"}
    - slot{"price": "moderate"}
    - action_validate_city
    - slot{"location": "delhi"}
    - action_validate_price
    - slot{"price": "moderate"}
    - utter_ask_cuisine
* notify{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - action_validate_request_data
    - slot{"is_valid_search_request": true}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_data_found": true}
    - slot{"is_valid_search_request": null}
    - slot{"email_body": "Wenger's in A 16, Connaught Place, New Delhi has been rated 4.7 with price for two as 400.\n\nAMA Cafe in House 6, New Colony, Majnu ka Tilla, New Delhi has been rated 4.6 with price for two as 550.\n\nWenger's Deli in A 18, Radial Road, Connaught Place, New Delhi has been rated 4.6 with price for two as 500.\n\nMaxims Pastry Shop in HS-3, Main Market, Kailash Colony, New Delhi has been rated 4.6 with price for two as 300.\n\nC.I.A. Call It Asiian in 13 - 16, Narmada Shopping Complex, Near Don Bosco School, Alaknanda Road, Greater Kailash 2 (GK 2), New Delhi has been rated 4.5 with price for two as 700.\n\nAKU'S - The Burger Co. in Shop 47, Ground Floor, Main Market, Defence Colony, New Delhi has been rated 4.5 with price for two as 600.\n\nBurgerama in Plot B, 96, Ground Floor, Zamrudpur, Greater Kailash 1 (GK 1), New Delhi has been rated 4.5 with price for two as 600.\n\nYum Yum Burger in DG 58, Rodeo Drive Market, Sector 49, Gurgaon has been rated 4.5 with price for two as 500.\n\nThe Burger Xpress in Rohini, New Delhi has been rated 4.5 with price for two as 400.\n\nMr. Crust Bakers in B 29/B, Opposite Mother Dairy, Vijay Nagar, New Delhi has been rated 4.4 with price for two as 500."}
    - utter_ask_for_result_email
* deny
    - utter_goodbye
    - action_restart

## All together with email
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "Mysore", "price": "expensive"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "Mysore"}
    - slot{"price": "expensive"}
    - action_validate_city
    - slot{"location": "mysore"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - action_validate_price
    - slot{"price": "expensive"}
    - action_validate_request_data
    - slot{"is_valid_search_request": true}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_data_found": true}
    - slot{"is_valid_search_request": null}
    - slot{"email_body": "Spring - Radisson Blu Plaza in Radisson Blu Plaza, 1, MG Road, Ittige Gudu, Mysore has been rated 4.5 with price for two as 1700.\n\nJalpaan Dining Saga in 366, 2nd & 3rd Floor, Near Ramaswamy Circle, Chamaraja Mohalla, Chamrajpura, Mysore has been rated 4.4 with price for two as 900.\n\nKapoor's Cafe in 3132, D 27 & 3132/A, D 27/A, Kalidasa Road, VV Mohalla, Jayalakhsmipuram, Mysore has been rated 4.4 with price for two as 800.\n\nKapoor's Cafe in H/8C, Kantharaja Urs Road, Bogadi Sharadevi Nagar, Chamrajpura, Mysore has been rated 4.4 with price for two as 800.\n\nGufha Restaurant in 35/A, Pai Hotels, Bangalore Nilgiri Road, Doora, Mysore has been rated 4.3 with price for two as 1000.\n\nSepoy's Phirangi in Opp JSS Hospital,  MG Road, Chamrajpura, Mysore has been rated 4.2 with price for two as 1000.\n\nBig Chicken in 331/A, Loyal World Building, Adjacent To St Josephs Hospital, Bannimantap, Mysore has been rated 4.1 with price for two as 1000.\n\nThe Barge Restaurant in Plot 440A, Hebbal Industrial Area, Near Infosys Campus, Vijay Nagar, Mysore has been rated 4.1 with price for two as 1500.\n\nWhite Lantern in 9/A, 3rd Block, Gokulam Main Road, Jayalakshmipuram, Mysuru, Karnataka has been rated 4.1 with price for two as 800.\n\nPurple Haze in 129-131, High Tension Double Road, Mahadeswara Badavane, 2nd Stage, Vijay Nagar, Mysore has been rated 4.1 with price for two as 1200."}
    - utter_ask_for_result_email
* affirm
    - utter_ask_email
* send_email{"emailid": "deepak.4ev@gmail.com"}
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

## Wrong cuisine with location followed by correct cuisine with no email
* greet
    - utter_greet
* restaurant_search{"cuisine": "french", "location": "Bhopal"}
    - slot{"cuisine": "french"}
    - slot{"location": "Bhopal"}
    - action_validate_city
    - slot{"location": "bhopal"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_wrong_cuisine
    - utter_ask_cuisine
* notify{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* notify{"price": "economic"}
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
    - slot{"email_body": "Sagar Gaire Fast Food : Platinum Plaza in Shop  33-34,Ground Floor, Platinum Plaza, TT Nagar, Bhopal has been rated 4.4 with price for two as 250.\n\nSagar Gaire Fast Food : Arera Colony in 10, Number Market, Arera Colony, Bhopal has been rated 4.4 with price for two as 250.\n\nSagar Gaire Fast Food : Jhangirabad in 615-A, 80 Feet Road, Ashoka Garden, Jhangirabad, Bhopal has been rated 4.3 with price for two as 250.\n\nMamaji Jalebi Wale in 8 & 9, Lakherapura, Peer Gate Area, Ibrahimpura, Peer Gate Area has been rated 4.3 with price for two as 200.\n\nSagar Gaire Fast Food : DIG Bungalow in 12, Sant Kavaram Colony, Berasia Road, JP Nagar, Bhopal has been rated 4.3 with price for two as 250.\n\nSagar Gaire Fast Food : 7 Number in Shop 101, B.D.A Complex, Habib Ganj, Bhopal has been rated 4.2 with price for two as 250.\n\nSagar Gaire Fast Food - Idgah Hills in Shop 1, 2, 3, Meenakshi Complex, Aali Manzil Road, Niyamatpura, Idgah Hills, Bhopal has been rated 4.2 with price for two as 250.\n\nSagar Gaire Fast Food : Airport Road in 106-107/1/4/1, Near Elixir Garden, New Jail Road, Karond, Airport Area, Bhopal has been rated 4.2 with price for two as 250.\n\nSagar Gaire Fast Food : Kolar in 17-20, Ultimate Arcade, Sarvdharm Sector B, Main Road, Kolar, Bhopal has been rated 4.2 with price for two as 250.\n\nSagar Gaire Fast Food : ISBT in 28, ISBT Commercial Campus, Near Chetak Bridge, Maharana Pratap Nagar, Bhopal has been rated 4.2 with price for two as 250."}
    - utter_ask_for_result_email
* deny
    - utter_goodbye
    - action_restart

## Wrong location followed by correct location with all the correct data with not email
* greet
    - utter_greet
* restaurant_search{"location": "Munnar"}
    - slot{"location": "Munnar"}
    - action_validate_city
    - slot{"location": null}
    - utter_wrong_location
    - utter_ask_location
* restaurant_search{"location": "Rajkot"}
    - slot{"location": "Rajkot"}
    - action_validate_city
    - slot{"location": "rajkot"}
    - utter_ask_cuisine
* notify{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_price
* notify{"price": "economic"}
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
    - slot{"email_body": "Anand Snacks in 20 New Jagnath Plot, Dhanrajni Complex Dr. Yagnik, Dr Yagnik Road, Rajkot has been rated 4.4 with price for two as 150.\n\nMahakali  Bhel & Fast Food in Omkar Complex Nirmala Main Road Kotecha Nagar, Rajkot has been rated 4.3 with price for two as 200.\n\nGJ-5 Sandwich And Pizza in Jyoti Nagar Chowk, Behind Crystal Mall, Kalawad Road, Rajkot has been rated 4.3 with price for two as 200.\n\nDev Fast Food in Opposite Nirmala Convent School, Kotecha Nagar, Rajkot has been rated 4.2 with price for two as 200.\n\nFill In Fast Food and Chinese in Opp bank of baroda Shop 9, Nutan nagar shopping center, Kalawad Road, Kotecha Nagar, Rajkot has been rated 4.0 with price for two as 200.\n\nThe Maggi Centre in Shopno 7 Behind Wockhart hospital Jalaram 2 University Road  Kotecha Nagar, Rajkot has been rated 4.0 with price for two as 200.\n\nMor N Rich in 20, Jagnath Plot, Dr Yagnik Road, Rajkot has been rated 4.0 with price for two as 200.\n\nThe Maggi Centre in Suvarn Complex, Opposite Doshi Plaza Appartment, Jalaram-2, University Road, Kotecha Nagar, Rajkot has been rated 4.0 with price for two as 200.\n\nBrown Burger Co in Shop 4, Ground Floor, Near Tea Post, Race Course Road, Rajkot has been rated 3.9 with price for two as 250.\n\nHimalay Soda & Softy in Shop No. 4, Javerchand Meghani Tower, University Road, Near Panchayat Chowk, Rajkot, Gujarat 360005 has been rated 3.9 with price for two as 200."}
    - utter_ask_for_result_email
* deny
    - utter_goodbye
    - action_restart

## Search in valid location with wrong price range followed by correct price range and no email
* greet
    - utter_greet
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_validate_city
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* notify{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_price
* notify{"price": "600-800"}
    - slot{"price": "600-800"}
    - action_validate_price
    - slot{"price": null}
    - utter_wrong_price
    - utter_ask_price
* notify{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_validate_price
    - slot{"price": "moderate"}
    - action_validate_request_data
    - slot{"is_valid_search_request": true}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_data_found": true}
    - slot{"is_valid_search_request": null}
    - slot{"email_body": "Fusilli Reasons in 2/64, Ormes Main Road, Kilpauk, Chennai has been rated 4.5 with price for two as 400.\n\nMezze in Abhinav center, old no.19, new, no.14, Co Operative Colony Rd, Alwarpet, Chennai.  has been rated 4.5 with price for two as 700.\n\nOink in 5/47, Sterling Avenue, Nungambakkam, Chennai has been rated 4.5 with price for two as 500.\n\nBurgerMan in 31, 4th Main Road, Besant Nagar, Chennai has been rated 4.4 with price for two as 450.\n\nCafe CakeBee in 50, Seethammal Road, Off TTK Road, Alwarpet, Chennai has been rated 4.4 with price for two as 650.\n\nAegam in 1, Gurusamy Nagar Main Road, Gowrivakkam, Selaiyur, Chennai has been rated 4.4 with price for two as 500.\n\nSathyam Cinemas in 8, Thiruvika Road, Royapettah, Chennai has been rated 4.4 with price for two as 300.\n\nMomo Ke Baap in Shop 25, Corporation Shopping Complex, Indira Nagar, Adyar, Chennai has been rated 4.4 with price for two as 350.\n\nBlind Ch3mistry in 7/2 M, 4th Main Road, Besant Nagar, Chennai has been rated 4.3 with price for two as 700.\n\nBlind Ch3mistry in Old 11, New 19, 1st Floor, Brindhavan Apartment, Khader Nawaz Khan Road, Nungambakkam, Chennai has been rated 4.3 with price for two as 700."}
    - utter_ask_for_result_email
* deny
    - utter_goodbye
    - action_restart

## Valid search with no data
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "Asansol"}
    - slot{"cuisine": "american"}
    - slot{"location": "Asansol"}
    - action_validate_city
    - slot{"location": "asansol"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_price
* notify{"price": "expensive"}
    - slot{"price": "expensive"}
    - action_validate_price
    - slot{"price": "expensive"}
    - action_validate_request_data
    - slot{"is_valid_search_request": true}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_valid_search_request": null}
    - slot{"is_data_found": false}
    - utter_goodbye
    - action_restart


## Valid search with no data
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* notify{"location": "Purulia"}
    - slot{"location": "Purulia"}
    - action_validate_city
    - slot{"location": "purulia"}
    - utter_ask_cuisine
* notify{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* notify{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_validate_price
    - slot{"price": "moderate"}
    - action_validate_request_data
    - slot{"is_valid_search_request": true}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_valid_search_request": null}
    - slot{"is_data_found": false}
    - utter_goodbye
    - action_restart
  

## valid search with wrong email followed by correct email
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* notify{"location": "Nellore"}
    - slot{"location": "Nellore"}
    - action_validate_city
    - slot{"location": "nellore"}
    - utter_ask_price
* notify{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_validate_price
    - slot{"price": "moderate"}
    - action_validate_request_data
    - slot{"is_valid_search_request": true}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_data_found": true}
    - slot{"is_valid_search_request": null}
    - slot{"email_body": "Hotel Reshma in Mahatma Gandhi Nagar Road, Vedayapalem, Nellore - 524004, Opposite Nallapa Reddy Srinivasulu Reddy Statue, Nellore Locality, Nellore has been rated 4.2 with price for two as 300.\n\nIndies Family Dhaba in Door No 2B, Mini Bypass, Bv Nagar, Nellore, Oppsite ANR Function Hall&near Royalenfield Service Station, Nellore Locality, Nellore has been rated 4.1 with price for two as 450.\n\nR R Family Dhaba Veg in SALI STREET, BESIDE KALESWARA TRANSPORT, STONEHOUSEPET, NELLORE. has been rated 4.1 with price for two as 300.\n\nTharanga @ Athidhi Grand in Reliance Upstairs, Police Officers Road, Dargamitta, Nellore, Nellore Locality, Nellore has been rated 4.1 with price for two as 300.\n\nSalma Biriyani in Shop No -2(B), Balajinagar, Nellore - 524002, Masjid Center, Nellore Locality, Nellore has been rated 4.0 with price for two as 300.\n\nSai Ram Malla Reddy Dhaba in Thalpagiri colony, Opp NH 5 Building, Ayyappagudi circle towards NH, Nellore, Nellore Locality, Nellore has been rated 4.0 with price for two as 350.\n\nR Bawarchi 2 in 26/3/171, Mini Bypass Road, BV Nagar, Nellore.  has been rated 3.9 with price for two as 600.\n\nHotel Noor in 18, Achari St, Vrc Centre, Achari Street, Nellore - 524001, Near Collctor Office, Barkas Center, Nellore Locality, Nellore has been rated 3.9 with price for two as 350.\n\nCelebrations Multicuisine Restaurant in Kings court Avenue, Magunta layout main road, Magunta Layout, Nellore has been rated 3.8 with price for two as 300.\n\nThe Mint Multicuisine Restaurant in 23/1184, Sodhan Nagar, Beside Rtc, Nellore Locality, Nellore has been rated 3.8 with price for two as 450."}
    - utter_ask_for_result_email
* affirm
    - utter_ask_email
* send_email
    - action_validate_email
    - slot{"emailid": null}
    - slot{"is_valid_email": false}
    - utter_wrong_email
    - utter_ask_email
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

## Wrong place followed by correct place and send email
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_city
    - slot{"location": null}
    - utter_wrong_location
    - utter_ask_location
* restaurant_search{"location": "prayagraj"}
    - slot{"location": "prayagraj"}
    - action_validate_city
    - slot{"location": "prayagraj"}
    - utter_ask_cuisine
* notify{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* notify{"price": "expensive"}
    - slot{"price": "expensive"}
    - action_validate_price
    - slot{"price": "expensive"}
    - action_validate_request_data
    - slot{"is_valid_search_request": true}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_data_found": true}
    - slot{"is_valid_search_request": null}
    - slot{"email_body": "Sagar Ratna in 3/3, Hashimpur Road, Balson Crossing, Near Anand Bhawan, Tagore Town, Allahabad has been rated 4.5 with price for two as 800.\n\nOld School Cafe in 2nd Floor, 9-10 Tulsiani Grace, Civil Lines, Allahabad has been rated 4.5 with price for two as 1000.\n\nEl Chico Restaurant in 142A, 32, Mahatma Gandhi, Civil Lines, Allahabad has been rated 4.4 with price for two as 800.\n\nEDEN by Connoisseur in Hotel Samrat, Civil Lines, Allahabad has been rated 4.4 with price for two as 1000.\n\nPind Balluchi in 48/8, Stratchy Road, Civil Lines, Allahabad has been rated 4.4 with price for two as 1000.\n\nBerco's in 17C, 0-1, Stretchy Road, Civil Lines, Allahabad has been rated 4.2 with price for two as 1600.\n\nHotel Kanha Shyam in Allahabad HO, Civil Lines, Allahabad has been rated 4.1 with price for two as 900.\n\nKohinoor Restaurant in LG1 - LG2, Lower Ground Floor, Vinayak Tower, MG Marg, Civil Lines, Allahabad has been rated 4.1 with price for two as 800.\n\nMoti Mahal Delux in Second Floor, Vinayak City Center Mall, SP Marg, Civil Lines, Allahabad has been rated 4.0 with price for two as 850.\n\nMoti Mahal Delux Tandoori Trail in Shop 18A, Second Floor, Sardar Patel Marg, Above HDFC Bank, Civil Lines, Allahabad has been rated 3.9 with price for two as 800."}
    - utter_ask_for_result_email
* affirm
    - utter_ask_email
* send_email{"emailid": "deepak.4ev@gmail.com"}
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

## Wrong cuisine with Location followed by correct cuisine and then price with email
* greet
    - utter_greet
* restaurant_search{"cuisine": "thaai", "location": "Nagpur"}
    - slot{"cuisine": "thaai"}
    - slot{"location": "Nagpur"}
    - action_validate_city
    - slot{"location": "nagpur"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_wrong_cuisine
    - utter_ask_cuisine
* notify{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* notify{"price": "economic"}
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
    - slot{"email_body": "Kesariya Cake Shopee in 280,Wardhaman Nagar Square, Nagpur has been rated 4.2 with price for two as 200.\n\nFood For Foodies in Plot 58, Somwari Peth, Near Gajanan Mandir, Ayodhya Nagar, Nagpur has been rated 4.2 with price for two as 250.\n\nKhau Galli in 11, Santaji Society, Near Railway Crossing, Manish Layout, Manish Nagar, Nagpur has been rated 4.1 with price for two as 200.\n\nGuptaji's Pani Puri Corner in Plot 19, Narkesri Appartment, Deo Nagar Square, Vivekanand Nagar, Nagpur has been rated 4.1 with price for two as 150.\n\nSpicy Fast Food in Sufiyer Complex, Amravati Road, Bharat Nagar, Vayusena nagar, Nagpur has been rated 4.0 with price for two as 250."}
    - utter_ask_for_result_email
* affirm
    - utter_ask_email
* send_email{"emailid": "ashwani.kumar04@gmail.com"}
    - slot{"emailid": "ashwani.kumar04@gmail.com"}
    - action_validate_email
    - slot{"emailid": "ashwani.kumar04@gmail.com"}
    - slot{"is_valid_email": true}
    - action_send_email
    - slot{"emailid": null}
    - slot{"email_body": null}
    - slot{"is_data_found": null}
    - slot{"is_valid_email": null}
    - utter_goodbye
    - action_restart

## location with price followed by cuisine with no email
* greet
    - utter_greet
* restaurant_search{"location": "Solapur", "price": "moderate"}
    - slot{"location": "Solapur"}
    - slot{"price": "moderate"}
    - action_validate_city
    - slot{"location": "solapur"}
    - action_validate_price
    - slot{"price": "moderate"}
    - utter_ask_cuisine
* notify{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - action_validate_request_data
    - slot{"is_valid_search_request": true}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_data_found": true}
    - slot{"is_valid_search_request": null}
    - slot{"email_body": "Hotel Bhaijaan in CTS 201/1, Shop 2, 3, 4, 7, Krushan Plaza, Hotgi Road, Solapur Locality, Solapur has been rated 4.5 with price for two as 400.\n\nHotel Yash Palace in 69 Castle Apartment, Station Road, Solapur - 413001, Opp Mahapaur Banglow, Solapur Locality, Solapur has been rated 4.4 with price for two as 400.\n\nAnand Restaurant in Anand Hotel Opposite to Oasis Mall Muraji path Solapur 413001 has been rated 4.2 with price for two as 350.\n\nHotel Yatiraj in 111 modi khana near modi police station saat rasta solapur, Solapur Locality, Solapur has been rated 4.2 with price for two as 350.\n\nHotel Shourya Veg And Nonveg in Plot No 1829, Datta Nagar, Solapur - 413005, Opposite New WIT College, Behind Tana Ban, Solapur has been rated 4.1 with price for two as 300.\n\nGanesh Bhuwan Iddli Gruha in shop 8&9 city corner saraswati chowk soloapur, Solapur Locality, Solapur has been rated 4.1 with price for two as 400.\n\nHotel Sai Prasad Executive in 8/2, Railway Lines, Ramlal Chowk Solapur Locality, Solapur has been rated 4.0 with price for two as 300.\n\nHotel Priyanka in 131, Siddheshwar Peth, Civil Chowk, Solapur Locality, Solapur has been rated 3.9 with price for two as 500.\n\nSheetal Dining Hall Pure Veg in 93/C, Oppossite Bhagwat Theatre, Gold Finch Peth, Solapur Locality, Solapur has been rated 3.9 with price for two as 350.\n\nHotel Mantralaya in 8389/3, BNR Jawahar Appartment 162, Railway Line, Solapur Locality, Solapur has been rated 3.9 with price for two as 300."}
    - utter_ask_for_result_email
* deny
    - utter_goodbye
    - action_restart

## valid search with no data
* restaurant_search{"location": "Jammu"}
    - slot{"location": "Jammu"}
    - action_validate_city
    - slot{"location": "jammu"}
    - utter_ask_cuisine
* notify{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "economic"}
    - slot{"price": "economic"}
    - action_validate_price
    - slot{"price": "economic"}
    - action_validate_request_data
    - slot{"is_valid_search_request": true}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_valid_search_request": null}
    - slot{"is_data_found": false}
    - utter_goodbye
    - action_restart

## Search with price range wrong followed by correct
* greet
    - utter_greet
* restaurant_search{"price": "within 1000"}
    - slot{"price": "within 1000"}
    - action_validate_price
    - slot{"price": null}
    - utter_wrong_price
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_validate_price
    - slot{"price": "moderate"}
    - utter_ask_location
* notify{"location": "Goa"}
    - slot{"location": "Goa"}
    - utter_ask_cuisine
* notify{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - action_validate_request_data
    - slot{"is_valid_search_request": true}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_data_found": true}
    - slot{"is_valid_search_request": null}
    - slot{"email_body": "Caravela Cafe and Bistro in Caravela Homestay, House 27, 31st January Road, Panaji, Goa has been rated 4.4 with price for two as 700.\n\nDa Tita's in Majorda Nuvem Road, Majorda, Goa has been rated 4.4 with price for two as 600.\n\nAJ's in House 1336, K.K. White House, Don Bosco Road, Murida, Fatorda, Margao, Goa has been rated 4.4 with price for two as 500.\n\nMagic Italy in Palolem Road, Palolem, Goa has been rated 4.4 with price for two as 700.\n\nRoger's in Benaulim Beach, Benaulim, Goa has been rated 4.3 with price for two as 700.\n\nPiccola Roma in Chapora Road, Near Petrol Pump, Vagator, Goa has been rated 4.1 with price for two as 700.\n\nCremeux Cafe & Bistro in 12/17, 1st Floor, MG Road, Panaji, Goa has been rated 4.1 with price for two as 600.\n\nLa Cucina in 749, Morjim, Goa has been rated 4.1 with price for two as 600.\n\nPizza Hut in 1/147/A, Gaura Vaddo, Calangute, Goa has been rated 4.0 with price for two as 600.\n\nDomino's Pizza in 10-11, Old Municipal Building, 18th June Road, Panaji, Goa has been rated 4.0 with price for two as 400."}
    - utter_ask_for_result_email
* affirm
    - utter_ask_email
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

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* notify{"location": "Jamnagar"}
    - slot{"location": "Jamnagar"}
    - action_validate_city
    - slot{"location": "jamnagar"}
    - utter_ask_cuisine
* notify{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_validate_price
    - slot{"price": "moderate"}
    - action_validate_request_data
    - slot{"is_valid_search_request": true}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_data_found": true}
    - slot{"is_valid_search_request": null}
    - slot{"email_body": "Imperial Blue Restaurant in Opp. Oshwal Hospital, Jamnagar, Digvijay Plot, Jamnagar. has been rated 4.6 with price for two as 300.\n\nBlack Pepper Restaurant in Shital Plot No 1, Near Hariya College, Jamnagar has been rated 4.5 with price for two as 500.\n\nHotel Aram in Hotel Aram, opp DKV college has been rated 4.4 with price for two as 500.\n\nVividh Food Zone in Digjam Circle, Khambhaliya Road, Jamnagar has been rated 4.4 with price for two as 400.\n\nHotel Keshwara's in Jamnagar Bypass Road, After Swaminarayan Temple, Jamnagar has been rated 4.3 with price for two as 300.\n\nVeer Restaurant in Ground Floor Vinayak Plaza Aerodrome Road, Mayur Nagar Jamnagar has been rated 4.3 with price for two as 600.\n\nZayka Restaurant in Nr Dominoz, Paras Society, Panchvati, Jamnagar has been rated 4.2 with price for two as 400.\n\nFriendz Dosa Centre in 11 Patel Colony, PN Marg, Jamnagar has been rated 4.1 with price for two as 300.\n\nKathiyawadi Dining Hall  in 3rd Floor, Khandelwala Complex, 12- Patel Colony, Bedi Bandar Road, Jamnagar has been rated 4.1 with price for two as 300.\n\nNew Zayka Restaurant in Opposite Nawanagar Bank, Ranjitsagar Road, Green City, Jamnagar has been rated 3.9 with price for two as 400."}
    - utter_ask_for_result_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* notify{"location": "kakinada"}
    - slot{"location": "kakinada"}
    - action_validate_city
    - slot{"location": "kakinada"}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_validate_price
    - slot{"price": "moderate"}
    - action_validate_request_data
    - slot{"is_valid_search_request": true}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_valid_search_request": null}
    - slot{"is_data_found": false}
    - utter_goodbye
    - action_restart



## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* notify{"location": "Asansol"}
    - slot{"location": "Asansol"}
    - action_validate_city
    - slot{"location": "asansol"}
    - utter_ask_cuisine
* notify{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_price
* notify{"price": null}
    - slot{"price": null}
    - action_validate_price
    - slot{"price": null}
    - utter_wrong_price
    - utter_ask_price
* notify{"price": "economic"}
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
    - slot{"email_body": "<ul>\n                <h3>Restaurant #1</h3>\n                <ul>\n                    <li>Restaurant Name: Grill n Bite</li>\n                    <li> Restaurant locality address: shop no-4, Mohini Tower, Shristinagar, Asansol, Asansol Locality, Asansol</li>\n                    <li> Average budget for two people: Rs. 200</li>\n                    <li> Zomato user rating: 4.3</li>\n               </ul>\n            <br/>\n                <h3>Restaurant #2</h3>\n                <ul>\n                    <li>Restaurant Name: Punjabi Rasoi</li>\n                    <li> Restaurant locality address: GT road, rambandhu talaw, asansol, Asansol Locality, Asansol</li>\n                    <li> Average budget for two people: Rs. 250</li>\n                    <li> Zomato user rating: 4.3</li>\n               </ul>\n            <br/>\n                <h3>Restaurant #3</h3>\n                <ul>\n                    <li>Restaurant Name: Minar Food Product</li>\n                    <li> Restaurant locality address: Fairdeal Market, Bastin Bazar, Opp South Traffic Guard., Asansol Locality, Asansol</li>\n                    <li> Average budget for two people: Rs. 150</li>\n                    <li> Zomato user rating: 4.1</li>\n               </ul>\n            <br/>\n                <h3>Restaurant #4</h3>\n                <ul>\n                    <li>Restaurant Name: Lips Slip</li>\n                    <li> Restaurant locality address: Jagnath Plaza, Ground Floor, Girls College Road, Burnpur, Asansol - 713325, Near Chitra Cinema, Asansol Locality, Asansol</li>\n                    <li> Average budget for two people: Rs. 200</li>\n                    <li> Zomato user rating: 4.1</li>\n               </ul>\n            <br/>\n                <h3>Restaurant #5</h3>\n                <ul>\n                    <li>Restaurant Name: Hindustan Cake Walk</li>\n                    <li> Restaurant locality address: Laxmi Narayan Avenue, GT Road(East), Ushagram, Asansol West Bengal, Asansol Locality, Asansol</li>\n                    <li> Average budget for two people: Rs. 150</li>\n                    <li> Zomato user rating: 4.1</li>\n               </ul>\n            <br/>\n                <h3>Restaurant #6</h3>\n                <ul>\n                    <li>Restaurant Name: Gupshup</li>\n                    <li> Restaurant locality address: 4th floor, galaxy mall, burnpur road, asansol, Asansol Locality, Asansol</li>\n                    <li> Average budget for two people: Rs. 260</li>\n                    <li> Zomato user rating: 3.9</li>\n               </ul>\n            <br/>\n                <h3>Restaurant #7</h3>\n                <ul>\n                    <li>Restaurant Name: Vikinah</li>\n                    <li> Restaurant locality address: H C L Road Rupnarayanpur Bazar, Salanpur Asansol, Asansol Locality, Asansol</li>\n                    <li> Average budget for two people: Rs. 0</li>\n                    <li> Zomato user rating: 3.9</li>\n               </ul>\n            <br/>\n                <h3>Restaurant #8</h3>\n                <ul>\n                    <li>Restaurant Name: Ganpati Meet and Eat</li>\n                    <li> Restaurant locality address: Radha Nagar Road, Opposite Galaxy Mall, Burnpur, Asansol, Asansol Locality, Asansol</li>\n                    <li> Average budget for two people: Rs. 0</li>\n                    <li> Zomato user rating: 3.8</li>\n               </ul>\n            <br/>\n                <h3>Restaurant #9</h3>\n                <ul>\n                    <li>Restaurant Name: Appy's Kichen</li>\n                    <li> Restaurant locality address: GT Road, Barakar, Asansol, Asansol Locality, Asansol</li>\n                    <li> Average budget for two people: Rs. 0</li>\n                    <li> Zomato user rating: 0</li>\n               </ul>\n            <br/>\n                <h3>Restaurant #10</h3>\n                <ul>\n                    <li>Restaurant Name: Pizza Xpress Pizzeria</li>\n                    <li> Restaurant locality address: Lower Chelidanga, Asansol, Asansol Locality, Asansol</li>\n                    <li> Average budget for two people: Rs. 0</li>\n                    <li> Zomato user rating: 0</li>\n               </ul>\n            </ul>"}
    - utter_ask_for_result_email
* affirm
    - utter_ask_email
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

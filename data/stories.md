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
    - action_restart
  
## Price and Cuisine together followed by invalid city
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
    - action_restart

## Search restaurant one by one: location->cuisine->price->send-email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* notify{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_validate_city
    - slot{"location": "nashik"}
    - slot{"is_valid_location": true}
    - utter_ask_cuisine
* notify{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - slot{"is_valid_cuisine": true}
    - utter_ask_price
* goodbye{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_valid_cuisine": null}
    - slot{"is_valid_location": null}
    - slot{"email_body": "McDonald's in Opposite Big Bazaar, College Road, Nashik has been rated 4.3 with price for two as 500.\nMad Over Chicken in 1, Vishva Apartment, Near Bank Of Hyderabad, Thatte Nagar , Off College Road, College Road, Nashik has been rated 4.2 with price for two as 400.\nBurger King in G1, Thakker Majesty, College Road, Nashik has been rated 4.1 with price for two as 500.\nGolu's Rolls in Near Big Bazar Mall, College Road, Nashik has been rated 4.1 with price for two as 450.\nMcDonald's in Vijay Mamta Theater Complex, Shivaji Nagar, Nashik Road, Nasik has been rated 4.1 with price for two as 500.\nPizza Hut in Shop 4, Pratik Arcade, Shivaji Nagar, Nashik Pune Road, Pathardi Phata, Nashik has been rated 4.0 with price for two as 600.\nCafe Bliss in 6, Rushiraj Tower, Jehan Circle, Gangapur Road, College Road, Nashik has been rated 3.9 with price for two as 650.\nVenkys Chicken Experience in Shop 5 Satyam Leela Tower Near Pancham Hotel College Road Nashik has been rated 3.9 with price for two as 300.\nPizza Hut in Ground Floor, Metro 99 Off, Plot 456, Thatte Nagar, College Road, Nashik has been rated 3.8 with price for two as 600.\nUFO Fries and Corn in Shiv Om Building, Sant Kabir Nagar, Veer Sawarkar Nagar, Nashik has been rated 3.8 with price for two as 700."}
    - utter_ask_for_result_email
* affirm
    - utter_ask_email
* send_email{"emailid": "ashwani.kumar04@gmail.com"}
    - slot{"emailid": "ashwani.kumar04@gmail.com"}
    - action_send_email
    - slot{"emailid": null}
    - slot{"email_body": null}
    - utter_goodbye
    - action_restart

## Search restaurant one by one: location->cuisine->price->send-email
* greet
    - utter_greet
* restaurant_search{"people": "2"}
    - utter_ask_location
* notify{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_city
    - slot{"location": "delhi"}
    - slot{"is_valid_location": true}
    - utter_ask_cuisine
* notify{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - slot{"is_valid_cuisine": true}
    - utter_ask_price
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_valid_cuisine": null}
    - slot{"is_valid_location": null}
    - slot{"email_body": "The Big Chill Cakery in 3B, Main Market, Khan Market, New Delhi has been rated 4.8 with price for two as 700.\n\nWenger's in A 16, Connaught Place, New Delhi has been rated 4.7 with price for two as 400.\n\nThe Big Chill Cakery in Ground Floor, DLF Mall Of India, Sector 18, Noida has been rated 4.7 with price for two as 700.\n\nAMA Cafe in House 6, New Colony, Majnu ka Tilla, New Delhi has been rated 4.6 with price for two as 550.\n\nWenger's Deli in A 18, Radial Road, Connaught Place, New Delhi has been rated 4.6 with price for two as 500.\n\nMaxims Pastry Shop in HS-3, Main Market, Kailash Colony, New Delhi has been rated 4.6 with price for two as 300.\n\nJust Pizzas in 70, Baldev Park, Parwana Road, Gandhi Nagar, Near Apna Store, Chander Nagar, New Delhi has been rated 4.6 with price for two as 400.\n\nAzzurro Express in Greater Kailash 2 (GK2), New Delhi has been rated 4.5 with price for two as 650.\n\nThe Taste Maker in Uttam Nagar, New Delhi has been rated 4.5 with price for two as 600.\n\nTPP - The Pizza Project in Malviya Nagar, New Delhi has been rated 4.5 with price for two as 600."}
    - utter_ask_for_result_email
* affirm
    - utter_ask_email
* send_email{"emailid": "ashwani.kumar04@gmail.com"}
    - slot{"emailid": "ashwani.kumar04@gmail.com"}
    - action_send_email
    - slot{"emailid": null}
    - slot{"email_body": null}
    - utter_goodbye
    - action_restart

## Search restaurant with valid location and price followed by valid cuisine with email
* greet
    - utter_greet
* restaurant_search{"price": "economic", "location": "shimla"}
    - slot{"location": "shimla"}
    - slot{"price": "economic"}
    - action_validate_city
    - slot{"location": "shimla"}
    - slot{"is_valid_location": true}
    - utter_ask_cuisine
* notify{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"is_valid_cuisine": true}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_valid_cuisine": null}
    - slot{"is_valid_location": null}
    - slot{"email_body": "Gupta Ji Bhojnalya in Middle Bazaar, The Mall, Longwood, Shimla has been rated 4.0 with price for two as 150.\n\nCity Point in Sunbreeze Building 2nd floor , Sanjauli, Shimla has been rated 3.8 with price for two as 200.\n\nPappi Da Dhaba in Local Bus Stand, Sanjauli has been rated 3.7 with price for two as 150.\n\nAmar Dhaba in 16/1, Lakkar Bazar, Longwood, Shimla has been rated 3.5 with price for two as 150.\n\nBanshira Cafe in Kasumpti, Shimla has been rated 3.4 with price for two as 200.\n\nZayka New Singh's Tandoor in Shop 1 3/4, Lakkar Bazar, Summer Hill, Shimla has been rated 3.4 with price for two as 200.\n\nNew Singhs Tandoor in Shop 11, Middle Bazar, Summer Hill, Shimla has been rated 3.4 with price for two as 250.\n\nAmritsari Rasoi in 39/1, Above Dr. Pal Clinic, Lakkar Bazar, Shimla, Summer Hill, Shimla has been rated 3.3 with price for two as 200.\n\nLekh Raj fast food in Shop 96, Near DC office Shimla, Shimla has been rated 3.3 with price for two as 200.\n\nSharma Sweet Shop in Khalni Chownk, Shimla 171002, Panthaghati, Shimla has been rated 3.3 with price for two as 150."}
    - utter_ask_for_result_email
* affirm
    - utter_ask_email
* send_email{"emailid": "deepak4ev@gmail.com"}
    - slot{"emailid": "deepak4ev@gmail.com"}
    - action_send_email
    - slot{"emailid": null}
    - slot{"email_body": null}
    - utter_goodbye
    - action_restart

## Search restaurant with valid price, location and cuisine all together with no email
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mysore", "price": "economic"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mysore"}
    - slot{"price": "economic"}
    - action_validate_city
    - slot{"location": "mysore"}
    - slot{"is_valid_location": true}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"is_valid_cuisine": true}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_valid_cuisine": null}
    - slot{"is_valid_location": null}
    - slot{"email_body": "Hotel Cafe Mysore in 1206/A, N-4/A, New Street, 5th Cross, Opposite Karaga Temple, Ittige Gudu, Mysore has been rated 4.1 with price for two as 200.\n\nSri Devi Bhavan in 19, Seebai Road, Behind Dhanavathri Road, Devaraja Mohalla, Mandi Mohalla, Mysore has been rated 4.0 with price for two as 200.\n\nNew Palav Point in 1111, Udayaravi Road, Opposite Pramati School, Kuvempunagar, Mysore has been rated 3.9 with price for two as 200.\n\nSantrupthi Restaurant in #63, near Bharath cancer hospital, opp to kalyani hotel, Mysore has been rated 3.9 with price for two as 100.\n\nArz Bakes & Snacks in 6/1, Ground Floor, Opposite Teresian College, T Narsipur Main Road, Siddhartanagar, Ittige Gudu, Mysore has been rated 3.9 with price for two as 250.\n\nThe Bowl Factory in 174, Moksha Marga, Geetha School Road, Siddhartha Nagar, Ittige Gudu, Mysore has been rated 3.9 with price for two as 200.\n\nMysuru Food Court in 315/A, WAP Factory road, Hebbal Industrial Area, Vijay Nagar, Mysore has been rated 3.9 with price for two as 250.\n\nThe Bowl Factory in 115 , 3rd Floor , Sathya Complex ,  Kalidasa Road , Mysore.  has been rated 3.9 with price for two as 200.\n\nNew Mysore Refreshment in 12/1, Opposite Zoo Garden, Shalivahana Main Road, Ittige Gudu, Mysore has been rated 3.8 with price for two as 250.\n\nDose Corner in 19/1, Budda Marga, Opposite New D.C. Office, Bannur Main road, Siddartha Layout, Ittige Gudu, Mysore has been rated 3.8 with price for two as 200."}
    - utter_ask_for_result_email
* deny
    - utter_goodbye
    - action_restart

## Search restaurant with invalid city
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "ooty"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "ooty"}
    - action_validate_city
    - slot{"location": null}
    - slot{"is_valid_location": null}
    - utter_goodbye
    - action_restart

## Search restaurant with valid city and invalid cuisine followed by valid cuisine followed by wrong email then correct email
* restaurant_search{"cuisine": "french", "location": "Bhopal"}
    - slot{"cuisine": "french"}
    - slot{"location": "Bhopal"}
    - action_validate_city
    - slot{"location": "bhopal"}
    - slot{"is_valid_location": true}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - slot{"is_valid_cuisine": null}
    - utter_ask_cuisine
* notify{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"is_valid_cuisine": true}
    - utter_ask_price
* notify{"price": "economic"}
    - slot{"price": "economic"}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_valid_cuisine": null}
    - slot{"is_valid_location": null}
    - slot{"email_body": "Total Refreshing Point in Campion School Shahpura, Bhopal, Arera Colony, Bhopal has been rated 3.8 with price for two as 200.\n\nHotel Atishay in Mezzanine Floor, R 55, Zone 1, Maharana Pratap Nagar, Bhopal has been rated 3.7 with price for two as 200.\n\nMr. Petu in Shop no. 7 , hawkers corner 6 no. Bus stop shivaji nagar bhopal has been rated 3.3 with price for two as 200.\n\nDesi Fusion By Firangi Cafe in Shop 3, 35 Zone-2, MP Nagar, Bhopal, Maharana Pratap Nagar, Bhopal has been rated 0 with price for two as 250."}
    - utter_ask_for_result_email
* affirm
    - utter_ask_email
* send_email{"emailid": "deepak4ev.gmail.com"}
    - slot{"emailid": "deepak4ev.gmail.com"}
    - action_validate_email
    - slot{"emailid": null}
    - utter_ask_email
* send_email{"emailid": "deepak4ev@gmail.com"}
    - slot{"emailid": "deepak4ev@gmail.com"}
    - action_send_email
    - slot{"emailid": null}
    - slot{"email_body": null}
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"price": "moderate", "location": "pune"}
    - slot{"location": "pune"}
    - slot{"price": "moderate"}
    - action_validate_city
    - slot{"location": "pune"}
    - slot{"is_valid_location": true}
    - utter_ask_cuisine
* notify{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"is_valid_cuisine": true}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_valid_cuisine": null}
    - slot{"is_valid_location": null}
    - slot{"email_body": "Vaishali in 1218/1, FC Road, Pune has been rated 4.6 with price for two as 500.\n\nHotel Shreyas in Survey 1242/B, Apte Road, Deccan Gymkhana, Pune has been rated 4.4 with price for two as 500.\n\nRam Krishna in Shop 6, Opposite Westend Theatre, Moledina Road, Camp Area, Pune has been rated 4.3 with price for two as 700.\n\nSambar Pure Veg in 1, Gera Emporia, Beside Phoenix East Court, Viman Nagar, Pune has been rated 4.3 with price for two as 300.\n\nRoopali Restaurant in 1227, Opposite British Library, FC Road, Pune has been rated 4.3 with price for two as 400.\n\nPriya in 245/46, MG Road, Pune has been rated 4.3 with price for two as 300.\n\nKerala Fast Food in Shop 1, Guru Teg Bahadur Co-operative Housing Society, Aundh Road, Haveli, Khadki, Pune has been rated 4.3 with price for two as 500.\n\nHotel Durga in Near Raj Motors, Rambaug Colony, Paud Road, Kothrud, Pune has been rated 4.3 with price for two as 300.\n\nDadu's Sweet Emporio in House 11, Survey 251, Moledina Road, East Street Camp, Camp Area, Pune has been rated 4.3 with price for two as 450.\n\nSatkar Rice Plate House in 1, Aditya Nakoda Enclave 1, Opposite Big Bazar, Sinhgad Road, Pune has been rated 4.2 with price for two as 700."}
    - utter_ask_for_result_email
* affirm
    - utter_ask_email
* send_email{"emailid": "ashwani.kumar04@gmaill.com"}
    - slot{"emailid": "ashwani.kumar04@gmaill.com"}
    - action_send_email
    - slot{"emailid": null}
    - slot{"email_body": null}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_validate_city
    - slot{"location": "hyderabad"}
    - slot{"is_valid_location": true}
    - utter_ask_cuisine
* notify{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"is_valid_cuisine": true}
    - utter_ask_price
* notify{"price": "500"}
    - slot{"price": "500"}
    - utter_ask_price
* goodbye{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_valid_cuisine": null}
    - slot{"is_valid_location": null}
    - slot{"email_body": "Subbayya Gari Hotel in MIG 295, Sri Devi Residency, Road 4, KPHB Colony, Kukatpally, Hyderabad has been rated 4.4 with price for two as 400.\n\nUdipi's Upahar in 2-21/4, Kannayalal Complex, Indira Nagar, Gachibowli, Hyderabad has been rated 4.4 with price for two as 500.\n\nSSP Kitchen & Dosa Station in Anupama Homes, Narsingi-Puppalaguda Main Road, Manikonda, Hyderabad has been rated 4.4 with price for two as 550.\n\nBikanervala in 6-3-190/2, Road 1, Banjara Hills, Hyderabad has been rated 4.3 with price for two as 700.\n\nHouse of Dosas in Opposite Lucid Diagnostics, Road 2, Banjara Hills, Hyderabad has been rated 4.3 with price for two as 300.\n\nAbhiruchi Hotel in Plot 19, Near Durgam Cheru Road, Kalyan Nagar, Madhapur, Hyderabad has been rated 4.3 with price for two as 700.\n\nTaj Mahal - Taj Mahal Hotel in 4-1-999, Abids Road, Abids, Hyderabad has been rated 4.3 with price for two as 700.\n\n5 Star Sambar in Shop 1, Cellar 1-29, Miyapur Road, Rajiv Gandhi Nagar, Gachibowli, Hyderabad has been rated 4.3 with price for two as 400.\n\nBurflet in Shop 634, 635, Plot 616, Sriram Nagar, Serilingampally, Kondapur, Hyderabad has been rated 4.3 with price for two as 400.\n\nKitchen house in Plot 354-B, Ragavendra Colony, Kondapur, Hyderabad has been rated 4.3 with price for two as 350."}
    - utter_ask_for_result_email
* affirm
    - utter_ask_email
* send_email{"emailid": "deepak.4ev@gmail.com"}
    - slot{"emailid": "deepak.4ev@gmail.com"}
    - action_send_email
    - slot{"emailid": null}
    - slot{"email_body": null}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "russian", "location": "Gokarna"}
    - slot{"cuisine": "russian"}
    - slot{"location": "Gokarna"}
    - action_validate_city
    - slot{"location": null}
    - slot{"is_valid_location": null}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* notify{"cuisine": "mexican", "location": "Asansol"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Asansol"}
    - action_validate_city
    - slot{"location": "asansol"}
    - slot{"is_valid_location": true}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - slot{"is_valid_cuisine": true}
    - utter_ask_price
* notify{"price": "expensive"}
    - slot{"price": "expensive"}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_valid_cuisine": null}
    - slot{"is_valid_location": null}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* notify{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_city
    - slot{"location": "mumbai"}
    - slot{"is_valid_location": true}
    - utter_ask_cuisine
* notify{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - slot{"is_valid_cuisine": true}
    - utter_ask_price
* notify{"price": "600-800"}
    - slot{"price": "600-800"}
    - utter_ask_price
* goodbye{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_valid_cuisine": null}
    - slot{"is_valid_location": null}
    - slot{"email_body": "Bombay To Barcelona Library Café in 778, Timmy Arcade, Makwana Road, Gamdevi, Marol, Mumbai has been rated 4.9 with price for two as 500.\n\nHearsch Bakery in 90/A, Next to Holy Family Hospital, Hill Road, Bandra West, Mumbai has been rated 4.7 with price for two as 400.\n\nThe Big Cloud Kitchen in Shop 20, Plot 182C, Punit Park, Cosmopolitan CHS, Sector 17, Nerul, Navi Mumbai has been rated 4.7 with price for two as 400.\n\nJimis Burger in 13-14, Pleasant Park, Off Link Road, Evershine Nagar, Opposite Movie Time Cinema, Malad West, Mumbai has been rated 4.5 with price for two as 700.\n\nJimis Burger in Shop B2, Shree Siddhivinayak Plaza, Off Link Road, Opposite Citi Mall, Andheri Lokhandwala, Andheri West, Mumbai has been rated 4.4 with price for two as 700.\n\nFrisbees in Shop 6, A39, Labaik House, Chimbai Road, Near St. Andrews Church, Hill Road, Bandra West has been rated 4.4 with price for two as 600.\n\nFooze in Shop 21, Block 3, Emerald Plaza, Hiranandani Meadows, GB Road, Vasant Vihar, Thane West, Thane has been rated 4.4 with price for two as 600.\n\nJimis Burger in Shop 25, Plot 20, Satra Plaza, Sector 19D, Palm Beach Road, Vashi, Navi Mumbai has been rated 4.4 with price for two as 700.\n\nCoffee By Di Bella in Shop 1, Carlton Court, Perry Road Junction, Pali Hill, Bandra West, Mumbai has been rated 4.4 with price for two as 650.\n\nDiet With Delight in Kurla Camp Road, Baba Namandas Nagar, Kailash Colony, Ulhasnagar, Mumbai has been rated 4.4 with price for two as 350."}
    - utter_ask_for_result_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Hydrabad"}
    - slot{"location": "Hydrabad"}
    - action_validate_city
    - slot{"location": null}
    - slot{"is_valid_location": null}
    - utter_ask_location
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_validate_city
    - slot{"location": "hyderabad"}
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
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_valid_cuisine": null}
    - slot{"is_valid_location": null}
    - slot{"email_body": "Conçu in Plot 738, Road 37, Jubilee Hills, Hyderabad has been rated 4.9 with price for two as 1000.\n\nChurrolto in Film Nagar Main Road, Opposite Indian Oil, Film Nagar, Hyderabad has been rated 4.9 with price for two as 1200.\n\nAB's - Absolute Barbecues in 8-2-618/10-11, Survey 129/70/283, 2nd Floor, Krishe Amethyst, Road 1, Banjara Hills, Hyderabad has been rated 4.7 with price for two as 1250.\n\nAB's - Absolute Barbecues in T-02, 3rd Floor, Inorbit Mall, Mind Space Road, Hitech City, Hyderabad has been rated 4.7 with price for two as 1250.\n\nBarbeque Pride in 790, Rangoli Building, Road 36, Jubilee Hills, Hyderabad has been rated 4.6 with price for two as 1200.\n\nSeasonal Tastes - The Westin in The Westin Mindspace, Survey 64, Building 15, K.Raheja IT Park, APIIC Software Layout, Hitech City, Hyderabad has been rated 4.6 with price for two as 3000.\n\nThe Roastery Coffee House in 8/2/287/12, House 418, Road 14, Banjara Hills, Hyderabad has been rated 4.5 with price for two as 800.\n\nCoffee Cup in E 89, 1st Floor, Near Canara Bank, Sainikpuri, Secunderabad has been rated 4.5 with price for two as 800.\n\nFlechazo in Sun Tower, 2nd Floor, above Axis Bank, Hitech , Madhapur, Hyderabad has been rated 4.5 with price for two as 1300.\n\nThe Glass Onion in Survey 236, Vattinagulappally Village, Rajendra Nagar Mandal, Gachibowli, Hyderabad has been rated 4.5 with price for two as 1200."}
    - utter_ask_for_result_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - utter_ask_cuisine
* notify{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"is_valid_cuisine": true}
    - utter_ask_price
* notify{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_valid_cuisine": null}
    - slot{"is_valid_location": null}
    - slot{"email_body": "Global Platters in M-37, Old DLF Colony, Sector 14, Gurgaon has been rated 4.7 with price for two as 500.\n\nPaddy's Den in U 50/1, Sector 24, Near Basement Market, DLF Phase 3, Gurgaon has been rated 4.7 with price for two as 400.\n\nRowls in Shahdara, New Delhi has been rated 4.6 with price for two as 400.\n\nC.I.A. Call It Asiian in 13 - 16, Narmada Shopping Complex, Near Don Bosco School, Alaknanda Road, Greater Kailash 2 (GK 2), New Delhi has been rated 4.5 with price for two as 700.\n\n4U in BH-01, Block C, Sector 71, Noida has been rated 4.5 with price for two as 400.\n\nBeijing Bowl in Rajouri Garden, New Delhi has been rated 4.5 with price for two as 400.\n\nMc Tadka - The Punjab Special in Sector 12, Gurgaon has been rated 4.5 with price for two as 300.\n\nChinese Crew in Sector 12, Gurgaon has been rated 4.5 with price for two as 300.\n\nMr. Gogo Chinese Food Point in 1625 A, Near Petrol Pump, Thane Road, Najafgarh, Delhi has been rated 4.5 with price for two as 350.\n\nBlue Moon Zayka in Jasola, New Delhi has been rated 4.5 with price for two as 400."}
    - utter_ask_for_result_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"location": "prayagraj"}
    - slot{"location": "prayagraj"}
    - action_validate_city
    - slot{"location": "prayagraj"}
    - slot{"is_valid_location": true}
    - utter_ask_cuisine
* notify{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - slot{"is_valid_cuisine": true}
    - utter_ask_price
* notify{"price": "expensive"}
    - slot{"price": "expensive"}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_valid_cuisine": null}
    - slot{"is_valid_location": null}
    - slot{"email_body": "Barbeque Nation in Fifth Floor, P Square Mall, MG Road, George Town, Allahabad has been rated 4.9 with price for two as 1200.\n\nSagar Ratna in 3/3, Hashimpur Road, Balson Crossing, Near Anand Bhawan, Tagore Town, Allahabad has been rated 4.5 with price for two as 800.\n\nOld School Cafe in 2nd Floor, 9-10 Tulsiani Grace, Civil Lines, Allahabad has been rated 4.5 with price for two as 1000.\n\nEl Chico Restaurant in 142A, 32, Mahatma Gandhi, Civil Lines, Allahabad has been rated 4.4 with price for two as 800.\n\nEDEN by Connoisseur in Hotel Samrat, Civil Lines, Allahabad has been rated 4.4 with price for two as 1000.\n\nPind Balluchi in 48/8, Stratchy Road, Civil Lines, Allahabad has been rated 4.4 with price for two as 1000.\n\nHotel Kanha Shyam in Allahabad HO, Civil Lines, Allahabad has been rated 4.1 with price for two as 900.\n\nKohinoor Restaurant in LG1 - LG2, Lower Ground Floor, Vinayak Tower, MG Marg, Civil Lines, Allahabad has been rated 4.1 with price for two as 800.\n\nMoti Mahal Delux in Second Floor, Vinayak City Center Mall, SP Marg, Civil Lines, Allahabad has been rated 4.0 with price for two as 850.\n\nJannat - Hotel Kanhashyam in 2nd Floor, South Road, Civil Lines, Allahabad has been rated 4.0 with price for two as 1300."}
    - utter_ask_for_result_email
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* notify{"location": "begaluraruad"}
    - slot{"location": "begaluraruad"}
    - action_validate_city
    - slot{"location": null}
    - slot{"is_valid_location": null}
    - utter_ask_location
* notify{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_city
    - slot{"location": "bangalore"}
    - slot{"is_valid_location": true}
    - utter_ask_cuisine
* notify{"cuisine": "chinease"}
    - slot{"cuisine": "chinease"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - slot{"is_valid_cuisine": null}
    - utter_ask_cuisine
* notify{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"is_valid_cuisine": true}
    - utter_ask_price
* notify{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_search_restaurants
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"price": null}
    - slot{"is_valid_cuisine": null}
    - slot{"is_valid_location": null}
    - slot{"email_body": "Meghana Foods in 57/1, 1st Floor, Jayalaxmi Chambers, Next to Old Galaxy Theatre, Residency Road, Bangalore has been rated 4.5 with price for two as 600.\n\nHyderabad Biryaani House in 7/1, Victoria Road, Richmond Town Area, Richmond Town, Bangalore has been rated 4.5 with price for two as 600.\n\nRoyal Andhra Spice in OSR Hotels, 60 Feet Road, Near BEML Bus Depot, Rajarajeshwari Nagar, Bangalore has been rated 4.5 with price for two as 650.\n\nDorothy's Kitchen in Beside Lakshmi Narasimha Temple, Bommanahalli, Bangalore has been rated 4.5 with price for two as 450.\n\nPeoples Choice Food And Beverage in 3, B Narayanpura, 1st Main, Behind HP Campus, Whitefield Main Road, Whitefield, Bangalore has been rated 4.5 with price for two as 400.\n\nShivaji Military Hotel in 718, 1st C Main, 45th Cross, 8th Block, Jayanagar, Bangalore has been rated 4.4 with price for two as 450.\n\nLeon Grill in 1671, 9th Main, 4th Cross, HAL 3rd Stage, Jeevan Bhima Nagar, Bangalore has been rated 4.4 with price for two as 650.\n\nKhawa Karpo in 50/1,  Near Jyothi Nivas College, Koramangala 5th Block, Bangalore has been rated 4.4 with price for two as 350.\n\nGreen Onion in 43 - 44, Chandraprabha Complex, Residency Road, Bangalore has been rated 4.4 with price for two as 600.\n\nEAT - East Asian Treats in 47/7, 1st Floor, Nanjunda Reddy Complex, Doddathogur, Near Velankani Gate 2, Electronic City, Bangalore has been rated 4.4 with price for two as 550."}
    - utter_ask_for_result_email
* affirm
    - utter_ask_email
* send_email{"emailid": "ashwani.kumar.04@gmail.com"}
    - slot{"emailid": "ashwani.kumar.04@gmail.com"}
    - action_validate_email
    - slot{"emailid": "ashwani.kumar.04@gmail.com"}
    - action_send_email
    - slot{"emailid": null}
    - slot{"email_body": null}
    - utter_goodbye
    - action_restart

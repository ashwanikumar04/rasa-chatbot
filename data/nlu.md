## intent:greet
- hi
- hey
- hello
- howdy
- hey there
- good morning
- good afternoon
- good evening
- hola
- what's up
- Hello
- hi there

## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thank you
- thanks
- of course
- that sounds good
- yea
- sounds correct
- yea, please do
- yep, send

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- bye bye
- have a good one
- see you around
- see you later
- see you
- see ya
- [moderate](price)

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really
- nope
- not interested
- not at all

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab something to eat
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- i am looking for an [indian](cuisine) spot called tadka
- search for restaurants
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- please help me to find restaurants in [pune](location)
- Please find me a restaurant in [bengaluru](location)
- [mumbai](location)
- show me restaurants
- can you book a table in [Aligarh](location) in a [moderate](price) price range with [Indian](cuisine) food for [2](people) people
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- show me [chinese](cuisine) restaurants in [Delhi](location) in [moderate](price) price range
- find me some restaurants in [Pune](location)
- [mexican](cuisine)
- find me food in [Noida](location)
- [biriyani]{"entity": "cuisine", "value": "south indian"}
- under my [budget]{"entity": "price", "value": "moderate"}
- show me restaurants with [medium price]{"entity": "price", "value": "moderate"} range in [baroda](location)
- south [indian](cuisine)
- I'm hungry. Looking for some good restaurants
- [Mexican](cuisine)
- [American](cuisine)
- find me a restaurant
- [chennai](location)
- [bengaluru](location)
- somethink like [biriyani]{"entity": "cuisine", "value": "south indian"}
- Im hungry. Looking out for some good restaurants
- show me some [italian](cuisine) cusine restaurants
- [high budget]{"entity": "price", "value": "expensive"} restaurants
- [higher budget]{"entity": "price", "value": "expensive"} restaurants
- [medium cost]{"entity": "price", "value": "moderate"} restaurants
- [average]{"entity": "price", "value": "moderate"} restaurants
- [mid level]{"entity": "price", "value": "moderate"} restaurants
- in the range of [300 to 700]{"entity": "price", "value": "moderate"}
- I’m hungry. Looking out for some good restaurants
- looking for a restaurant in [bhilwara](location)
- looking for restaurants in [Vijayawada](location)
- looking for [North Indian](cuisine) cuisine in [Ujjain](location)
- find out [american](cuisine) cuisine in [mumbai](location)
- search for [Mexican](cuisine) cuisine in [mumbai](location)
- looking for [Italian](cuisine) restaurant in [Varanasi](location)
- [Lesser than Rs. 300]{"entity": "price", "value": "economic"}
- [lesser than Rs. 300]{"entity": "price", "value": "economic"}
- [less than 300]{"entity": "price", "value": "economic"}
- [max 300]{"entity": "price", "value": "economic"}
- [cheap]{"entity": "price", "value": "economic"} restaurants
- [cheap]{"entity": "price", "value": "economic"} punjabi(cuisine) restaurants
- [inexpensive]{"entity": "price", "value": "economic"} restaurants
- [lower than 300]{"entity": "price", "value": "economic"}
- [lower cost]{"entity": "price", "value": "economic"} restaurants
- [economical]{"entity": "price", "value": "economic"} restaurants
- [low budget]{"entity": "price", "value": "economic"} restaurants
- looking for [North Indian](cuisine) restaurants in [Delhi](location) in [moderate](price) price range
- get me [expensive](price) [North Indian](cuisine) restaurants in [Hyderabad](location)
- get me [best]{"entity": "price", "value": "expensive"} restaurants for a [couple]{"entity": "people", "value": "2"}
- [Asansol](location)
- in [Bhopal](location)
- any where in [Coimbatore](location)
- [good ambience]{"entity": "price", "value": "expensive"} restaurant in [gaya](location)
- [gaya](location)
- Looking for restaurants in [mumbai](location)
- show me some [chinese](cuisine) restaurants in [delhi](location)
- [expensive](price)
- get me some [expensive](price) restaurants in [american](cuisine) style in [pune](location)
- I am looking for some [cheap]{"entity": "price", "value": "economic"} restaurants in [chennai](location)
- looking for [french](cuisine) cuisine in [mumbai](location)
- Can you please suggest the [beach side]{"entity": "price", "value": "expensive"} restaurants in [Chennai](location)
- [Mexican](cuisine)

## intent:send_email
- kindly send email to [xyz@gmail.com](emailid)
- you can send email to [xyz@gmail.com](emailid)
- here it is [xyz@domain.com](emailid)
- sure, here it is [xyz@domain.com](emailid)
- thanks please send email to [xyx@gmail.com](emailid)
- could you please send it to [xyx@gmail.com](emailid)
- [xy@sth.edu](emailid)
- [xy@dkj.com](emailid)
- [xy@dkdl.co.in](emailid)
- yes. Please send it to [abc@domain.com](emailid)
- please send the email to [xyx@gmail.com](emailid)
- my id is [xyz@gmail.com](emailid)
- my email is [xyz@domain.com](emailid)
- my emailid is [deepak4ev@gmail.com](emailid)
- emailId is [deepak4ev@gmail.com](emailid)
- email is [deepak4ev@gmail.com](emailid)
- [deepak4ev@gmail.com](emailid)

## synonym:2
- couple
- two

## synonym:Chennai
- Madras
- Chennaii

## synonym:Delhi
- New Delhi
- Nayi delhi
- nayi dilli
- Dilli
- NDLS

## synonym:Kolkata
- Kolkatta
- calcutta

## synonym:Thiruvananthapuram
- Trivandrum

## synonym:Vijayawada
- Bezawada

## synonym:Visakhapatnam
- Vizag
- Visakha

## synonym:bangalore
- bengaluru
- bglr
- banglore
- blr

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:economic
- Lesser than Rs. 300
- lesser than Rs. 300
- less than 300
- max 300
- cheap
- inexpensive
- lower than 300
- lower cost
- economical
- low budget
- lesser than 300
- <300
- cheaper
- low cost
- lower budget

## synonym:expensive
- high budget
- higher budget
- best
- good ambience
- more than Rs. 700
- more than 700
- min 700
- expensive
- higher than 700
- >700
- high end
- lavish
- roof top
- beach side

## synonym:moderate
- budget
- medium price
- medium cost
- average
- mid level
- 300 to 700
- Rs. 300 to 700
- mid
- mid range
- 300-700
- moderate

## synonym:mumbai
- Mumbaii
- bambai
- Bombay

## synonym:north indian
- northies
- punjabi
- gujrati
- rajasthani

## synonym:south indian
- biriyani
- southies
- spicy
- biryani

## synonym:vegetarian
- veggie
- vegg
- vegan
- jain restaurant

## regex:email
- (\w+[.|\w])*@(\w+[.])*\w+

## regex:greet
- hey[^\s]*
- hi[^\s]*

## lookup:cuisine
  data/cuisine.txt

## lookup:location
  data/cities.txt
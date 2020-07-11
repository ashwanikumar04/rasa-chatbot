import zomatopy

cuisines_dict = {'maxican': 73, 'chinese': 25, 'american': 1,
                 'italian': 55,  'north indian': 50, 'south indian': 85}

price_dict = {'economic': (0, 299), 'moderate': (
    300, 700), 'expensive': (701, 9999)}

config = {"user_key": "50aadfe48ced3c06244a29a7381ac7eb"}

zomato = zomatopy.initialize_app(config)

def test_api(loc, cuisine, price):
    restaurant_list = zomato.getTopRestaurants(
        loc, str(cuisines_dict.get(cuisine)), price_dict[price])
    for restaurant in restaurant_list:
        print('{0} in {1} has been rated {2} with price for two as {3}.'.format(
            restaurant['name'], restaurant['address'], restaurant['rating'], restaurant["average_cost_for_two"]))

print("Printing economic")
test_api('delhi', 'chinese', 'economic')
print("______________________")

print("Printing moderate")

test_api('delhi', 'chinese', 'moderate')
print("______________________")

print("Printing expensive")
test_api('delhi', 'chinese', 'expensive')

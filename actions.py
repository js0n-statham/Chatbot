from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json


class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config = { "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		# operable_areas = ['Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Ahmedabad', 'Pune', 'Kochi', 'Agra', 'Ajmer', 'Aligarh', 'Amravati', 'Amritsar', 'Asansol', 'Aurangabad', 'Bareilly', 'Belgaum', 'Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bilaspur', 'Bokaro Steel City', 'Chandigarh', 'Coimbatore Nagpur', 'Cuttack', 'Dehradun', 'Dhanbad', 'Bhilai', 'Durgapur', 'Erode', 'Faridabad', 'Firozabad', 'Ghaziabad', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Gwalior', 'Gurgaon', 'Guwahati', 'Hamirpur', 'Hubli–Dharwad', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar', 'Jammu', 'Jamnagar', 'Jamshedpur', 'Jhansi', 'Jodhpur', 'Kakinada', 'Kannur', 'Kanpur', 'Kottayam', 'Kolhapur', 'Kollam', 'Kozhikode', 'Kurnool', 'Ludhiana', 'Lucknow', 'Madurai', 'Malappuram', 'Mathura', 'Goa', 'Mangalore', 'Meerut', 'Moradabad', 'Mysore', 'Nanded', 'Nashik', 'Nellore', 'Noida', 'Palakkad', 'Patna', 'Perinthalmanna', 'Pondicherry', 'Purulia Prayagraj', 'Raipur', 'Rajkot', 'Rajahmundry', 'Ranchi', 'Rourkela', 'Salem', 'Sangli', 'Shimla', 'Siliguri', 'Solapur', 'Srinagar', 'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli', 'Tirur', 'Tirupati', 'Tirunelveli', 'Tiruppur', 'Tiruvannamalai', 'Ujjain', 'Bijapur', 'Vadodara', 'Varanasi', 'Vasai-Virar City', 'Vijayawada', 'Vellore', 'Warangal', 'Surat', 'Visakhapatnam']
		# if loc not in operable_areas:
		# 	dispatcher.utter_message("We do not operate in that area yet.")
		# else:
		cuisine = tracker.get_slot('cuisine')
		location_detail = zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat = d1["location_suggestions"][0]["latitude"]
		lon = d1["location_suggestions"][0]["longitude"]
		cuisines_dict = {'american': 1, 'chinese': 25, 'mexican': 73, 'italian': 55, 'north indian': 50, 'south indian': 85}
		results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 100)
		d = json.loads(results)
		
		global result_10
		result_10 = ""
		response = ""
		if d['results_found'] == 0:
			response = "no results"
			result_10 = "no results"
		else:
			price = tracker.get_slot('price')
			min_price = 0
			max_price= 9999999
			if price == 'LessThan300':
				max_price = 299
			elif price =='300to700':
				min_price = 300
				max_price = 700
			else:
				min_price = 701
				
			def sort_by_rating(restaurant):			
				return restaurant['restaurant']['user_rating']['aggregate_rating']
				
			counter = 0
			for restaurant in sorted(d['restaurants'], key = sort_by_rating, reverse = True):
				avg_c_2 = restaurant['restaurant']['average_cost_for_two']
				if avg_c_2>=min_price and avg_c_2<=max_price:
					counter = counter + 1
					if counter <= 5:
						response = response + "\n" + str(counter) + ". " + restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated "+str(restaurant['restaurant']['user_rating']['aggregate_rating'])	
						result_10 = result_10 + str(counter) + ". " + restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated "+str(restaurant['restaurant']['user_rating']['aggregate_rating'])+"\n"	
					elif counter > 5 and counter <= 10:
						result_10 = result_10 + str(counter) + ". " + restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated "+str(restaurant['restaurant']['user_rating']['aggregate_rating'])+"\n"	
			if response	== "":
				response = "no results"
				result_10 = "no results"
			else :
				response = 'Showing you top rated restaurants:' + response
		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]

		
		
		
		
# Send email the list of 10 restaurants
class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		email = tracker.get_slot('email')
		
	
		import smtplib 
		from email.mime.text import MIMEText as text
		
		s = smtplib.SMTP('smtp.gmail.com', 587) 
		s.starttls() 
		s.login("youremailid@yourmail.com", "yourpassword")
		message = "The details of all the restaurants you inquried \n \n"
		global result_10
		message = message + result_10
		email_struct=text(message)
		email_struct['Subject'] = 'Restaurant Search Results'
		email_struct['From'] = 'youremailid@yourmail.com'
		email_struct['To'] = str(email)
		
		try:
			s.send_message(email_struct)
			s.quit()
		except:
			dispatcher.utter_message(email)

		result_10 = ""
		return [SlotSet('email',email)]


# Action to check if the cities entered are valid tier1 or tier 2 cities

class ActionCheckCity(Action):
	def name(self):
		return 'action_check_city'

	def run(self, dispatcher, tracker, domain):
		operable_areas = ['Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Ahmedabad', 'Pune', 'Kochi', 'Agra', 'Ajmer', 'Aligarh', 'Amravati', 'Amritsar', 'Asansol', 'Aurangabad', 'Bareilly', 'Belgaum', 'Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bilaspur', 'Bokaro Steel City', 'Chandigarh', 'Coimbatore Nagpur', 'Cuttack', 'Dehradun', 'Dhanbad', 'Bhilai', 'Durgapur', 'Erode', 'Faridabad', 'Firozabad', 'Ghaziabad', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Gwalior', 'Gurgaon', 'Guwahati', 'Hamirpur', 'Hubli–Dharwad', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar', 'Jammu', 'Jamnagar', 'Jamshedpur', 'Jhansi', 'Jodhpur', 'Kakinada', 'Kannur', 'Kanpur', 'Kottayam', 'Kolhapur', 'Kollam', 'Kozhikode', 'Kurnool', 'Ludhiana', 'Lucknow', 'Madurai', 'Malappuram', 'Mathura', 'Goa', 'Mangalore', 'Meerut', 'Moradabad', 'Mysore', 'Nanded', 'Nashik', 'Nellore', 'Noida', 'Palakkad', 'Patna', 'Perinthalmanna', 'Pondicherry', 'Purulia Prayagraj', 'Raipur', 'Rajkot', 'Rajahmundry', 'Ranchi', 'Rourkela', 'Salem', 'Sangli', 'Shimla', 'Siliguri', 'Solapur', 'Srinagar', 'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli', 'Tirur', 'Tirupati', 'Tirunelveli', 'Tiruppur', 'Tiruvannamalai', 'Ujjain', 'Bijapur', 'Vadodara', 'Varanasi', 'Vasai-Virar City', 'Vijayawada', 'Vellore', 'Warangal', 'Surat', 'Visakhapatnam']
		operable_areas_lower = [city.lower() for city in operable_areas]
		loc = tracker.get_slot('location')
		if loc.lower() in operable_areas_lower:
			if tracker.get_slot('cuisine') is None:
				dispatcher.utter_message(template = 'utter_ask_cuisine')
			else :
				dispatcher.utter_message(template = 'utter_ask_price_range')
			return [SlotSet('location', loc)]
		else:
			dispatcher.utter_message(template = 'utter_ask_location_again')
			return [SlotSet('location', None)]

			






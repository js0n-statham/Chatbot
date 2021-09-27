## complete path 1.1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_city
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price_range
* restaurant_search{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_email
* send_email
    - utter_enquire_mail_id
* send_email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_send_email
    - utter_sent_email
    - action_restart

## complete path 1.2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mangalore"}
    - slot{"location": "Mangalore"}
    - action_check_city
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price_range
* restaurant_search{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "Mangalore"}
    - utter_ask_email
* send_email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_send_email
    - slot{"email": "ahbcdj@dkj.com"}
    - utter_sent_email
    - action_restart

## complete path 1.3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_city
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price_range
* restaurant_search{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - utter_ask_email
* dont_send_email
    - utter_bon_appetit
    - action_restart

## complete path 2.1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bengaluru"}
    - slot{"location": "Bengaluru"}
    - action_check_city
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "American"}
    - utter_ask_price_range
* restaurant_search{"price": "LessThan300"}
    - slot{"price": "LessThan300"}
    - action_search_restaurants
    - slot{"location": "Bengaluru"}
    - utter_ask_email
* send_email
    - utter_enquire_mail_id
* send_email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_send_email
    - utter_sent_email
    - action_restart

## complete path 2.2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Ahmedabad"}
    - slot{"location": "Ahmedabad"}
    - action_check_city
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price_range
* restaurant_search{"price": "LessThan300"}
    - slot{"price": "LessThan300"}
    - action_search_restaurants
    - slot{"location": "Ahmedabad"}
    - utter_ask_email
* send_email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_send_email
    - slot{"email": "ahbcdj@dkj.com"}
    - utter_sent_email
    - action_restart

## complete path 2.3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_city
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price_range
* restaurant_search{"price": "LessThan300"}
    - slot{"price": "LessThan300"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - utter_ask_email
* dont_send_email
    - utter_bon_appetit
    - action_restart

## complete path 3.1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_city
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price_range
* restaurant_search{"price": "MoreThan700"}
    - slot{"price": "MoreThan700"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email
* send_email
    - utter_enquire_mail_id
* send_email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_send_email
    - utter_sent_email
    - action_restart

## complete path 3.2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kochi"}
    - slot{"location": "Kochi"}
    - action_check_city
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price_range
* restaurant_search{"price": "MoreThan700"}
    - slot{"price": "MoreThan700"}
    - action_search_restaurants
    - slot{"location": "Kochi"}
    - utter_ask_email
* send_email{"email": "ahbcdj@dkj.com"}
    - slot{"email": "ahbcdj@dkj.com"}
    - action_send_email
    - slot{"email": "ahbcdj@dkj.com"}
    - utter_sent_email
    - action_restart

## complete path 3.3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Coimbatore"}
    - slot{"location": "Coimbatore"}
    - action_check_city
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price_range
* restaurant_search{"price": "MoreThan700"}
    - slot{"price": "MoreThan700"}
    - action_search_restaurants
    - slot{"location": "Coimbatore"}
    - utter_ask_email
* dont_send_email
    - utter_bon_appetit
    - action_restart


## location specified 1
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_city
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price_range
* restaurant_search{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_email
* send_email
    - utter_enquire_mail_id
* send_email{"email": "abcdefgh123456@pqr123.com"}
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - action_send_email
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - utter_sent_email
    - action_restart

## location specified 2
* greet
    - utter_greet
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_check_city
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price": "MoreThan700"}
    - slot{"price": "MoreThan700"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_ask_email
* send_email{"email": "abcdefgh123456@pqr123.com"}
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - action_send_email
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - utter_sent_email
    - action_restart


## location specified 3
* greet
    - utter_greet
* restaurant_search{"location": "Belgaum"}
    - slot{"location": "Belgaum"}
    - action_check_city
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price_range
* restaurant_search{"price": "LessThan300"}
    - slot{"price": "LessThan300"}
    - action_search_restaurants
    - slot{"location": "Belgaum"}
    - utter_ask_email
* dont_send_email
    - utter_bon_appetit
    - action_restart


 ## all intents specified 1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Kanpur"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Kanpur"}
    - action_check_city
* restaurant_search{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "Kanpur"}
    - utter_ask_email
* send_email
    - utter_enquire_mail_id
* send_email{"email": "abcdefgh123456@pqr123.com"}
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - action_send_email
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - utter_sent_email
    - action_restart
 
## all intents specified 2
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "Lucknow"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Lucknow"}
    - action_check_city
* restaurant_search{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "Lucknow"}
    - utter_ask_email
* send_email{"email": "abcdefgh123456@pqr123.com"}
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - action_send_email
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - utter_sent_email
    - action_restart

## all intents specified 3
* greet
    - utter_greet
* restaurant_search{"cuisine": "South Indian", "location": "Malappuram"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "Malappuram"}
    - action_check_city
* restaurant_search{"price": "LessThan300"}
    - slot{"price": "LessThan300"}
    - action_search_restaurants
    - slot{"location": "Malappuram"}
    - utter_ask_email
* dont_send_email
    - utter_bon_appetit
    - action_restart


## cuisine specified 1
* greet
    - utter_greet
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_location
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_check_city
* restaurant_search{"price": "MoreThan700"}
    - slot{"price": "MoreThan700"}
    - action_search_restaurants
    - slot{"location": "Patna"}
    - utter_ask_email
* send_email
    - utter_enquire_mail_id
* send_email{"email": "abcdefgh123456@pqr123.com"}
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - action_send_email
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - utter_sent_email
    - action_restart

 
## cuisine specified 2
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_location
* restaurant_search{"location": "Salem"}
    - slot{"location": "Salem"}
    - action_check_city
* restaurant_search{"price": "300to700"}
    - slot{"price": "MoreThan700"}
    - action_search_restaurants
    - slot{"location": "Salem"}
    - utter_ask_email
* send_email{"email": "abcdefgh123456@pqr123.com"}
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - action_send_email
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - utter_sent_email
    - action_restart

## cuisine specified 3
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_location
* restaurant_search{"location": "Shimla"}
    - slot{"location": "Shimla"}
    - action_check_city
* restaurant_search{"price": "LessThan300"}
    - slot{"price": "LessThan300"}
    - action_search_restaurants
    - slot{"location": "Shimla"}
    - utter_ask_email
* dont_send_email
    - utter_bon_appetit
    - action_restart

<!-- Below are some stories trained using RASA Interactive -->

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_city
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price_range
* restaurant_search{"price": "MoreThan700"}
    - slot{"price": "MoreThan700"}
    - action_search_restaurants
    - utter_ask_email
* send_email
    - utter_enquire_mail_id
* send_email{"email": "abcdefgh123456@pqr123.com"}
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - action_send_email
    - utter_sent_email
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_city
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price_range
* restaurant_search{"price": "LessThan300"}
    - slot{"price": "LessThan300"}
    - action_search_restaurants
    - utter_ask_email
* dont_send_email
    - utter_bon_appetit
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mangalore"}
    - slot{"location": "Mangalore"}
    - action_check_city
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price_range
* restaurant_search{"price": "LessThan300"}
    - slot{"price": "LessThan300"}
    - action_search_restaurants
    - utter_ask_email
* send_email{"email": "abcdefgh123456@pqr123.com"}
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - action_send_email
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - utter_sent_email
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - action_check_city
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price_range
* restaurant_search{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "Amritsar"}
    - utter_ask_email
* send_email
    - utter_enquire_mail_id
* send_email{"email": "abcdefgh123456@pqr123.com"}
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - action_send_email
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - utter_sent_email
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_city
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price_range
* restaurant_search{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_email
* send_email
    - utter_enquire_mail_id
* send_email{"email": "abcdefgh123456@pqr123.com"}
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - action_send_email
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - utter_sent_email
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "Bhopal"}
    - slot{"location": "Bhopal"}
    - action_check_city
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price": "MoreThan700"}
    - slot{"price": "MoreThan700"}
    - action_search_restaurants
    - slot{"location": "Bhopal"}
    - utter_ask_email
* send_email{"email": "abcdefgh123456@pqr123.com"}
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - action_send_email
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - utter_sent_email
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Agra"}
    - slot{"location": "Agra"}
    - action_check_city
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price_range
* restaurant_search{"price": "LessThan300"}
    - slot{"price": "LessThan300"}
    - action_search_restaurants
    - slot{"location": "Agra"}
    - utter_ask_email
* dont_send_email
    - utter_bon_appetit
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Chandigarh"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Chandigarh"}
    - action_check_city
* restaurant_search{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "Chandigarh"}
    - utter_ask_email
* send_email
    - utter_enquire_mail_id
* send_email{"email": "abcdefgh123456@pqr123.com"}
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - action_send_email
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - utter_sent_email
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "Kozhikode"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Kozhikode"}
    - action_check_city
* restaurant_search{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "Kozhikode"}
    - utter_ask_email
* send_email{"email": "abcdefgh123456@pqr123.com"}
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - action_send_email
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - utter_sent_email
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "South Indian", "location": "Madurai"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "Madurai"}
    - action_check_city
* restaurant_search{"price": "LessThan300"}
    - slot{"price": "LessThan300"}
    - action_search_restaurants
    - slot{"location": "Madurai"}
    - utter_ask_email
* dont_send_email
    - utter_bon_appetit
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_location
* restaurant_search{"location": "Noida"}
    - slot{"location": "Noida"}
    - action_check_city
* restaurant_search{"price": "MoreThan700"}
    - slot{"price": "MoreThan700"}
    - action_search_restaurants
    - slot{"location": "Noida"}
    - utter_ask_email
* send_email
    - utter_enquire_mail_id
* send_email{"email": "abcdefgh123456@pqr123.com"}
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - action_send_email
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - utter_sent_email
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_location
* restaurant_search{"location": "Pondicherry"}
    - slot{"location": "Pondicherry"}
    - action_check_city
* restaurant_search{"price": "MoreThan700"}
    - slot{"price": "MoreThan700"}
    - action_search_restaurants
    - slot{"location": "Pondicherry"}
    - utter_ask_email
* send_email{"email": "abcdefgh123456@pqr123.com"}
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - action_send_email
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - utter_sent_email
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_location
* restaurant_search{"location": "Rajkot"}
    - slot{"location": "Rajkot"}
    - action_check_city
* restaurant_search{"price": "LessThan300"}
    - slot{"price": "LessThan300"}
    - action_search_restaurants
    - slot{"location": "Rajkot"}
    - utter_ask_email
* dont_send_email
    - utter_bon_appetit
    - action_restart


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_location
* restaurant_search{"location": "Vijayawada"}
    - slot{"location": "Vijayawada"}
    - action_check_city
* restaurant_search{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "Vijayawada"}
    - utter_ask_email
* send_email{"email": "abcdefgh123456@pqr123.com"}
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - action_send_email
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - utter_sent_email
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_city
    - slot{"location": "Delhi"}
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_email
* dont_send_email
    - utter_bon_appetit
    - action_restart

<!-- Interactive stories for incorrect city/location -->

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_city
    - slot{"location": null}
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - action_check_city
    - slot{"location": null}
* restaurant_search{"location": "Ahmedabad"}
    - slot{"location": "Ahmedabad"}
    - action_check_city
    - slot{"location": "Ahmedabad"}
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price_range
* restaurant_search{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "Ahmedabad"}
    - utter_ask_email
* send_email{"email": "abcdefgh123456@pqr123.com"}
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - action_send_email
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - utter_sent_email
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_city
    - slot{"location": "bangalore"}
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price_range
* restaurant_search{"price": "MoreThan700"}
    - slot{"price": "MoreThan700"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_email
* dont_send_email
    - utter_bon_appetit
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "mysore"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "mysore"}
    - action_check_city
    - slot{"location": "mysore"}
* restaurant_search{"price": "MoreThan700"}
    - slot{"price": "MoreThan700"}
    - action_search_restaurants
    - slot{"location": "mysore"}
    - utter_ask_email
* send_email
    - utter_enquire_mail_id
* send_email{"email": "abcdefgh123456@pqr123.com"}
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - action_send_email
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - utter_sent_email
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_city
    - slot{"location": "Bangalore"}
* restaurant_search{"price": "LessThan300"}
    - slot{"price": "LessThan300"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_ask_email
* dont_send_email
    - utter_bon_appetit
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Raichur"}
    - slot{"location": "Raichur"}
    - action_check_city
    - slot{"location": null}
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_city
    - slot{"location": "Bangalore"}
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price_range
* restaurant_search{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_ask_email
* send_email{"email": "abcdefgh123456@pqr123.com"}
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - action_send_email
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - utter_sent_email
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "kolar"}
    - slot{"location": "kolar"}
    - action_check_city
    - slot{"location": null}
* restaurant_search{"location": "mysore"}
    - slot{"location": "mysore"}
    - action_check_city
    - slot{"location": "mysore"}
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price_range
* restaurant_search{"price": "MoreThan700"}
    - slot{"price": "MoreThan700"}
    - action_search_restaurants
    - slot{"location": "mysore"}
    - utter_ask_email
* send_email
    - utter_enquire_mail_id
* send_email{"email": "abcdefgh123456@pqr123.com"}
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - action_send_email
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - utter_sent_email
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "Ladakh"}
    - slot{"cuisine": "american"}
    - slot{"location": "Ladakh"}
    - action_check_city
    - slot{"location": null}
* restaurant_search{"location": "srinagar"}
    - slot{"location": "srinagar"}
    - action_check_city
    - slot{"location": "srinagar"}
* restaurant_search{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "srinagar"}
    - utter_ask_email
* dont_send_email
    - utter_bon_appetit
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "Hunsur"}
    - slot{"location": "Hunsur"}
    - action_check_city
    - slot{"location": null}
* restaurant_search{"location": "mysore"}
    - slot{"location": "mysore"}
    - action_check_city
    - slot{"location": "mysore"}
* restaurant_search{"price": "300to700"}
    - slot{"price": "300to700"}
    - action_search_restaurants
    - slot{"location": "mysore"}
    - utter_ask_email
* send_email{"email": "abcdefgh123456@pqr123.com"}
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - action_send_email
    - slot{"email": "abcdefgh123456@pqr123.com"}
    - utter_sent_email
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Kozhikode"}
    - slot{"location": "Kozhikode"}
    - action_check_city
    - slot{"location": "Kozhikode"}
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price_range
* restaurant_search{"price": "MoreThan700"}
    - slot{"price": "MoreThan700"}
    - action_search_restaurants
    - utter_ask_email
* dont_send_email
    - utter_bon_appetit
    - action_restart

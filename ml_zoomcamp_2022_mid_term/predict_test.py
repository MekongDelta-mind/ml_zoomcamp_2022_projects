#!/usr/bin/env python
# coding: utf-8


import requests



# to test the model is loaded and working properly or not
customer_id = 'pkn_2022'
customer = {'age': '26-39',
  'gender': 'male',
  'driving_experience': '0-9y',
  'education': 'none',
  'income': 'middle_class',
  'vehicle_ownership': 1.0,
  'married': 1.0,
  'children': 0.0,
  'postal_code': 10238,
  'speeding_violations': 2,
  'duis': 0,
  'past_accidents': 0,
  'vehicle_year': 'after_2015',
  'type_of_vehicle': 'sports_car',
  'id': 18647,
  'credit_score': 0.7179927843792123,
  'annual_mileage': 9000.0}



url = 'http://localhost:9696/predict'


response = requests.post(url, json=customer).json()
print(response)


if response['accept_or_reject']=='Yes':
    print(f' the customer with customer_id: {customer_id} is accepted for the insurance claims')
else:
    print(f'Sorry :( , the customer with customer_id: {customer_id} is rejected for the insurance claims')

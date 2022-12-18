#!/usr/bin/env python
# coding: utf-8


import requests

bidding = {'Auction_ID': 2185,
  'Bidder_Tendency': 0.045454545,
  'Bidding_Ratio': 0.025641026,
  'Successive_Outbidding': 0.0,
  'Last_Bidding': 0.0040856481,
  'Auction_Bids': 0.538461538,
  'Starting_Price_Average': 0.99935281,
  'Early_Bidding': 0.0040856481,
  'Winning_Ratio': 0.0,
  'Auction_Duration': 5}

auction_Id = bidding['Auction_ID']
bidder_ID = 'm***t' # from the dataset at df_train.iloc[1534]


url = 'http://localhost:9696/predict'


response = requests.post(url, json=bidding).json()
print(f'Response from the service for the given test data point : {response}')



if response['fraud_or_not']=='Yes':
    print(f' The bidding with the auciton_id: {auction_Id} and bidding_id: {bidder_ID} is a fraud bidding and should be discarded ')
else:
    print(f'The bidding with the auciton_id: {auction_Id} and bidding_id: {bidder_ID} is fair bidding. Thanks for behaving !!!')






import pickle

from flask import Flask
from flask import request
from flask import jsonify


input_file = 'model_C=1.bin'

with open(input_file, 'rb') as f_in: 
    dv, model = pickle.load(f_in)

# print(f'Loaded model is {model}')

# test_bidding = {'Auction_ID': 2185,
#   'Bidder_Tendency': 0.045454545,
#   'Bidding_Ratio': 0.025641026,
#   'Successive_Outbidding': 0.0,
#   'Last_Bidding': 0.0040856481,
#   'Auction_Bids': 0.538461538,
#   'Starting_Price_Average': 0.99935281,
#   'Early_Bidding': 0.0040856481,
#   'Winning_Ratio': 0.0,
#   'Auction_Duration': 5}

def predict():
    bidding = request.

X = dv.transform([test_bidding])


y_pred = model.predict_proba(X)[0, 1]


print('input:', test_bidding)
print('output:', y_pred)
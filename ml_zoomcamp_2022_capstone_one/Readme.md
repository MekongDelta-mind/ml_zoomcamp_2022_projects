# ML Zoomcamp 2022

## Description of the problem

 

Source: [Shill Bidding Dataset](https://archive.ics.uci.edu/ml/datasets/Shill+Bidding+Dataset)

## Repo Contents
        
- Data
    - Source: [Shill Bidding Dataset](https://archive.ics.uci.edu/ml/datasets/Shill+Bidding+Dataset)
        - scraped a large number of eBay auctions of a popular product. After preprocessing the auction data, the the SB dataset.
- Files
    - **`bidding_notebook.ipynb` -**
        - Data preparation and data cleaning
        - EDA, feature importance analysis
        - Model selection process and parameter tuning
        - NOTE: All the inferences found are in the notebook.
    - `train.py`
        - Training the final model
        - Saving it to a file (e.g. pickle) or saving it with specialized software (BentoML)
    - `predict.py`
        - Loading the model
        - Serving it via a web service (with Flask or specialized software - BentoML, KServe, etc)
    - **`predict_test.ipynb`**
        - notebook to test the flask app created in the above file
    - **`predict_test.py`**
        - converting the predict_test.ipynb to python script so to test the app directly from the cli instead of running the notebook repeatedly.
    - `Pipenv` and `Pipenv.lock`
    - `Dockerfile`

## Description of the problem

### Details about the project

The data is scraped for a large number of eBay auctions of a popular product. After preprocessing the auction data, the the SB dataset. Based on teh features we decide if the bidding is fraud or not. It is a binary classification problem.

- Data Dictionary
    - `Record ID`: Unique identifier of a record in the dataset.
    - `Auction ID`: Unique identifier of an auction.
    - `Bidder ID`: Unique identifier of a bidder.
    - `Bidder Tendency`: A shill bidder participates exclusively in auctions of few sellers rather than a diversified lot. This is a collusive act involving the fraudulent seller and an accomplice.
    - `Bidding Ratio`: A shill bidder participates more frequently to raise the auction price and attract higher bids from legitimate participants.
    - `Successive Outbidding`: A shill bidder successively outbids himself even though he is the current winner to increase the price gradually with small consecutive increments.
    - `Last Bidding`: A shill bidder becomes inactive at the last stage of the auction (more than 90\% of the auction duration) to avoid winning the auction.
    - `Auction Bids`: Auctions with SB activities tend to have a much higher number of bids than the average of bids in concurrent auctions.
    - `Auction Starting Price`: a shill bidder usually offers a small starting price to attract legitimate bidders into the auction.
    - `Early Bidding`: A shill bidder tends to bid pretty early in the auction (less than 25\% of the auction duration) to get the attention of auction users.
    - `Winning Ratio`: A shill bidder competes in many auctions but hardly wins any auctions.
    - `Auction Duration`: How long an auction lasted.
    - `Class`: 0 for normal behaviour bidding; 1 for otherwise.

## Instructions on how to run the project

1. `mkdir review_testing_capstone_one` run the command on your terminal
2. `cd review_testing_capstone_one` - changing the current cirectory into the folder
3. Run teh command `git clone -b gh_capstone_one_branch git@github.com:MekongDelta-mind/ml_zoomcamp_2022_projects.git .` to clone the branch `gh_capstone_one_branch`  to the current folder.
4. Now when you do `ls` you would fine the below files after the successful cloning

    ```bash
    (base):~/Workspace/ml_zoomcamp_sep_2022/review_testing/review_testing_capstone_one$ ls
    README.md  ml_zoomcamp_2022_capstone_one
    ```

5. go inside the folder `ml_zoomcamp_2022_capstone_one` and do an `ls` . Below are the files that you would find when you do a ls. Check if you can see the Dockerfile in the list of contents of the files

    ```bash
    (base):~/Workspace/ml_zoomcamp_sep_2022/review_testing/review_testing_capstone_one/ml_zoomcamp_2022_capstone_one$ ls
     Dockerfile     Readme.md                    bidding_notebook.ipynb  'model_C=1.bin'       predict_test.py
     Pipfile       'Shill Bidding Dataset.csv'   bidding_predict.py       predict.py
    ```

6. Run the command in the present directory with the command `docker build -t capstone_one .` to build the image . See to it that the whole building image is successful

    ```bash
    (base) :~/Workspace/ml_zoomcamp_sep_2022/review_testing/review_testing_capstone_one/ml_zoomcamp_2022_capstone_one$ docker build -t capstone_one .
    [+] Building 4.6s (11/11) FINISHED
     => [internal] load build definition from Dockerfile                                                                                       0.1s
     => => transferring dockerfile: 1.20kB                                                                                                     0.0s
     => [internal] load .dockerignore                                                                                                          0.0s
     => => transferring context: 2B                                                                                                            0.0s
     => [internal] load metadata for docker.io/library/python:3.8.13-slim                                                                      4.4s
     => [1/6] FROM docker.io/library/python:3.8.13-slim@sha256:dd46e1cb12432c17040638acb05508c35dc828db04f4f33c692d3894b7bc76cf                0.0s
     => [internal] load build context                                                                                                          0.0s
     => => transferring context: 18.54kB                                                                                                       0.0s
     => CACHED [2/6] RUN pip install pipenv                                                                                                    0.0s
     => CACHED [3/6] WORKDIR /app                                                                                                              0.0s
     => CACHED [4/6] COPY [Pipfile, Pipfile.lock, ./]                                                                                          0.0s
     => CACHED [5/6] RUN pipenv install --system --deploy                                                                                      0.0s
     => CACHED [6/6] COPY [predict.py, model_C=1.bin, ./]                                                                                      0.0s
     => exporting to image                                                                                                                     0.0s
     => => exporting layers                                                                                                                    0.0s
     => => writing image sha256:475919ce9873fe2da38676daf6a99a41e25ba759c242700a55021211346c5012                                               0.0s
     => => naming to docker.io/library/capstone_one                                                                                            0.0s

    Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
    ```

7. Once the image is build, run the image to create a container `docker run -it --rm -p 9696:9696 capstone_one` . It will start the web service and we can test service as follows
8. Open another terminal and go to the directory `review_testing/review_testing_capstone_one/ml_zoomcamp_2022_capstone_one` and do a `ls` . Chekc if you can see a file `predict_test.py` . If yes, then try to execute the command `python predict_test.py` and check if you get the result `Response from the service for the given test data point : {'fraud_or_not': 'No', 'fraud_probability': 0.0020708928277582295}
The bidding with the auciton_id: 2185 and bidding_id: m***t is fair bidding. Thanks for behaving !!!`

    ```bash

    (base) :~/Workspace/ml_zoomcamp_sep_2022/review_testing/review_testing_capstone_one/ml_zoomcamp_2022_capstone_one$ python predict_test.py
    Response from the service for the given test data point : {'fraud_or_not': 'No', 'fraud_probability': 0.0020708928277582295}
    The bidding with the auciton_id: 2185 and bidding_id: m***t is fair bidding. Thanks for behaving !!!
    ```

## Pre-requisite

Installing Docker Desktop into the OS you are going to test the project


## Cloning the repo, building and running the docker Image

1. Create a folder in any location. For example, in the desktop and name is as `zoomcamp_review_testing` .
- Cloning the repo
    1. inside the folder open the terminal or switch to the folder in the new folder created.
    2. execute teh command `git init` .
    3. For sanity check run the command `git branch -a` . This commadn shouldn’t return anything.
    4. run the command `git clone -b gh_mid_term_branch git@github.com:MekongDelta-mind/ml_zoomcamp_2022_projects.git` . After the clone is successful, try to go to the folder by running the commadn `cd ml_zoomcamp_2022_mid_term/` .
    5. Check the output to the command `ls -la` in teh folder `ml_zoomcamp_2022_mid_term` . If the clone is usccesful then you would get the following output.
        
        ```bash
        (base) prabin_nayak@DESKTOP-IUPLGMD:~/Workspace/ml_zoomcamp_sep_2022/review_testing/review_testing_mid_term$ git init
        hint: Using 'master' as the name for the initial branch. This default branch name
        hint: is subject to change. To configure the initial branch name to use in all
        hint: of your new repositories, which will suppress this warning, call:
        hint:
        hint:   git config --global init.defaultBranch <name>
        hint:
        hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
        hint: 'development'. The just-created branch can be renamed via this command:
        hint:
        hint:   git branch -m <name>
        Initialized empty Git repository in /home/prabin_nayak/Workspace/ml_zoomcamp_sep_2022/review_testing/review_testing_mid_term/.git/
        (base) prabin_nayak@DESKTOP-IUPLGMD:~/Workspace/ml_zoomcamp_sep_2022/review_testing/review_testing_mid_term$ git branch -a
        (base) prabin_nayak@DESKTOP-IUPLGMD:~/Workspace/ml_zoomcamp_sep_2022/review_testing/review_testing_mid_term$ git clone -b gh_mid_term_branch git@github.com:MekongDelta-mind/ml_zoomcamp_2022_projects.git
        Cloning into 'ml_zoomcamp_2022_projects'...
        remote: Enumerating objects: 39, done.
        remote: Counting objects: 100% (39/39), done.
        remote: Compressing objects: 100% (34/34), done.
        remote: Total 39 (delta 6), reused 9 (delta 2), pack-reused 0
        Receiving objects: 100% (39/39), 3.35 MiB | 1003.00 KiB/s, done.
        Resolving deltas: 100% (6/6), done.
        
        # movin to the correct folder to execute the program
        (base) prabin_nayak@DESKTOP-IUPLGMD:~/Workspace/ml_zoomcamp_sep_2022/review_testing/review_testing_mid_term/ml_zoomcamp_2022_projects$ ls -la
        total 20
        drwxr-xr-x 4 prabin_nayak prabin_nayak 4096 Nov  7 01:46 .
        drwxr-xr-x 4 prabin_nayak prabin_nayak 4096 Nov  7 01:46 ..
        drwxr-xr-x 8 prabin_nayak prabin_nayak 4096 Nov  7 01:46 .git
        -rw-r--r-- 1 prabin_nayak prabin_nayak  210 Nov  7 01:46 README.md
        drwxr-xr-x 4 prabin_nayak prabin_nayak 4096 Nov  7 01:46 ml_zoomcamp_2022_mid_term
        (base) prabin_nayak@DESKTOP-IUPLGMD:~/Workspace/ml_zoomcamp_sep_2022/review_testing/review_testing_mid_term/ml_zoomcamp_2022_projects$ cd ml_zoomcamp_2022_mid_term/
        (base) prabin_nayak@DESKTOP-IUPLGMD:~/Workspace/ml_zoomcamp_sep_2022/review_testing/review_testing_mid_term/ml_zoomcamp_2022_projects/ml_zoomcamp_2022_mid_term$ ls -la
        total 17896
        drwxr-xr-x 4 prabin_nayak prabin_nayak     4096 Nov  7 01:46  .
        drwxr-xr-x 4 prabin_nayak prabin_nayak     4096 Nov  7 01:46  ..
        drwxr-xr-x 2 prabin_nayak prabin_nayak     4096 Nov  7 01:46  .ipynb_checkpoints
        -rw-r--r-- 1 prabin_nayak prabin_nayak     1148 Nov  7 01:46  Dockerfile
        -rw-r--r-- 1 prabin_nayak prabin_nayak      240 Nov  7 01:46  Pipfile
        -rw-r--r-- 1 prabin_nayak prabin_nayak    18391 Nov  7 01:46  Pipfile.lock
        -rw-r--r-- 1 prabin_nayak prabin_nayak       72 Nov  7 01:46  Untitled.ipynb
        drwxr-xr-x 2 prabin_nayak prabin_nayak     4096 Nov  7 01:46  __pycache__
        -rw-r--r-- 1 prabin_nayak prabin_nayak    88846 Nov  7 01:46  analytics_olympiad_2022.ipynb
        -rw-r--r-- 1 prabin_nayak prabin_nayak    88846 Nov  7 01:46  analytics_olympiad_2022_python.ipynb
        -rw-r--r-- 1 prabin_nayak prabin_nayak       94 Nov  7 01:46  gh_mid_term.md
        -rw-r--r-- 1 prabin_nayak prabin_nayak     1905 Nov  7 01:46 'model_C=1.0.bin'
        -rw-r--r-- 1 prabin_nayak prabin_nayak     1233 Nov  7 01:46  predict.py
        -rw-r--r-- 1 prabin_nayak prabin_nayak     2930 Nov  7 01:46  predict_test.ipynb
        -rw-r--r-- 1 prabin_nayak prabin_nayak      937 Nov  7 01:46  predict_test.py
        -rw-r--r-- 1 prabin_nayak prabin_nayak   180008 Nov  7 01:46  submission.csv
        -rw-r--r-- 1 prabin_nayak prabin_nayak  5240488 Nov  7 01:46  test.csv
        -rw-r--r-- 1 prabin_nayak prabin_nayak 12648162 Nov  7 01:46  train.csv
        -rw-r--r-- 1 prabin_nayak prabin_nayak     3462 Nov  7 01:46  train.py
        ```
        
- Building the docker image
    1. check if the Dockerfile is present in the folder and run teh command `docker build -t zoomcamp_mid_term_pkn_gh .` 
    
    ```bash
    (base) prabin_nayak@DESKTOP-IUPLGMD:~/Workspace/ml_zoomcamp_sep_2022/review_testing/review_testing_mid_term/ml_zoomcamp_2022_projects/ml_zoomcamp_2022_mid_term$ docker build -t zoomcamp_mid_term_pkn_gh .
    [+] Building 5.0s (11/11) FINISHED
     => [internal] load build definition from Dockerfile                                                                                       0.1s
     => => transferring dockerfile: 1.19kB                                                                                                     0.0s
     => [internal] load .dockerignore                                                                                                          0.0s
     => => transferring context: 2B                                                                                                            0.0s
     => [internal] load metadata for docker.io/library/python:3.8.13-slim                                                                      4.8s
     => [internal] load build context                                                                                                          0.0s
     => => transferring context: 21.94kB                                                                                                       0.0s
     => [1/6] FROM docker.io/library/python:3.8.13-slim@sha256:dd46e1cb12432c17040638acb05508c35dc828db04f4f33c692d3894b7bc76cf                0.0s
     => CACHED [2/6] RUN pip install pipenv                                                                                                    0.0s
     => CACHED [3/6] WORKDIR /app                                                                                                              0.0s
     => CACHED [4/6] COPY [Pipfile, Pipfile.lock, ./]                                                                                          0.0s
     => CACHED [5/6] RUN pipenv install --system --deploy                                                                                      0.0s
     => CACHED [6/6] COPY [predict.py, model_C=1.0.bin, ./]                                                                                    0.0s
     => exporting to image                                                                                                                     0.0s
     => => exporting layers                                                                                                                    0.0s
     => => writing image sha256:f2cf3980181027def9c14ff83322251b340a42a1fdaa47dd15c2c26b18901b6f                                               0.0s
     => => naming to docker.io/library/zoomcamp_mid_term_pkn_gh                                                                                0.0s
    
    Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them 
    ```
    
- Running the docker image:
    
    To RUn teh image so that is initiates the app , try to 
    
    ```bash
    (base) prabin_nayak@DESKTOP-IUPLGMD:~/Workspace/ml_zoomcamp_sep_2022/review_testing/review_testing_mid_term/ml_zoomcamp_2022_projects/ml_zoomcamp_2022_mid_term$ docker run -it --rm -p 9696:9696 zoomcamp_mid_term_pkn_gh
    [2022-11-06 20:21:09 +0000] [1] [INFO] Starting gunicorn 20.1.0
    [2022-11-06 20:21:09 +0000] [1] [INFO] Listening at: http://0.0.0.0:9696 (1)
    [2022-11-06 20:21:09 +0000] [1] [INFO] Using worker: sync
    [2022-11-06 20:21:09 +0000] [8] [INFO] Booting worker with pid: 8
    /usr/local/lib/python3.8/site-packages/sklearn/base.py:329: UserWarning: Trying to unpickle estimator DictVectorizer from version 1.0.2 when using version 1.1.3. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:
    https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
      warnings.warn(
    /usr/local/lib/python3.8/site-packages/sklearn/base.py:329: UserWarning: Trying to unpickle estimator LogisticRegression from version 1.0.2 when using version 1.1.3. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:
    https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
      warnings.warn(
    ```
  
 
## Testing the app is working properly

1. open a new terminal  and change to the dir where the projects is present i .e `ml_zoomcamp_2022_mid_term`
2. list all the files in the current dir after moving to the folder to check if the test files is present or not
    
    ```bash
    (base) prabin_nayak@DESKTOP-IUPLGMD:~$ cd Workspace/ml_zoomcamp_sep_2022/review_testing/review_testing_mid_term/ml_zoomcamp_2022_projects/ml_zoomcamp_2022_mid_term
    (base) prabin_nayak@DESKTOP-IUPLGMD:~/Workspace/ml_zoomcamp_sep_2022/review_testing/review_testing_mid_term/ml_zoomcamp_2022_projects/ml_zoomcamp_2022_mid_term$ ls -ls
    total 17884
        4 -rw-r--r-- 1 prabin_nayak prabin_nayak     1148 Nov  7 01:46  Dockerfile
        4 -rw-r--r-- 1 prabin_nayak prabin_nayak      240 Nov  7 01:46  Pipfile
       20 -rw-r--r-- 1 prabin_nayak prabin_nayak    18391 Nov  7 01:46  Pipfile.lock
        4 -rw-r--r-- 1 prabin_nayak prabin_nayak       72 Nov  7 01:46  Untitled.ipynb
        4 drwxr-xr-x 2 prabin_nayak prabin_nayak     4096 Nov  7 01:46  __pycache__
       88 -rw-r--r-- 1 prabin_nayak prabin_nayak    88846 Nov  7 01:46  analytics_olympiad_2022.ipynb
       88 -rw-r--r-- 1 prabin_nayak prabin_nayak    88846 Nov  7 01:46  analytics_olympiad_2022_python.ipynb
        4 -rw-r--r-- 1 prabin_nayak prabin_nayak       94 Nov  7 01:46  gh_mid_term.md
        4 -rw-r--r-- 1 prabin_nayak prabin_nayak     1905 Nov  7 01:46 'model_C=1.0.bin'
        4 -rw-r--r-- 1 prabin_nayak prabin_nayak     1233 Nov  7 01:46  predict.py
        4 -rw-r--r-- 1 prabin_nayak prabin_nayak     2930 Nov  7 01:46  predict_test.ipynb
        4 -rw-r--r-- 1 prabin_nayak prabin_nayak      937 Nov  7 01:46  predict_test.py
      176 -rw-r--r-- 1 prabin_nayak prabin_nayak   180008 Nov  7 01:46  submission.csv
     5120 -rw-r--r-- 1 prabin_nayak prabin_nayak  5240488 Nov  7 01:46  test.csv
    12352 -rw-r--r-- 1 prabin_nayak prabin_nayak 12648162 Nov  7 01:46  train.csv
        4 -rw-r--r-- 1 prabin_nayak prabin_nayak     3462 Nov  7 01:46  train.py
    ```
    
3. Then execute the command `python predict_test.py` and check the result is below.
    
    ```bash
    (base) prabin_nayak@DESKTOP-IUPLGMD:~/Workspace/ml_zoomcamp_sep_2022/review_testing/review_testing_mid_term/ml_zoomcamp_2022_projects/ml_zoomcamp_2022_mid_term$ python predict_test.py
    {'accept_or_reject': 'No', 'decision_probability': 0.4484685581863869}
    Sorry :( , the customer with customer_id: pkn_2022 is rejected for the insurance claims
    (base) prabin_nayak@DESKTOP-IUPLGMD:~/Workspace/ml_zoomcamp_sep_2022/review_testing/review_testing_mid_term/ml_zoomcamp_2022_projects/ml_zoomcamp_2022_mid_term$
    ```
    
    NOTE: you can open the predict_test.py and change the `customer` value to test with different values and check if it is working properly or not. Like you can change the gender to 
    'female' while keeping other and check for the results to check if the project is working fine.
    
    ```json
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
    ```

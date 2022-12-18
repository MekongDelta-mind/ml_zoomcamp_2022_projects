#running th ebse OS which is going ot be used for teh docker image
FROM python:3.8.13-slim

RUN pip install pipenv

# creating the app directory which will create the folder which will contain all the files required for creating the app
# at this stage you are in teh app folder
WORKDIR /app

# copying all the env reltaed files into teh app
# ./ -- > is current dir
COPY ["Pipfile", "Pipfile.lock", "./"]

#here we don't need to pipenv shell as we don't need to  create a  virtual env inside docker as it already isollated from system OS 
#so in turn it is isolated from the OS too
# --system --> instead of creating a venv , it uses the current config as a system config
# --deploy 
RUN pipenv install --system --deploy

# copying files which will actually predict the model
COPY ["predict.py", "model_C=1.bin", "./"]

# exposing the port number of the docker image to the host machine
EXPOSE 9696

# the commadn to actually start the app to be exposed for the host machine to interact
# the actual ocmmnad which is executed in real in the cli  -> gunicorn --bind=0.0.0.0:9696 predict:app
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]
# Creating URL Shortener Service using AI Pair Programmer - Github Copilot

The goal of this project is to use AI Pair Programmer to generate a frontend and backend for URL shortener service.
We are using Github Copilot for this which has generated all the code as well as steps to setup the environment.

Youtube Demonstration: https://youtu.be/oIhiezJfMF0

# Setup

## Install Redis
First, we need to setup redis as key-value store. To do this, execute following commands on MacOS
```
brew install redis
brew services start redis
```

## Run Backend
To run backend, execute following commands : 
```
cd backend
pip3 install
python3 app.py
```
This will run the backend and will expose Rest API endpoints over localhost:5000

## Run Frontend
Open index.html in browser to run the frontend page for the service.

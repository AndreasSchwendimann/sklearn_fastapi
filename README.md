# Dockerized FastAPI for FE-DS Trial Day
This repository can be used to deploy a local instance of the pipeline used in the trial day challenge.
The currently implemented model is a GMM with 5 clusters.

## Clone, Build and Run
Clone this repository, navigate to the cloned folder to build the image and start a container:

```bash
https://github.com/AndreasSchwendimann/trialday-api

docker build -t modelapi .
docker run -p 80:80 modelapi
```

## Documentation
The api documentation is generated automatically by FastAPI and is available when deployed on:  
- http://localhost/redoc
- http://localhost/docs

## Verification
Returns True:  
http://localhost/predict/?meeting_data=25,1,0.7142857142857143,0.2857142857142857,0,0,14,24300,0,0.7857142857142857,0,0,0.21428571428571427,0

Returns False:  
http://localhost/predict/?meeting_data=10,9,0.9230769230769231,0.07692307692307693,0,0,13,21600,0,0.8461538461538461,0,0,0.15384615384615385,0

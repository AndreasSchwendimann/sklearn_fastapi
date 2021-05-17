# Dockerized FastAPI for FE-DS Trial Day
This repository can be used to deploy a local instance of the pipeline used in the trial day challenge.

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
http://localhost/predict/?meeting_data=3,5,0.6507936507936508,0.3492063492063492,0,0,63,18001,0.15873015873015872,0.6031746031746031,0,0,0.23809523809523808,0

Returns False:  
http://localhost/predict/?meeting_data=12,8,0.1774193548387097,0.45161290322580644,0.3709677419354839,0,62,17100,0,1,0,0,0,0

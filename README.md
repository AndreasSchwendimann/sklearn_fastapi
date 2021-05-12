# Dockerized FastAPI for FE-DS Trial Day
This repository can be used to deploy a local instance of the pipeline used in the trial day challenge.

## Clone, Build and Run
Clone this repository, navigate to the cloned folder to build the image and start a container:

```bash
https://github.com/AndreasSchwendimann/trialday-api

docker build -t modelAPI . 
docker run -p 80:80 modelAPI
```

## Documentation
The api documentation is generated automatically by FastAPI and is available when deployed on:  
- http://localhost/redoc
- http://localhost/docs

## Verification
Returns True:  
http://localhost/predict/?duration=80000&meeting_data=1,2,0,0,0.5,0.5,7,0.1,0.1,0.1,0.1,0.1,0.1

Returns False:  
http://localhost/predict/?duration=8000&meeting_data=1,2,0,0,0.5,0.5,7,0.1,0.1,0.1,0.1,0.1,0.1

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install 'joblib' \
     'scikit-learn==0.22.*' \
     'pandas'

COPY ./model /model
COPY ./app /app
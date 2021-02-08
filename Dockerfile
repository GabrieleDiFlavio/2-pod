FROM python:3.8-slim

RUN pip3 install Flask 
RUN pip3 install urllib3

COPY ./  ./app

# Exposing Ports
EXPOSE 5000

WORKDIR ./app

CMD [ "python3", "sum.py" ]

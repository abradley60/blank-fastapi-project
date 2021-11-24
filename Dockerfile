FROM python:3.8

RUN apt-get -y update && \
    apt-get install -y libgl1-mesa-glx poppler-utils

ADD requirements.txt .

RUN pip install -r requirements.txt 

WORKDIR "/opt/working"
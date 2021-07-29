FROM python:3.9

WORKDIR /IMDB_analysis
COPY . .

RUN pip install -r requirements.txt

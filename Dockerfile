FROM python:3.8
WORKDIR /application
COPY etl_csv_msql.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 1270
WORKDIR /application
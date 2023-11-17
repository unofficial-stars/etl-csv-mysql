FROM python:3.8
WORKDIR /application
COPY . .
RUN pip install -r requirements.txt
EXPOSE 1270
CMD ["sh", "deploy.sh"]
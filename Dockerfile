FROM python:3-slim
WORKDIR /programas/ingesta
RUN pip3 install --no-cache-dir boto3 psycopg2-binary pandas
COPY . .
CMD [ "python3", "./ingesta.py" ]

FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN	pip install uvicorn && \
	pip install django && \
    pip install python-dotenv && \
    pip install psycopg2

RUN apt-get update && \
    apt-get install -y \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
	pip install -r requirements.txt

RUN openssl req -x509 -nodes -days 365 -newkey \
    rsa:2048 -keyout /app/key.pem -out /app/cert.pem -subj \
    "/C=FR/ST=France/L=Lyon/O=42/OU=LaRueZebi/CN=transcendance.fr"

EXPOSE 8000

CMD [ "uvicorn", "trans.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--ssl-keyfile", "/app/key.pem", "--ssl-certfile", "/app/cert.pem" ]

#CMD ["tail", "-f", "/dev/null"] # issue finding
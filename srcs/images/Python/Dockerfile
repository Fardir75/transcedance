FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN apt-get update && \
    apt-get install -y \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
	pip install -r requirements.txt

RUN	pip install uvicorn && \
	pip install django

EXPOSE 8000

CMD [ "uvicorn", "trans.asgi:application", "--host", "0.0.0.0", "--port", "8000" ]

#CMD ["tail", "-f", "/dev/null"] # issue finding
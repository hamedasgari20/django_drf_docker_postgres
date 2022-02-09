FROM python:3.8.6

RUN pip install -U pip
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN pip install gunicorn

COPY . /code/
WORKDIR /code

EXPOSE 8000





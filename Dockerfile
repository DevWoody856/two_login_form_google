FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /twologin_8_220424
COPY requirements.txt /twologin_8_220424/requirements.txt

RUN pip install -r requirements.txt

COPY . /twologin_8_220424

CMD python manage.py runserver 0.0.0.0:8022
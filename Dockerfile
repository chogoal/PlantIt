FROM python:3.9.0

WORKDIR /home/

RUN echo "plantitplantit"

RUN git clone https://github.com/WholesomeMullet/plant-it.git

WORKDIR /home/plant-it/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=PlantIt.settings.deploy && python manage.py migrate --settings=PlantIt.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=PlantIt.settings.deploy PlantIt.wsgi --bind 0.0.0.0:8000"]

FROM python:3.9.0

WORKDIR /home/

RUN echo "plantit_for_planet"

RUN git clone https://github.com/chogoal/PlantIt.git

WORKDIR /home/PlantIt/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=PlantIt.settings.deploy && python manage.py migrate --settings=PlantIt.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=PlantIt.settings.deploy PlantIt.wsgi --bind 0.0.0.0:8000"]

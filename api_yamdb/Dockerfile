FROM python:3.7-slim

RUN mkdir /app

COPY requirements.txt /app
# Скопировал requirements.txt отдельно для того, чтобы в случае если в проекте
# будут какие-либо изменеия и придётся пересобирать образ, не пришлось
# устанавливать зависимости повторно.
# Этот процесс может занимать достаточно большое количество времениq.

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY . /app

WORKDIR /app

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0.0.0.0:8000"]

LABEL author='psevdoslon.ya@yandex.ru' version=1
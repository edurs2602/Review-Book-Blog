FROM python:3.11

LABEL maintainer="Luís Eduardo <edurs.2602@gmail.com>"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /livros

COPY . /livros

RUN pip install --upgrade pip && pip install -r livros/requirements.txt

EXPOSE 8000

CMD ["python", "./livros/manage.py", "runserver", "0.0.0.0:8000"]
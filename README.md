# APP

Assay Marketplace Project based on [Django](https://docs.djangoproject.com/en/3.2/) is a high-level Python web
framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes
care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent
the wheel. It’s free and open source.

## Local Development

This is the initial setup for Image Analysis App .env.example to .env for the application to run. Navigate to the
project folder and deploy the stack. This command will launch 3 services.

GitHub Backend Repo: https://github.com/ish1301/edlight-project

```shell
cp env.example .env
docker-compose up -d
```

### Services

- amp: Backend service http://localhost:8888
- pgdb: Database service localhost port 5432
- adminer: Database administration http://localhost:8099

### Django Admin

URL: [http://localhost:8888/admin](http://localhost:8888/admin/)

Credential: Depending upon where you import the initial database

## Database Migrations

[Migrations are Django](https://docs.djangoproject.com/en/3.2/topics/migrations/)'s way of propagating changes you make
to your models (adding a field, deleting a model, etc.) into your database schema. They’re designed to be mostly
automatic.

```shell
docker exec -it amp bash
python manage.py makemigrations
python manage.py migrate
```

## Unit Testing

Unit testing is integrated as part of [PR merge workflow](https://github.com/ish1301/edlight-project/actions) and
executed before merges are approved at GitHub. Although unit tests can be executed locally as well.

```shell
docker exec -it amp bash
python manage.py test
```

## Source Code Formatting

Source code formatting is part of GitHub workflow approval, but you can manually run this with below commands.

```shell
docker exec -it amp bash
black api
flake8 api
```
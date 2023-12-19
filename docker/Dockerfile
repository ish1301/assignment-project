FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY ./requirements.txt ./requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . ./

EXPOSE 8000

RUN chmod +x ./scripts/run.sh

CMD [ "./scripts/run.sh" ]

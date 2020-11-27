FROM ubuntu:18.04
MAINTAINER motorny.nikita@gmail.com

RUN  apt-get update && apt-get install -y python3.7 python3.7-dev python3-pip
RUN rm /usr/bin/python3 && ln -s /usr/bin/python3.7 /usr/bin/python3
RUN python3 --version
RUN python3 -m pip install --upgrade pip && python3 -m pip install wheel

##    && apk add --no-cache --virtual .build-deps \
##    gcc \
##    python3-dev \
##    musl-dev \
##    postgresql-dev \
##    && pip install --no-cache-dir psycopg2-binary \
## && apk del --no-cache .build-deps && apk add postgresql-dev gcc
##RUN apk add  libffi-dev libxml2 libxml2-dev libxslt libxslt-dev libjpeg-turbo-dev zlib-dev gcc g++ gfortran

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN python3 -m pip --version && python3 -m pip install -r requirements.txt

RUN python3 -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"

ADD . /app
RUN pip install --no-deps ./

CMD ["sh", "run.sh"]
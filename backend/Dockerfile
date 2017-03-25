FROM python:2.7

WORKDIR /var/app

RUN pip install uwsgi

RUN useradd uwsgi -s /bin/false
RUN mkdir /var/log/uwsgi && chown -R uwsgi:uwsgi /var/log/uwsgi

ADD ./requirements.txt /var/app
RUN pip install -r /var/app/requirements.txt

ADD . /var/app

EXPOSE 8080

ADD uwsgi-start.sh /

CMD []
ENTRYPOINT ["/uwsgi-start.sh"]


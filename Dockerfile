FROM python:3.6
ENV PYTHONUNBUFFERED 1
MAINTAINER Roman Mashenkin <xromash@vxdesign.store>

RUN echo "Europe/Moscow" > /etc/timezone && \
      dpkg-reconfigure -f noninteractive tzdata

RUN mkdir /web
WORKDIR /web
ADD requirements.txt /web/
RUN pip install -r requirements.txt
ADD . /web/

CMD [ "/web/manage.py", "runserver", "0.0.0.0:8000" ]
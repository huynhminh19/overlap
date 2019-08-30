FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh && ln -s /usr/local/bin/docker-entrypoint.sh /
COPY docker-entrypoint.test.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.test.sh && ln -s /usr/local/bin/docker-entrypoint.test.sh /
ENTRYPOINT ["docker-entrypoint.sh"]

FROM hylang:python3.10
COPY . /web_app
WORKDIR /web_app
RUN pip3 install --only-binary :all: greenlet
RUN pip3 install --only-binary :all: Flask-SQLAlchemy
RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install -y netcat-traditional
RUN chmod 777 start_script.sh
ENTRYPOINT ["./start_script.sh"]
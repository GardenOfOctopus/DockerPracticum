FROM mysql:latest
COPY . /database
WORKDIR /database
RUN pip3 install --only-binary :all: greenlet
RUN pip3 install --only-binary :all: Flask-SQLAlchemy
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]
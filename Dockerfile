FROM python:3

ENV PYTHONPATH /src
WORKDIR /src
ENTRYPOINT ["python", "-u"]

COPY . /src
RUN pip install -r requirements.txt
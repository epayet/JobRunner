FROM python:3.5-slim

ENV PYTHONPATH /src
WORKDIR /src
ENTRYPOINT ["python"]

COPY . /src
RUN pip install -r requirements.txt
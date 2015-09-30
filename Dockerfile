FROM python:3.5-slim

WORKDIR /src
ENTRYPOINT ["python", "main.py"]

COPY . /src
RUN pip install -r requirements.txt
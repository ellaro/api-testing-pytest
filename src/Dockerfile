FROM python:3.10

WORKDIR /ella

COPY main.py requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python3", "main.py"]

FROM python:3.9

WORKDIR /code/

COPY requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt

COPY . /code/

CMD [ "python3", "src/main.py" ]

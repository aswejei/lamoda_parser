FROM python:3.10-alpine

RUN python3 -m pip install --upgrade pip && pip install pipenv

WORKDIR consumer

COPY ./consumer .

COPY Pipfile .

COPY Pipfile.lock .

RUN pipenv install --system --deploy

ENTRYPOINT ["python3", "consumer.py"]
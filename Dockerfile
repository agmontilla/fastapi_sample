FROM python:3.7.13

RUN mkdir /code

COPY /cmd /code/cmd
RUN chmod +x /code/cmd/*.sh

COPY pyproject.toml /code

WORKDIR /code
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY /app /code/app

CMD [ "/bin/bash", "/code/cmd/run.sh" ]
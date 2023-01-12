FROM apache/airflow:2.5.0
USER root
RUN apt-get update \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
USER airflow
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --user -r requirements.txt
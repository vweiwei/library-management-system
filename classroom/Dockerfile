FROM python:3.8
ADD . /classroom/
ADD requirements.txt .
ENV PYTHONPATH /classroom/
WORKDIR .
RUN pip install -r requirements.txt
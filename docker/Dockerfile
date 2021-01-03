FROM python:3.8.7-buster
ARG project_dir=/search-app/
ADD requirements.txt $project_dir

WORKDIR $project_dir
RUN pip install -r requirements.txt
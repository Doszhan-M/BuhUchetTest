FROM python:3.9.5-alpine

# set work directory
WORKDIR /home/github/BuhUchetTest

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /home/github/BuhUchetTest/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /home/github/BuhUchetTest/

# run entrypoint.sh
RUN ["chmod", "+x", "/home/github/BuhUchetTest/entrypoint.sh"]
ENTRYPOINT ["sh", "/home/github/BuhUchetTest/entrypoint.sh"]
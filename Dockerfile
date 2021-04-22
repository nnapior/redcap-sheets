#from alpine:latest


#LABEL maintainer="mariod<mariod@udel.edu>"

#RUN apk add --no-cache python3-dev 
   #&& pip3 install --upgrade pip

#RUN apk add apache2 php7-apache2 php7-gd php7-mysqli
#We copy just the requirements.txt first to leverage Docker cache


#WORKDIR /usa/mariod/RedcapApp/475-team5-s21project/

#COPY . /usa/mariod/RedcapApp/475-team5-s21project/

#RUN pip3 --no-cache-dir  install -r requirements.txt

#EXPOSE 500
#COPY . /redcap_sheets_webapp

#ENTRYPOINT ["python3"]
#CMD [ "redcap_sheets_webapp.py" ]


FROM ubuntu:16.04

LABEL maintainer="Mario Durso <mariod@udel.edu>"

RUN apt-get update -y && \
    apt-get install -y python-pip python3-dev

WORKDIR /475-team5-s21project

# We copy just the requirements.txt first to leverage Docker cache
COPY . /requirements.txt

RUN pip install -r requirements.txt

COPY . /475-team5-s21project

ENTRYPOINT [ "python3" ]

CMD [ "redcap_sheets_webapp.py" ]


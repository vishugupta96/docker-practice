From python:3.11.2

ENV DockerHOME=/home/app/webapp 

RUN mkdir -p $DockerHOME  

WORKDIR $DockerHOME  


# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  


# install dependencies  
RUN pip install --upgrade pip 



# copy whole project to your docker home directory. 
COPY . $DockerHOME  


# run this command to install all dependencies  
RUN pip install -r requirements.txt

  
# port where the Django app runs  
EXPOSE 8000  


# start server  
CMD python manage.py runserver  

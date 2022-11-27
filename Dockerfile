FROM python:3.9

WORKDIR /usr/src/app

COPY func.py .
  #COPY utils .
#COPY detect.py .
#COPY export.py .
#COPY fire_boizz.pt .
#COPY requirements.txt .


#RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./func.py" ]
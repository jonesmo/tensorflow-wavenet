FROM python:3.9.16

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install --no-deps numba==0.48
RUN apt update
RUN apt-get install -y libsndfile1-dev

COPY . .

RUN mkdir -p /generated

ENTRYPOINT ["python3", "generate.py"]
FROM python:3.11.8-alpine


WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x django.sh

EXPOSE 8000

ENTRYPOINT [ "./django.sh" ]
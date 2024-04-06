FROM python:3.8-alpine
ENV PYTHONUNBUFFERED=1
RUN apk update && apk add gcc python3-dev musl-dev
# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev curl-dev
WORKDIR /app
COPY app/ .
RUN pip3 install -r requirements.txt
EXPOSE 80

CMD ["./start.sh"]
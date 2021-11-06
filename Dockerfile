FROM alpine:latest


RUN apk add --no-cache --upgrade bash && apk add --update python3

WORKDIR .

COPY . .

RUN /bin/bash
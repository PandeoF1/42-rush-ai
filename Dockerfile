FROM alpine:latest


RUN apk add --no-cache --upgrade bash && apk add --update python3

WORKDIR ./srcs

COPY ./srcs .

RUN /bin/bash
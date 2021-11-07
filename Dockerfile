FROM python:latest

### Mandatory
#
WORKDIR /app
#
RUN adduser player && chown -R player /app
#
USER player
#############

COPY . /app/

# Run a little script : the /bin/bash maintain the container running
CMD ["python3", "/app/srcs/main.py"]

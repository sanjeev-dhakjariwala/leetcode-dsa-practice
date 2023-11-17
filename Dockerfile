FROM ubuntu:latest
LABEL authors="sanje"

ENTRYPOINT ["top", "-b"]
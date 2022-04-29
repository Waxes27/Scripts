FROM debian

COPY clean.py /root
WORKDIR /root

RUN apt update -y
RUN apt install python3 -y
RUN python3 clean.py
RUN ls -la *
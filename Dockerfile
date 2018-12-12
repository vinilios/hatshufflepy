FROM ubuntu:16.04
MAINTAINER Stefanos Chaliasos "schaliasos@grnet.gr"

ENV HOME /root

# Install libsnark
RUN apt-get update && apt-get install -y \
    build-essential cmake git libgmp3-dev libprocps4-dev python-markdown \
    libboost-all-dev libssl-dev pkg-config python-pip
RUN pip install cython setuptools
RUN git clone https://github.com/StefanosChaliasos/hatshufflepy.git \
    && cd hatshufflepy && python setup.py install

WORKDIR $HOME

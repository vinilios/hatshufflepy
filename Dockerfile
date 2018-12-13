FROM debian:jessie
MAINTAINER Stefanos Chaliasos "schaliasos@grnet.gr"

ENV HOME /root

# Install libsnark
RUN apt-get update && apt-get install -y \
    build-essential cmake git libgmp3-dev libprocps3-dev python-markdown \
    libboost-all-dev libssl-dev pkg-config python-pip python-setuptools cython
ADD . /root/hatshufflepy
RUN cd /root/hatshufflepy && ./clean.sh; echo "OK";
RUN cd /root/hatshufflepy && ./install_depends.sh;
RUN cd /root/hatshufflepy && python setup.py bdist_wheel;
RUN cd /root/hatshufflepy && python setup.py install;

WORKDIR $HOME

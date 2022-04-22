FROM ubuntu:22.04

RUN apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt install -y \
   xz-utils \
   build-essential \
   cmake git \
   python3 \
   curl wget \
   tree nano vim htop tmux

RUN apt-get install -y python3-pip
RUN pip install conan

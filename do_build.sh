#!/usr/bin/env bash

set -v -x -e

THIS_DIR="$( cd "$( dirname "$0" )" && pwd )"
cd $THIS_DIR

cd /sources &&\
  mkdir -p build &&\
  cd build &&\
  conan install .. --build=missing &&\
  cmake .. &&\
  make

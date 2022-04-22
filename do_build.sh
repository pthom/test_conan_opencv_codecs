#!/usr/bin/env bash

set -v -x -e

THIS_DIR="$( cd "$( dirname "$0" )" && pwd )"
cd $THIS_DIR

cd $THIS_DIR &&\
  mkdir -p build &&\
  cd build &&\
  conan install .. --build=missing &&\
  cmake .. -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake &&\
  make

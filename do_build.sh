#!/usr/bin/env bash

set -e

THIS_DIR="$( cd "$( dirname "$0" )" && pwd )"
cd $THIS_DIR
mkdir -p build
cd build
conan install ..
cmake ..
make

#!/bin/zsh
# This file must get called out of the project root

mkdir build
pip wheel --wheel-dir ./build .
rm -rf ./src/yearsinpixels_business.egg-info
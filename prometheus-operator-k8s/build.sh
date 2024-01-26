#!/bin/bash

set -x

# setup default values, use environment variables to override
# for example: exaport LESSON=lesson150 && ./build.sh
VER="${VER:-latest}"
LESSON="${LESSON:-lesson000}"

# myapp
docker build -t 
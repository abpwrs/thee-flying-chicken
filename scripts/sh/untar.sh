#!/bin/sh
# Author: AlexPowers
# Sun Dec 30 13:12:53 CST 2018
# All scripts should be run from the project root
for tar_file in ./data/*.tar.gz; do
mkdir ${tar_file%.tar.gz}
tar -xzvf ${tar_file} -C ./data/
done

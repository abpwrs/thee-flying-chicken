#!/usr/bin/env bash
# all scripts should be called from the root directory
for tar_file in ./data/*.tar.gz; do
tar -xzvf ${tar_file}
done

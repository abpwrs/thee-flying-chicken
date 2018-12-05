#!/usr/bin/env bash
for tar_file in ./*.tar.gz; do
tar -xzvf ${tar_file}
done

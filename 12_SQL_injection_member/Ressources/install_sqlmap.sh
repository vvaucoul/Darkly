#!/bin/bash

# Download sqlmap from the provided link
wget https://github.com/sqlmapproject/sqlmap/tarball/master -O sqlmap.tar.gz

# Extract the downloaded file
tar -xvf sqlmap.tar.gz
rm -rf sqlmap.tar.gz
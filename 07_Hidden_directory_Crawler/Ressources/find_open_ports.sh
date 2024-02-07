#!/bin/bash

# Prompt user for IP address
read -p "Enter IP address to scan: " ip_address

# Check if IP address is valid
if [[ ! $ip_address =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "Invalid IP address"
    exit 1
fi

# Scan IP address using nmap
nmap -v -A $ip_address

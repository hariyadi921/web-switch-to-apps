#!/bin/bash

# Input: Domain/IP
target=$1

# Eksekusi berbagai tools
whois $target > reports/whois.txt
host $target > reports/dns.txt
whatweb $target --color=never > reports/whatweb.txt
curl -s "https://api.ip2country.com/ip?$target" | jq . > reports/geo.json

# Panggil Python untuk processing
python3 processor.py reports/geo.json

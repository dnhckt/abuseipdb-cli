#! /bin/bash

mkdir /opt/ipdb/
cp ./abusecheck.py /opt/ipdb/abusecheck.py
cp install.sh /opt/ipdb/install.sh

echo "alias ipdb='python /opt/ipdb/abusecheck.py'" >> ~/.bashrc
source ~/.bashrc

read -p "Enter your API key:" apikey
export ABUSE_API_KEY="$apikey"

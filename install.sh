#! /bin/bash

mkdir /opt/ipdb/
mv ./abusecheck.py /opt/ipdb/
mv install.sh /opt/ipdb/

echo "alias ipdb='python /opt/ipdb/abusecheck.py'" >> ~/.bashrc
source ~/.bashrc

read -p "Enter your API key:" apikey
export $ABUSE_API_KEY=$apikey
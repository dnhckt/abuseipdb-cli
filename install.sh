#! /bin/bash -i

mkdir /opt/ipdb/
cp ./abusecheck.py /opt/ipdb/
#mv install.sh /opt/ipdb/

echo "alias ipdb='python /opt/ipdb/abusecheck.py'" >> ~/.bashrc

read -p "Enter your API key:" apikey
export ABUSE_API_KEY="$apikey"

source ~/.bashrc

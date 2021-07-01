import os, sys, requests, json

ABUSE_API_KEY = os.environ.get("ABUSE_API_KEY") # This assumes install.sh has been ran, or you've got your API Key saved as an environment variable

def checkIP(dodgyIP):
    url = "https://api.abuseipdb.com/api/v2/check"  

    querystring = {
    "ipAddress": dodgyIP,
    "maxAgeInDays": "90" # no older than
    }

    headers = {
    "Accept": "application/json",
    "Key": ABUSE_API_KEY,
    }

    response = requests.request(method="GET", url=url, headers=headers, params=querystring)
    decodedResponse = json.loads(response.text)

    # output
    print ""
    print "===================================================="    
    print ""
    print "Results for", decodedResponse["data"]["ipAddress"]
    print "==="

    # If the IP may be private, check
    if ( "172" in decodedResponse["data"]["ipAddress"] or "192" in decodedResponse["data"]["ipAddress"]):

        if (decodedResponse["data"]["isPublic"] == False):
            print "Private IP"

    print "Country:", decodedResponse["data"]["countryCode"]
    print "Owner:",  decodedResponse["data"]["domain"]

    print "Abuse confidence:", decodedResponse["data"]["abuseConfidenceScore"], "%"
    print "Times reported:", decodedResponse["data"]["totalReports"]
    
    if (decodedResponse["data"]["abuseConfidenceScore"] > 0):
        print "iptables -A INPUT -s " + decodedResponse["data"]["ipAddress"] + " -j DROP"
        
    print ""
    print "===================================================="    
    print ""

IPnum = len(sys.argv)

if (IPnum-1) == 0:
    print "No arguments given"

if (IPnum-1) == 1:
    checkIP(str(sys.argv[1]))

for x in range(2,6):
    if (IPnum-1) == x:
        for y in range(1, x+1):
            checkIP(str(sys.argv[y]))

if IPnum > 6:
    print "Invalid input" 

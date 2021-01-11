from flask import Flask
import sys
import requests, json

api_key = "c652aad8624cf514f2e3"
base_url = "https://free.currconv.com/api/v7/"



def currList():
    action ="currencies?apiKey="
    complete_url=base_url+action+api_key
    response = requests.get(complete_url) 
    x = response.json() 
    return (x["results"].keys())

def convert(amount,fr,to):
     action ="convert?apiKey="
     querry= "&q="+fr+"_"+to+","+to+"_"+"fr"
     complete_url= base_url+action+api_key+querry

     response = requests.get(complete_url) 
     x = response.json() 
     result= float(amount)*float(x["results"][fr+"_"+to]["val"])
     return result

    
def main(argv):
    if argv[0]=="convert":
        return (convert(argv[1],argv[2],argv[3]))
    else:
        return currList()

     
    


if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv[1:])
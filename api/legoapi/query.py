#LEGO's search queries

# import BeatuifulSoup into the code.
from bs4 import BeautifulSoup as bs
import requests
import re
from legoapi.test import test
from legoapi.lego_query_generator import *
#from legoapi.lego_query_generator import get_lego_query_payload #issue here
from legoapi.lego_response_parser import *


class LegoQuery:
    def __init__(self, base_url):
        self.url = base_url
        test()
    def get_api_key(self):

        url = "https://{}/en-us/service/buildinginstructions/".format(self.url)
        print(url)

        # STEP 1: sent the http request to the lego instructions page 

        response = requests.get(url)
        htmlText = response.text
        #print(response.text)


        # STEP 2 extract the url of the script.min.min.**

        # Load the html text into page using bs4
        page = bs(htmlText, "html.parser") #interpretes/ translates html file
        scripts = page.find_all("script")
        # List<String> scripts = new ArrayList<String>("tejst", "test")
        for script in scripts: # for(String script in scripts) { ... }
            if 'src' in script.attrs and  "scripts.min" in script.attrs['src']:
                target_script_url = script.attrs['src']

        apiKey = None

        if target_script_url is not None:
            # download the javascript
            script = requests.get(target_script_url)

        #-------??
            #print(script.text)
            matched = re.search(r'var Go={headers:{"x-api-key":"([\w]+)"}}', script.text)
            print("{}, {}".format(matched.group(0),matched.group(1)))
            apiKey=matched[1]

        return apiKey
    
    def search(self, query):
        url = "https://services.slingshot.lego.com/api/v4/lego_historic_product_read/_search"
        api_key = "p0OKLXd8US1YsquudM1Ov9Ja7H91jhamak9EMrRB" #self.get_api_key()
        print("apiKey = {}".format(api_key))

        headers = {}
        headers['Content-Type']= 'application/json'
        headers['X-Api-Key'] = api_key

        payload =get_lego_query_payload(keyword=query, index=0, batch_size=12)
        response = requests.post(url=url, json=payload, headers=headers) #48, 54, 50
        #print(response.json())
        response_print = response.json()
        parse_response(response_print)
        return response_print



    


    



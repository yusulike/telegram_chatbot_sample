# request, urllib, httplib2 등의 패키지가 http request 요청 가능
# 여기서는 httplib2를 사용

import httplib2
import json
import urllib.parse

#import simplejson as json

#def print_json(content):
#    print json.dumps(content, indent=4)

def get_cryto_currency_info(currency="ALL"):
    baseURL = "https://api.bithumb.com/public/ticker/"
    url_query = baseURL + currency

    print ("Request URL : %s" % (url_query))
    
    # 요청 & 응답
    http = httplib2.Http()
    response, content = http.request(
        url_query, "GET"
    )

    return response, content


def get_weather_info(region):
    # Rest API Query 문 생성
    baseURL = "https://query.yahooapis.com/v1/public/yql?q="

    yql_query = """select * from weather.forecast where woeid in 
        (select woeid from geo.places(1) where text='%s')""" % (region)


    yql_url = baseURL + urllib.parse.quote(yql_query) +  "&format=json"
    print ("Request URL : %s" % (yql_url))
    
    # 요청 & 응답
    http = httplib2.Http()
    response, content = http.request(
        yql_url, "GET"
    )
    return response, content
    
if __name__ == "__main__":
    response, content = get_cryto_currency_info('BTC')

    content = json.loads(content)
    print (json.dumps(content, indent=4))
    
    print (content['data']['closing_price'])

    response, content = get_weather_info("seoul,kr")
    content = json.loads(content)
    print (json.dumps(content, indent=4))

    # Get one word conditon
    print (content['query']['results']['channel']['item']['condition']['text'])


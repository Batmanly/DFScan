import time
import webbrowser
from threading import Thread

import requests
import uncurl

from keyword_parse import keywords, search_engine_keyword
from parse_curl import websites_with_timer, websites_without_timer, search_engines




# https://avilpage.com/2018/03/convert-browser-requests-to-python-requests.html
def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session

def make_request(curl_command):
    try:
        # parse request
        parsed_curl = uncurl.parse_context(curl_command)
        # print(parsed_curl.data)
        # create session for request
        session = get_tor_session()
        print("TOR IP" + session.get("http://httpbin.org/ip").text)


        # send request with Tor
        req = session.post(parsed_curl.url, headers=parsed_curl.headers, cookies=parsed_curl.cookies,
                            params=parsed_curl.data)
        # send request with your ip
        # req = requests.post(parsed_curl.url, headers=parsed_curl.headers, cookies=parsed_curl.cookies, params=parsed_curl.data)
        webbrowser.open(req.url)

    except Exception as e:
        print(e)


def without_timer():
    for curl_command in websites_without_timer:
        for i in range(len(keywords)):
            # look for the first keyword
            if 'KEYWORD' in curl_command:
                curl_command = curl_command.replace('KEYWORD', keywords[i])
            # change changed keyword
            else:
                curl_command = curl_command.replace(keywords[i - 1], keywords[i])
            # send request
            make_request(curl_command)
            time.sleep(0.2)


def with_timer():
    for curl_command in websites_with_timer:
        for i in range(len(keywords)):
            # look for the first keyword
            if 'KEYWORD' in curl_command:
                curl_command = curl_command.replace('KEYWORD', keywords[i])
            # change changed keyword
            else:
                curl_command = curl_command.replace(keywords[i - 1], keywords[i])
            # send request
            make_request(curl_command)
            time.sleep(40)


def open_with_search_engine():
    for curl_command in search_engines:
        for i in range(len(search_engine_keyword)):
            # look for the first keyword
            if 'KEYWORD' in curl_command:
                curl_command = curl_command.replace('KEYWORD', search_engine_keyword[i])
            # change changed keyword
            else:
                curl_command = curl_command.replace(search_engine_keyword[i - 1], search_engine_keyword[i])
            # send request
            make_request(curl_command)
            time.sleep(40)


t1 = Thread(target=without_timer)
t2 = Thread(target=with_timer)
t3 = Thread(target=open_with_search_engine)
if __name__ == '__main__':
    t1.start()
    t2.start()
    t3.start()

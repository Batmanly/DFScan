import re

import tldextract

from parse_curl import websites_with_timer, websites_without_timer

keywords = []
search_engine_keyword = []
search_engine_domain_tld = []
# open keyword file and read content , content doesn't matter what it is , it will get  the domain name from url etc, or we can directly give keyword
with open('keyword.txt', 'r') as f:
    read_keyword = f.readlines()

for i in read_keyword:
    # extract domain name from the readed content and append it to keywords list , for use in the main.py
    if len(i) <= 7:
        search_engine_keyword.append(i)
    else:
        keywords.append(tldextract.extract(i).domain)
    # print("keyword for looking:",tldextract.extract(i).domain)
for i in websites_without_timer:
    t = re.findall(r'(?P<url>https?://[^\s]+[^\s]+)', i)[1].replace('https://', '').replace('http://', '').strip('\'')
    search_engine_domain_tld.append(t)
for i in websites_with_timer:
    t = re.findall(r'(?P<url>https?://[^\s]+[^\s]+)', i)[1].replace('https://', '').replace('http://', '').strip('\'')
    search_engine_domain_tld.append(t)
if __name__ == '__main__':
    print(keywords)
    print(search_engine_keyword)
    print(search_engine_domain_tld)

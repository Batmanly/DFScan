import tldextract

keywords = []
search_engine_keyword = []
# open keyword file and read content , content doesn't matter what it is , it will get  the domain name from url etc, or we can directly give keyword
with open('keyword.txt', 'r') as f:
    read_keyword = f.readlines()

for i in read_keyword:
    # extract domain name from the readed content and append it to keywords list , for use in the main.py
    if len(i) <= 6:
        search_engine_keyword.append(i)
    else:
        keywords.append(tldextract.extract(i).domain)
    # print("keyword for looking:",tldextract.extract(i).domain)

# Darkweb Forum && Keyword Scanner
It's a simple tool that can be used to scan the Darkweb for keywords.

#### Feautures
- Tor proxy support
- Multiple threads as length of your forum count
- Scanning for multiple keywords
- Scanning for multiple forums

#### How to use:
```text
Clone Repository: git clone https://github.com/Batmanly/DFScan
Install Dependencies: pip install -r requirements.txt
Run: python3 main.py
```
First of all You must already be already logged forum , url will open direclty to your default browser.
For usage, you must add your forum CURL Request in the folder as the shown in the example.

Search KEYWORD must be KEYWORD in the CURL Request.Be Carefully !!!
Open Chrome Tools with F12 and click the "Network" tab. Than Copy Post Request as curl/bash.
![](keyword.gif)
Than add this curl to inside the folder. as a with name you want.
You can add keyword,url etc. that you want to search in to keyword.txt file.
I made some optimization for so many tabs, you can add the empty search keyword to false.txt , than you can escape unuseful tabs.
Sometimes page return 403 even it's empty, that time url will open again because i can't check the page.
i also won't open that page return 400 status code it's also mean empty page.
For use with Tor relay you must start tor service.

### Folders
There is three folders in the project.
For each folder there is one thread is working , in the timers folder forum has to wait for 40 second for each new tab, because some websites has limit for scan keyword.
![](folder.gif)
if your forum doesn't have limit for scanning you must and untimers folder your curl request.
you can add search engine in the search engine folder with dork and keyword. some forum doesn't let you scan 3-4 lenght keyword , so you can use google dork for this keywords.

![](with_dork.gif)
as like before add curl command to in the search engine folder with the name you want.

### For Tor Service , i use this.
```text
For Windows and Mac: https://github.com/jeremy-jr-benthum/onion-browser-button/releases you can use this.
```




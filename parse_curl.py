import glob

websites_without_timer = []
websites_with_timer = []
search_engines = []
# read all files in the directory
read_websites_untimers = glob.glob('untimers/*')
read_websites_with_timers = glob.glob('timers/*')
read_search_engines = glob.glob('search_engine/*')

# read all content of files in the directory
for i in read_websites_untimers:
    with open(i, 'r') as f:
        curl_command = f.read().replace('\n', '').replace('\ ', '')
        websites_without_timer.append(curl_command)
# read all content of files in the directory
for i in read_websites_with_timers:
    with open(i, 'r') as f:
        curl_command = f.read().replace('\n', '').replace('\ ', '')
        websites_with_timer.append(curl_command)
for i in read_search_engines:
    with open(i, 'r') as f:
        curl_command = f.read().replace('\n', '').replace('\ ', '')
        search_engines.append(curl_command)

if __name__ == '__main__':
    # write content of files in the directory
    print(websites_without_timer)
    print(websites_with_timer)
    print(search_engines)

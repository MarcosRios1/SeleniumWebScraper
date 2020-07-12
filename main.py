import chromeBot

def main():
    cbot = chromeBot.chromeBot()
    driver = cbot.search_url('http://ebay.com')
    cbot.send_search(driver, 'laptop')

main()
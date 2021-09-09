# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from time import sleep
# from selenium.webdriver.common import desired_capabilities, proxy
# from selenium.webdriver.common.proxy import Proxy, ProxyType

from bestBuyDrop import bestBuyDriver

# def ipProxy():
#     proxIPPort = '9411:631a:969f:ac25:c6a8:8015:f257:7630'
#     # driver.get('https://whatismyipaddress.com')
#     proxy = Proxy()
#     proxy.proxy_type = ProxyType.MANUAL
#     proxy.http_proxy = proxIPPort
#     proxy.ssl_proxy = proxIPPort

#     capabilities = webdriver.DesiredCapabilities.CHROME
#     proxy.add_to_capabilities(capabilities)

#     driver = webdriver.Chrome(PATH,desired_capabilities=capabilities)

#     driver.get('https://whatismyipaddress.com')
    
#     sleep(10)
#     driver.quit()

def main():
    while (1): #infinite loop
        # check best buy site to see item is in stock
        
        checkOut = bestBuyDriver().addToCart()

        if checkOut == True: 
            # TODO: need to be able to fill out checkout forms as user or guest
            # TODO: add inputs for dummy credit card info
            # TODO: be able to check multiple sites
            # TODO: maybe spoof IP 
            bestBuyDriver().fillForm()
            bestBuyDriver().placeOrder()
            pass
        
        # sleep(1) #add break point to pause


if __name__ == "__main__":
    main()
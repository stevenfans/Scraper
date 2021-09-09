# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from time import sleep
# from selenium.webdriver.common import desired_capabilities, proxy
# from selenium.webdriver.common.proxy import Proxy, ProxyType

from bestBuyDrop import bestBuyDriver

# PATH = "D:\VS Code\Scraper\chromedriver.exe"

# # driver.get("https://drsquatch.com/collections/bar-soaps");
# # driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402") #3060ti
# # driver.get("https://techwithtim.net")
# # chrome_options = Options() 
# # chrome_options.add_experimental_option("detach", True)
# # driver = webdriver.Chrome(options=chrome_options)

# class bestBuyDriver(object):

#     def addToCart():
#         buyButton = False
#         driver = webdriver.Chrome(PATH)

#         driver.get("https://www.bestbuy.com/site/bose-headphones-700-wireless-noise-cancelling-over-the-ear-headphones-triple-black/6332173.p?skuId=6332173")

#         while buyButton is False: 

#             try:
#                 # check if the item is sold out
#                 addToCart = driver.find_element_by_class_name('c-button-disabled')
#                 print('Sold Out')
#                 sleep(2)
#                 driver.refresh()
            
#             except:
#                 # if item is not sold out then add to cart
#                 addToCart = driver.find_element_by_class_name('add-to-cart-button')
#                 driver.execute_script("arguments[0].click();", addToCart)

#                 # Go to cart
#                 goToCart = driver.find_element_by_class_name('cart-label')
#                 driver.execute_script("arguments[0].click();", goToCart)

#                 # Check out the item
#                 # checkout = driver.find_element_by_xpath('//*[@id="cartApp"]/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[4]/div/div[1]/button')
#                 # checkout = driver.find_element_by_class_name('btn-primary')
#                 checkout = driver.find_element_by_css_selector('.btn.btn-lg.btn-block.btn-primary')
#                 checkout.click()
#                 # item is added to cart and is ready to check out
#                 buyButton = True
#                 sleep(2)
            
#         return buyButton

#     def fillForm():
#         # check if logged in 
#         # 

    
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
            pass
        
        # sleep(1) #add break point to pause


if __name__ == "__main__":
    main()
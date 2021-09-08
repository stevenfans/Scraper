from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

PATH = "D:\VS Code\Scraper\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# driver.get("https://drsquatch.com/collections/bar-soaps");
driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402")
# driver.get("https://www.bestbuy.com/site/bose-headphones-700-wireless-noise-cancelling-over-the-ear-headphones-triple-black/6332173.p?skuId=6332173")
# driver.get("https://techwithtim.net")
print(driver.title)
chrome_options = Options() 
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)

def bestBuyAddToCart():
    buyButton = False

    while buyButton is False: 

        try:
            # check if the item is sold out
            addToCart = driver.find_element_by_class_name('c-button-disabled')
            print('Sold Out')
            sleep(2)
            driver.refresh()
        
        except:
            # if item is not sold out then add to cart
            addToCart = driver.find_element_by_class_name('add-to-cart-button')
            driver.execute_script("arguments[0].click();", addToCart)

            # Go to cart
            goToCart = driver.find_element_by_class_name('cart-label')
            driver.execute_script("arguments[0].click();", goToCart)

            # Check out the item
            # checkout = driver.find_element_by_xpath('//*[@id="cartApp"]/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[4]/div/div[1]/button')
            checkout = driver.find_element_by_class_name('btn-primary')
            checkout.click()
            # item is added to cart and is ready to check out
            buyButton = True
            sleep(2)

def main():
    while (1): #infinite loop
        # check best buy site to see item is in stock
        bestBuyAddToCart()
        sleep(1) #add break point to pause


if __name__ == "__main__":
    main()
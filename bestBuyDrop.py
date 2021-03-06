from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common import desired_capabilities, proxy
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import NoSuchElementException        

PATH = "D:\VS Code\Scraper\chromedriver.exe"        

driver = webdriver.Chrome(PATH)
driver.get("https://www.bestbuy.com/site/microsoft-controller-for-xbox-series-x-xbox-series-s-and-xbox-one-latest-model-pulse-red/6448932.p?skuId=6448932")

# driver.get("https://drsquatch.com/collections/bar-soaps");
# driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402") #3060ti
# driver.get("https://techwithtim.net")
# chrome_options = Options() 
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)

class bestBuyDriver():

    def addToCart(self):
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
                
                sleep(1)

                # Check out the item
                # checkout = driver.find_element_by_xpath('//*[@id="cartApp"]/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[4]/div/div[1]/button')
                # checkout = driver.find_element_by_class_name('btn-primary')
                try: 
                    checkout = driver.find_element_by_css_selector('.btn.btn-lg.btn-block.btn-primary')
                except:
                    checkout = driver.find_element_by_class_name('checkout-buttons__checkout')
                try:
                    checkout = driver.find_element_by_xpath('//*[@id="cartApp"]/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[4]/div/div[1]')
                except:
                    pass
                    

                checkout.click()
                # item is added to cart and is ready to check out
                buyButton = True
                sleep(2)
            
        return buyButton

    def fillForm(self):

        # check if the guest sign is on webpage

        # email_in = input("type email: ")
        email_in = 'jajajackfrost96@gmail.com'
        pword_in = input("type pword: ")

        # check if logged in 
        email = driver.find_element_by_id('fld-e')
        pword = driver.find_element_by_id('fld-p1')

        # send information to form
        email.send_keys(email_in)
        pword.send_keys(pword_in)
  
        # sign in
        try: 
            signIn = driver.find_element_by_css_selector('.c-button.c-button-secondary.c-button-lg.c-button-block.c-button-icon.c-button-icon-leading.cia-form__controls__submit')
        except:
            signIn = driver.find_element_by_class_name('cia-form__controls')

        signIn.click()

        sleep(2)

        # Check current URL
        # If URL is fast-track then it means you don't need to enter Private Info
        fulfillment = driver.current_url
        print(fulfillment)

        if 'fulfillment' in fulfillment:

            # Enter User Private Info
            firstName  = 'Steven'
            lastName   = 'Phan'
            street     = '3634534'
            city       = 'asdf'
            zipCode    = '90230'
            
            sleep(10)

            try: 
                inFirstName = driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_1227.firstName"]')
            except Exception:
                pass
            try: 
                inFirstName = driver.find_element_by_id("consolidatedAddresses.ui_address_2.firstName")
            except Exception:
                pass

            try: 
                inLastName = driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_1227.lastName"]')
            except Exception:
                pass
            try: 
                inLastName = driver.find_element_by_id("consolidatedAddresses.ui_address_2.lastName")
            except Exception:
                pass

            try: 
                inStreet = driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_1227.street"]')
            except Exception:
                pass
            try: 
                inStreet = driver.find_element_by_id("consolidatedAddresses.ui_address_1227.street")
            except Exception:
                pass

            try: 
                inCity = driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_1227.city"]')
            except Exception:
                pass
            try: 
                inCity = driver.find_element_by_id("consolidatedAddresses.ui_address_1227.city")
            except Exception:
                pass


            inFirstName.send_keys(firstName)       
            inLastName.send_keys(lastName)
            inStreet.send_keys(street)
            inCity.send_keys(city)

        # input cvc
        # inputCVC = driver.find_element_by_id('cvv')
        inputCVC = driver.find_element_by_xpath('//*[@id="cvv"]')
        inputCVC.send_keys('000')

    def placeOrder(self): 
        try: 
            po = driver.find_element_by_xpath('//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[2]/div/div[4]/div[3]/div/div[2]/button')
        except:
            pass

        try:
            po = driver.find_element_by_css_selector('.btn.btn-lg.btn-block.btn-primary.button__fast-track')
        except Exception:
            pass

        try: 
            po = driver.find_element_by_class_name('payment__order-summary')
        except Exception:
            pass

        po.click()    
        pass

    def css_exists(css):
        
        try:
            driver.find_element_by_class_name(css)
        except NoSuchElementException:
            return False

        return True

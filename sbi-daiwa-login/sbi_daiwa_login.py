from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

# def main():
driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://www.sbisec.co.jp/ETGate'
driver.get(url)
sleep(3)

link_url_toushin = driver.find_element_by_css_selector('#navi01P > ul > li:nth-child(5) > a').get_attribute('href')
driver.get(link_url_toushin)

driver2 = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://www.sbisec.co.jp/ETGate'
driver2.get(url)
sleep(3)

link_url_fx = driver2.find_element_by_css_selector('#navi01P > ul > li:nth-child(7) > a').get_attribute('href')
driver2.get(link_url_fx)

driver3 = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://www.daiwa.jp/'
driver3.get(url)
sleep(3)

link_url_toushin2 = driver3.find_element_by_xpath('//a[text()="投資信託"]').get_attribute('href')
driver3.get(link_url_toushin2)

# if __name__ == "__main__":
#     main()

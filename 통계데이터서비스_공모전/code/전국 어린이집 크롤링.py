from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.daycarekorea.com/child/daycare_list.php?pagenum=1&addcode=&gubun=&searchkeyword=&orderby=&cnum=")

import time
from selenium import webdriver

driver = webdriver.Chrome('/usr/bin/chromedriver')


driver.get("https://dailyhoroscopee.com/admin/")
username = driver.find_element_by_id("id_username")
username.send_keys("user")
username = driver.find_element_by_id("id_password")
username.send_keys("pass")
driver.find_element_by_xpath('//*[@id="login-form"]/div[3]').click()



d = {"aries":1 , "taurus":2 , "gemini":3 ,"cancer":4,"leo":5,"virgo":6,"libra":7,'scorpio':8,'sagittarius':9,"capricorn":10,"aquarius":11,'pisces':12}
for key, value in d.items():
    driver.get(f'https://www.ganeshaspeaks.com/horoscopes/daily-love-and-relationship-horoscope/{key}/')
    content = driver.find_element_by_xpath('//*[@id="daily"]/div/div[1]/div[2]/p').text
    time.sleep(4)
    driver.get(f"https://dailyhoroscopee.com/admin/my_site/signslist/{value}/change/")
    Daily = driver.find_element_by_id("id_Love")
    Daily.clear()
    Daily.send_keys(content)
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="signslist_form"]/div/div/input[1]').click()
    time.sleep(4)


    driver.get(f'https://www.ganeshaspeaks.com/horoscopes/daily-money-and-finance-horoscope/{key}/')
    finance_text = driver.find_element_by_xpath('//*[@id="daily"]/div/div[1]/div[2]/p').text
    driver.get(f"https://dailyhoroscopee.com/admin/my_site/signslist/{value}/change/")
    finance = driver.find_element_by_id("id_Finance")
    finance.clear()
    finance.send_keys(finance_text)
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="signslist_form"]/div/div/input[1]').click()
    time.sleep(4)

    driver.get(f'https://www.ganeshaspeaks.com/horoscopes/daily-health-and-well-being-horoscope/{key}/')
    daily_text = driver.find_element_by_xpath('//*[@id="daily"]/div/div[1]/div[2]/p').text
    driver.get(f"https://dailyhoroscopee.com/admin/my_site/signslist/{value}/change/")
    daily = driver.find_element_by_id("id_Daily")
    daily.clear()
    daily.send_keys(daily_text)
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="signslist_form"]/div/div/input[1]').click()
    time.sleep(4)



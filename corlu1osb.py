from selenium import webdriver
from selenium.webdriver.common.by import By
import time, csv

datas = []

driver = webdriver.Safari()
# driver = webdriver.Chrome()
# driver = webdriver.Firefox()

url = 'https://www.corlu1osb.org.tr/tr/firmalarimiz/'
driver.get(url)
driver.maximize_window()

datas.append(['Emails'])

time.sleep(2)

mailler = driver.find_elements(By.XPATH, '//a[contains(@class, "list-group-item display-flex-xxl align-items-center-xxl")]')

for mail in mailler:
        if mail.get_attribute('href').startswith("mail") == True:
            e_mail = str(mail.get_attribute('href'))[7:]
            datas.append([e_mail])
            print(e_mail)
            

dosya_yolu = "corlu1osb.csv"

with open(dosya_yolu, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for data in datas:
        writer.writerow(data)

driver.close()

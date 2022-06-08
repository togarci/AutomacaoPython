from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from src.Export import Export


class SeleniumMode:

    def getAmazon(self, keyWordSearch):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.amazon.com.br/')
        data = { 'Titulo': [], 'Valor': [] }
        
        searchInput = driver.find_element(by=By.CSS_SELECTOR, value='#twotabsearchtextbox')
        searchInput.send_keys(keyWordSearch)

        submitInput = driver.find_element(by=By.CSS_SELECTOR, value='#nav-search-submit-button')
        submitInput.click()

        dataItems = driver.find_elements(by=By.CSS_SELECTOR, value='.s-card-container')

        for item in dataItems:
            title = item.find_element(by=By.CSS_SELECTOR, value='.a-size-base-plus.a-color-base.a-text-normal')

            try:
                value = item.find_element(by=By.CSS_SELECTOR, value='.a-offscreen')
                value = value.get_attribute('innerHTML')
                value = value.replace('&nbsp', '').replace(';', ':')

            except:
                value = ''

            data['Titulo'].append(title.text)
            data['Valor'].append(value)

        
        excelExport = Export()
        excelExport.createExcel(data)


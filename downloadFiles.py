# -*- coding: utf-8 -*-
import os
import re
import time
import unittest

import requests
from selenium import webdriver
from selenium.common.exceptions import (NoAlertPresentException,
                                        NoSuchElementException)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.getCredentials()
        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_settings.popups": 0,
                 "download.default_directory": dir_path, # IMPORTANT - ENDING SLASH V IMPORTANT
                 "directory_upgrade": True}
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=options)

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://siteseguro.inatel.br/PortalAcademico/WebLogin.aspx?ReturnUrl=%2fPortalacademico%2f"
    
    def getCredentials(self):
        self.username = input("Matricula: ")
        self.password = input("Senha: ")

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get(self.base_url)
        Select(driver.find_element_by_id("ctl00_Corpo_TabAcessoLogin_TabAluno_LogOn_dropSubCurso")).select_by_visible_text(u"Engenharia da Computação")
        
        ## Login
        driver.find_element_by_id("ctl00_Corpo_TabAcessoLogin_TabAluno_LogOn_dropSubCurso").click()
        driver.find_element_by_id("ctl00_Corpo_TabAcessoLogin_TabAluno_LogOn_tbMatricula").clear()
        driver.find_element_by_id("ctl00_Corpo_TabAcessoLogin_TabAluno_LogOn_tbMatricula").send_keys(self.username)
        driver.find_element_by_id("ctl00_Corpo_TabAcessoLogin_TabAluno_LogOn_Password").clear()
        driver.find_element_by_id("ctl00_Corpo_TabAcessoLogin_TabAluno_LogOn_Password").send_keys(self.password)
        driver.find_element_by_id("ctl00_Corpo_TabAcessoLogin_TabAluno_LogOn_LoginButton").click()
        
        
        ## Material de Aula
        driver.find_element_by_id("ctl00_Corpo_HyperLink22").click()
        # driver.find_element_by_xpath("//a[@id='ctl00_Corpo_UCMaterialAulaAluno1_tvwMaterialt1i']/img").click()
        id_base = "ctl00_Corpo_UCMaterialAulaAluno1_GridDados_ctl{0:0>2}_HyperLink2"
        urls = []
        for index in range(2,21):
            print("{0:0>2}".format(index))
            try:
                element_id = id_base.format(index)
                driver.find_element_by_id(element_id).click()
                element = driver.find_element_by_id(element_id)
                if element != None:
                    url = element.get_attribute("href")
                    urls.append(url)
                    print(url)
            except:
                print("Couldn't find element with id {}".format(element_id))

if __name__ == "__main__":
    unittest.main()

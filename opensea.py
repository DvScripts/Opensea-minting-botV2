import time
import os
import pathlib
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


def mint(values, isWindows):
    
    def selectWallet():
        print("Accepting terms")
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//a[@class='sc-1pie21o-0 elyzfO sc-1xf18x6-0 sc-glfma3-0 hiIVBZ eqgvEc']")))
        continue__ = driver.find_element(By.XPATH, "//a[@class='sc-1pie21o-0 elyzfO sc-1xf18x6-0 sc-glfma3-0 hiIVBZ eqgvEc']").click()
        print("Finished accepting")

    def recaptcha(site_key):
        print('ReCaptcha sitekey is ' +site_key)
        page_url = values[0]
        method = "userrecaptcha"
        key = values[2]
        url = "http://2captcha.com/in.php?key={}&method={}&googlekey={}&pageurl={}".format(key,method,site_key,page_url)
        response = requests.get(url)
        if response.text[0:2] != 'OK':
            quit('Service error. Error code:' + response.text)
        captcha_id = response.text[3:]
        token_url = "http://2captcha.com/res.php?key={}&action=get&id={}".format(key,captcha_id)
        while True:
            time.sleep(1)
            response = requests.get(token_url)
            print(response.text)
            if response.text[0:2] == 'OK':
                break

        captha_results = response.text[3:]
        driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="";')
        driver.execute_script("""document.querySelector('[name="g-recaptcha-response"]').innerHTML='{}'""".format(captha_results))
        driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="none";')
        driver.execute_script("___grecaptcha_cfg.clients[0].X.X.callback(arguments[0]);",captha_results)
        accept()

    def accept():
        print('Accepting in phantom')
        original_window = driver.current_window_handle
        WebDriverWait(driver, 60).until(EC.number_of_windows_to_be(3))
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        WebDriverWait(driver, 60).until(EC.presence_of_element_located(
            (By.XPATH, "//button[contains(text(), 'Approve')]")))
        approve = driver.find_element(
            By.XPATH, "//button[contains(text(), 'Approve')]")
        approve.click()

    def yorn():
        if values[2] != '':
            print('2captcha')
            avaitMint()
            accept()
        else:
            print('Manual captcha')
            avaitMintManual()

    def avaitMintManual():
        print("Waiting for Mint")
        time.sleep(1)
        element = driver.find_element(By.XPATH, "//button[contains(text(),'Mint')]")
        prop = element.get_property('disabled')
        if prop == False :
            element.click()
            time.sleep(20)
        else:
            print("Still waiting")
            avaitMintManual()

    def avaitMint():
        print("Waiting for Mint")
        time.sleep(1)
        element = driver.find_element(By.XPATH, "//button[contains(text(),'Mint')]")
        prop = element.get_property('disabled')
        if prop == False :
            print('We can mint now')
            element.click()
            time.sleep(1)
            site_key = driver.execute_script("return window.__sidecar_config__.recaptchaSiteKey")
            recaptcha(site_key)
        else:
            print("Still waiting")
            avaitMint()

    def initWallet():
        print("Status - Initializing wallet")
        # add wallet to chrome

        if driver.current_url != "chrome-extension://gfoeaaijjjdneafnjccohndgdljjoemp/onboarding.html":
            driver.switch_to.window(driver.window_handles[0])
        if driver.current_url != "chrome-extension://gfoeaaijjjdneafnjccohndgdljjoemp/onboarding.html":
            driver.switch_to.window(driver.window_handles[1])

        print("Event - switch window")
        WebDriverWait(driver, 120).until(EC.presence_of_element_located(
            (By.XPATH, "//button[contains(text(),'Use Secret Recovery Phrase')]")))
        recovery_phrase = driver.find_element(
            By.XPATH, "//button[contains(text(),'Use Secret Recovery Phrase')]").click()
        WebDriverWait(driver, 120).until(EC.presence_of_element_located(
            (By.XPATH, "//textarea[@placeholder='Secret phrase']")))
        text_area = driver.find_element(
            By.XPATH, "//textarea[@placeholder='Secret phrase']").send_keys(values[1])
        import_btn = driver.find_element(
            By.XPATH, "//button[@class='sc-bdfBQB bzlPNH']").click()
        WebDriverWait(driver, 120).until(EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Password']")))
        password1 = driver.find_element(
            By.XPATH, "//input[@placeholder='Password']").send_keys(values[2])
        password2 = driver.find_element(
            By.XPATH, "//input[@placeholder='Confirm Password']").send_keys(values[2])
        check_box = driver.find_element(
            By.XPATH, "//input[@type='checkbox']").click()
        submit = driver.find_element(
            By.XPATH, "//button[@type='submit']").click()
        WebDriverWait(driver, 120).until(EC.presence_of_element_located(
            (By.XPATH, "//button[contains(text(),'Continue')]")))
        continue_ = driver.find_element(
            By.XPATH, "//button[contains(text(),'Continue')]")
        driver.execute_script("arguments[0].click();", continue_)
        WebDriverWait(driver, 120).until(EC.presence_of_element_located(
            (By.XPATH, "//button[contains(text(),'Finish')]")))
        finish = driver.find_element(
            By.XPATH, "//button[contains(text(),'Finish')]")
        driver.execute_script("arguments[0].click();", finish)
        print("Status - Finished Initializing wallet")
        driver.switch_to.window(driver.window_handles[0])
        print("Finished Initializing wallet")



    options = Options()

    options.add_extension("Phantom.crx")

    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    os.environ['WDM8LOCAL'] = '1'


    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    print("Found chrome driver")
    



    driver.get(values[0])

    main_window = initWallet()

    selectWallet()

    yorn()

    print("Minting Finished")

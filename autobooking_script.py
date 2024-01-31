from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
c


def login_to_unisport():
    # Path to your Chrome WebDriver
    path_to_webdriver = '/Users/naveenmalla/Documents/Code/Personal/UniSport/chromedriver_mac_arm64/chromedriver'

    # Define Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Initialize the Chrome driver
    service = Service(executable_path=path_to_webdriver)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # URL of the login page
    login_url = 'https://ahs.uni-trier.de/login_neu.php#6'

    # Open the browser and navigate to the login page
    driver = webdriver.Chrome(path_to_webdriver)
    driver.get(login_url)

    # Allow some time for the page to load
    time.sleep(2)

    # Find the email and password fields and fill them in
    email_field = driver.find_element_by_xpath('//*[@id="login"]/form[1]/table/tbody/tr[1]/td[2]/input')
    email_field.send_keys('s4namall@uni-trier.de')  # Replace with your email

    password_field = driver.find_element_by_xpath('//*[@id="passw"]')
    password_field.send_keys('j?U9_eVnXkPra2')  # Replace with your password

    # Find the login button and click it
    login_button = driver.find_element_by_xpath('//*[@id="login"]/form[1]/input')
    login_button.click()

    # Allow some time for any post-login navigation
    time.sleep(5)

    # Close the browser
    driver.quit()

if __name__ == '__main__':
    login_to_unisport()

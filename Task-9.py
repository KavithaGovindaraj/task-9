from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time

# Path to the Edge WebDriver executable
driver_path = 'C:\\Users\\PREMA\\msedgedriver.exe'  # Update this with the actual path

# Set up Edge options
options = Options()
options.use_chromium = True

# Set up the Edge WebDriver with the Service object
service = Service(executable_path=driver_path)
driver = webdriver.Edge(service=service, options=options)

try:
    # Open the URL
    driver.get("https://www.saucedemo.com/")

    # Login using provided credentials
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    # Wait for a few seconds to ensure the page loads
    time.sleep(3)

    # Get the title of the webpage
    title = driver.title
    print(f"Title of the webpage: {title}")

    # Get the current URL of the webpage
    current_url = driver.current_url
    print(f"Current URL of the webpage: {current_url}")

    # Extract the entire contents of the webpage
    page_source = driver.page_source

    # Save the contents to a text file
    with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
        file.write(page_source)

    print("Webpage content has been saved to 'Webpage_task_11.txt'")

finally:
    # Close the WebDriver
    driver.quit()
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_scores_service(url):
    try:
        # Initialize the Selenium WebDriver for Safari
        driver = webdriver.Safari()

        # Open the specified URL
        driver.get(url)

        # Wait for a few seconds to allow the page to load
        time.sleep(5)

        # Find the score element by its XPath
        score_element = driver.find_element(By.XPATH, "//h1[contains(text(), 'The global score is')]")

        # Check if the score element is found
        is_element_found = score_element is not None

        return is_element_found

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

    finally:
        driver.quit()  # Close the browser window

def main_function():
    url = 'http://127.0.0.1:5000'
    if test_scores_service(url):
        print("Tests passed!")
        return 0
    else:
        print("Tests failed.")
        return -1

if __name__ == "__main__":
    exit_code = main_function()
    os._exit(exit_code)

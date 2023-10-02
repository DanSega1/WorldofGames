import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_scores_service(url):
    try:
        # Initialize the Selenium WebDriver for Safari
        driver = webdriver.Safari()

        # Open the specified URL
        driver.get(url)

        # Wait for a few seconds to allow the page to load
        time.sleep(10)

        # Find the score element by its ID
        score_element = driver.find_element_by_id("score")

        # Get the text content of the score element and convert it to an integer
        score = int(score_element.text)

        # Check if the score is between 1 and 1000
        is_valid_score = 1 <= score <= 1000

        return is_valid_score

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

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

PROTOCOL: str = "http://"
HOST: str = "127.0.0.1"
PORT: str = ":5000"
TEST_URL: str = f"{PROTOCOL}{HOST}{PORT}"

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get(TEST_URL)
    yield driver
    driver.quit()

# UI Test-1: Check main page
def test_open_main_page(driver):
    page_header: str = driver.find_element(By.TAG_NAME, "h1").text
    assert page_header == "Welcome to Bank Identifier!"

# UI Test-2: Check bank brands
@pytest.mark.parametrize("bin_number, expected_bank_brand", [
    ("516793", "MASTERCARD"),
    ("999999", "None"),
    ("0", "Invalid BIN"),
])
def test_check_bank_brand_via_bin(driver, bin_number, expected_bank_brand):
    #bin_number: str = "548230"
    #expected_bank_brand: str = "MASTERCARD"

    input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "BIN")))
    input_field.send_keys(bin_number)
    driver.find_element(By.ID,"IDENTIFY").click()
    identify_result: str = driver.find_element(By.TAG_NAME, "body").text

    assert expected_bank_brand in identify_result
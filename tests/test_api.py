import requests
import pytest
import time

PROTOCOL: str = "http://"
HOST: str = "127.0.0.1"
PORT: str = ":5000"
ENDPOINT: str = "/identify"
TEST_URL: str = f"{PROTOCOL}{HOST}{PORT}"
SUCCESS_STATUS_CODE: int = 200
CUSTOM_SLEEP_WAITER: int = 3

# API Test-1: Check bank brands
@pytest.mark.parametrize("bin_number, expected_bank_brand", [
    ("?BIN=19627", "Unknown bank"),
    ("?BIN=45719942", "DIBA BANK"),
    ("?BIN=2147483647", "Unknown bank"),
    ("?BIN=0", "Invalid BIN"),
    ("?BIN=-1", "Invalid BIN"),
    ("?BIN=abc", "Invalid BIN"),
    ("?BIN=#$&", "Invalid BIN"),
])
def test_response_bank_brand_via_bin(bin_number, expected_bank_brand):
    response = requests.get(f"{TEST_URL}{ENDPOINT}{bin_number}")

    assert response.status_code == SUCCESS_STATUS_CODE
    assert expected_bank_brand in response.text

# API Test-2: Check response time
def test_response_estimate_time():
    start_time = time.time()
    requests.get(f"{TEST_URL}")
    end_time = time.time()
    estimate_time = end_time - start_time
    assert int(estimate_time) <= CUSTOM_SLEEP_WAITER
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    opts = Options()
    if os.getenv("CI"):
        opts.add_argument("--headless=new")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1280,800")
    d = webdriver.Chrome(options=opts)
    yield d
    d.quit()
import os.path
from pathlib import Path
from selene import browser
import pytest

PROJECT_ROOT_PATH = os.path.dirname(__file__)
RESOURCE_PATH = os.path.abspath(os.path.join(PROJECT_ROOT_PATH, 'resources'))

@pytest.fixture(scope="module", autouse=True)
def set_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'

    yield


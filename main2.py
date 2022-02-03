from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest
import sys
import unittest

def get_channel_results():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.youtube.com/results?search_query=mojang')

    title = driver.find_element_by_css_selector('#info #text').text
    link = driver.find_element_by_css_selector('#main-link').get_attribute('href')
    subs = driver.find_element_by_css_selector('#subscribers').text
    video_count = driver.find_element_by_css_selector('#video-count').text
    desc = driver.find_element_by_css_selector('#description').text
    print(f'{title}\n{link}\n{subs}\n{video_count}\n{desc}')

    get_channel_results()

expectedTitle = "title"
actualTitle = get_channel_results

def checkTitle():
    assert expectedTitle == actualTitle

def test_a():
    checkTitle()





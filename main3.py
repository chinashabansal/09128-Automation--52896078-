import pytest
import unittest
import sys
import main2

expectedTitle = get_channel_results.title
actualTitle = driver.title
def checkTitle():
    assert expectedTitle == actualTitle

def test_a():
    checkTitle()

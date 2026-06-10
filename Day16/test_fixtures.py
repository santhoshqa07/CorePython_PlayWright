
#Fixture: reusable function

import pytest

@pytest.fixture
def setup():
    print("this is my browser setup")

def test_one(setup):
    print("this is my test one")

def test_two(setup):
    print("this is my test two")

def test_three(setup):
    print("this is my test three")



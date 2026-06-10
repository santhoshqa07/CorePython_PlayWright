import pytest

@pytest.fixture

def setup():
    print("This is the setup browser")
    yield
    print("This is the teardown browser")





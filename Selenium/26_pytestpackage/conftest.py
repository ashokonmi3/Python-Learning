import pytest

@pytest.yield_fixture()
def setUp():
    print(" ")
    print("Running method level setUp")
    yield
    print("Running method level tearDown")

@pytest.yield_fixture(scope="module")
def oneTimeSetUp():
    print(" ")
    print("Running conftest demo one time setUp")
    yield
    
    print("Running conftest demo one time tearDown")
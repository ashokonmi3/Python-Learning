import pytest
@pytest.yield_fixture()
def setUp():
    print("   ")
    print("Running demo2 setUp")
    yield
    print("   ")
    print("Running demo2 tearDown")

def test_demo2_methodA(setUp):
    print("   ")

    print("Running demo2 method A")

def test_demo2_methodB(setUp):
    print("   ")

    print("Running demo2 method B")
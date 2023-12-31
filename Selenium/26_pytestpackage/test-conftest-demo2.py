import pytest

def test_demo2_methodA(setUp):
    print("Running conftest demo2 method A")

def test_demo3_methodB(setUp):
    print("Running conftest demo2 method B")
    
# import pytest

# def test_demo2_methodA(oneTimeSetUp, setUp):
#     print("Running conftest demo2 method A")

# def test_demo3_methodB(oneTimeSetUp, setUp):
#     print("Running conftest demo2 method B"
import pytest

# def test_demo1_methodA(setUp):
#     print("Running conftest demo1 method A")

# def test_demo1_methodB(setUp):
#     print("Running conftest demo1 method B")
    
import pytest

def test_demo1_methodA(oneTimeSetUp, setUp):
    print("Running conftest demo1 method A")

def test_demo1_methodB(oneTimeSetUp, setUp):
    print("Running conftest demo1 method B")
# import pytest

# def test_demo1_methodA():
#     print("Running demo1 method A")

# def test_demo1_methodB():
#     print("Running demo1 method B")
    
# import pytest
# @pytest.fixture()
# def setUp():
#     print(" ")
#     print("Running demo1 setUp")

# def test_demo1_methodA(setUp):# name of fixture will be passed in method it will make sure setup is run beore 
#     print(" " )
#     print("Running demo1 method A")

# def test_demo1_methodB(setUp):
#     print(" ")
#     print("Running demo1 method B")
    
# import pytest
# @pytest.fixture()
# def setUp():
#     print("Running demo1 setUp")

# def test_demo1_methodA(setUp):# name of fixture will be passed in method it will make sure setup is run beore 
#     print("Running demo1 method A")

# def test_demo1_methodB():
#     print("Running demo1 method B")  
 
import pytest
@pytest.fixture()
def s():
    print("Running demo1 setUp")

def test_demo1_methodA(s):# name of fixture will be passed in method it will make sure setup is run beore 
    print("Running demo1 method A")

def test_demo1_methodB(s):
    print("Running demo1 method B") 

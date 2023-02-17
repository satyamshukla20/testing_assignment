from calculator import *

def test_addition():
    assert addition(1,2)==3
    assert addition(0,0)!=1
    assert addition(5.1,1)==6.1

def test_subtraction():
    assert subtraction(1,2)==-1
    assert subtraction(0,0)!=1
    assert subtraction(5.1,1)==4.1

def test_multiplication():
    assert multiplication(1,2)==2
    assert multiplication(0,0)!=1
    assert multiplication(5.1,1)==5.1

def test_division():
    assert division(1,2)==0.5
    assert division(0,1)!=1
    assert division(5.1,1)==5.1
    assert division(1,0)=="denominator cannot be 0"

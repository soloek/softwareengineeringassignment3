import pytest
import math

from triangle import classify_triangle

def test_valid_triangle_zero_sides():
    assert classify_triangle(0,0,0)=="Invalid"
def test_valid_triangle_one_side_zero():
    assert classify_triangle(0,1,3)=="Invalid"
def test_valid_triangle_negative_sides():
    assert classify_triangle(-1,2,5)=="Invalid"
def test_valid_triangle_degenerate_boundary():
    assert classify_triangle(1,2,3)=="Invalid"

def test_equilateral_triangle():
    assert classify_triangle(3,3,3)=="Equilateral"

#said 3,3,3 changed to 6,6,4 to make it isoceles
def test_isosceles_triangle():
    assert classify_triangle(6,6,4)=="Isosceles"
 #said 1,1,some decimal number, changed to 1,1,(1*math.sqrt(2))
def test_right_isosceles_triangle():
    assert classify_triangle(1,1,(1*math.sqrt(2)))=="Right Isosceles"

def test_scalene_triangle():
    assert classify_triangle(10,15,20)=="Scalene"
def test_right_scalene_triangle():
    assert classify_triangle(3,4,5)=="Right Scalene"

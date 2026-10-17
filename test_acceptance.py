import pytest
import math
from triangle import classify_triangle

def test_valid_triangle():
    assert classify_triangle(3,4,5)!="Invalid"


def test_kind_of_triangle():
    assert classify_triangle(3,3,3)=="Equilateral"

def test_is_right_triangle():
    assert classify_triangle(1,1,1*(math.sqrt(2)))=="Right Isosceles"

#tbh the way this section is worded in the assignment is a bit confusing, hope this is good
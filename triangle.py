def is_valid_triangle(a, b, c) -> bool:
    """
    Checks if the inputted sides form a valid triangle.

    Parameters:
    a (float): Length of side a.    
    b (float): Length of side b.
    c (float): Length of side c.

    Returns:
    A boolean indicating whether the formed traingle is valid
    """
    if a<=0 or b<=0 or c<=0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    else:
        return True
def classify_triangle(a,b,c) -> str:
    """
    Classifies what kind of triangle would be made from three inputted side lengths

    Parameters:
    a(float): Length of side a.
    b(float): Length of side b.
    c( float): Length of side c.
    """
    triangletype = ""
    if is_valid_triangle(a,b,c) == False:
        triangletype="Invalid"
        return triangletype
    if a==b and b==c:
        triangletype="Equilateral"
        return triangletype
    if (a**a) + (b**b) == (c**c) or (a**a) + (c**c) == (b**b) or (b**b) + (c**c) == (a**a):
        triangletype+="Right "
    if a==b or b==c or a==c:
        triangletype+="Isosceles"
        return triangletype
    else:
        triangletype+="Scalene"
        return triangletype
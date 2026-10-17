def is_valid_triangle(a, b, c):
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
    
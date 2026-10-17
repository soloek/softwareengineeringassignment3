 This is my submission for the module 6 assignment. It is my take on the classic bit of figuring whether a triangle is valid and what kind of triangle it would be, which is an old way programmers have tried out testing when learning to code.
 
 It takes an input of three sides and determines if it is a valid triangle, and what kind of triangle it would be, including whether it is a right triangle.
 
 How to run:
 To run the tests just use pytest by typing pip install pytest in your terminal. You can also use requirements.txt to help you out.
 Python 3.15 was used to make this, but it should work fine with older versions.
 
 Equivalence classes:
 Invalid triangles, achieved by having all the sides at 0 or failing the triangle inequality
 Equilateral triangles, achieved by having all the sides be equal in length
 Isosceles triangles, achieved by having two sides equal in length
 Scalene triangles, achieved by not already being in an equivalence class
 
 Boundaries:
 The boundary where a triangle goes from being an isosceles triangle to being an equilateral triangle and vice versa
 The boundary where a triangle becomes invalid by having a side that is 0 in length, including negative numbers
 The boundary where a triangle goes from being an isosceles triangle to being a scalene triangle and vice versa
 The boundary where a triangle goes from being invalid to valid by no longer failing triangle inequality
 
 Copilot review log:
 |Test|Copilot-suggested?|Kept/edited/rejected|Why|
 |test_valid_triangle_zero_sides|Yes|Kept|N/A|
 |test_valid_triangle_one_side_zero|Yes|Kept|N/A|
 |test_valid_triangle_negative_sides|Yes|Kept|N/A|
 |test_valid_triangle_degenerate_boundary|Yes|Kept|N/A (The whole assertion thing was in my code, not with this)|
 |test_equilateral_triangle|Yes|Kept|N/A|
 |test_isoceles_triangle|Yes|Changed|It initially said 3,3,3 but I changed it to 6,6,4 which made it isoceles|
 |test_right_isoceles_triangle|Yes|Changed|The final number was a decimal, I changed it to get the number using math.sqrt|
 |test_scalene_triangle|Yes|Kept|N/A|
 |test_right_scalene|Yes|Kept|N/A|
 
 Acceptance criteria as used in test_acceptance.py:
 Criteria 1: Given an inputted triangle with 3 sides a,b,c, if at least one of the sides is 0, or fails the triangle inequality rule, the program should return false without causing an exception.
 Criteria 2: Given an inputted triangle with 3 sides a,b,c, if those sides pass the triangle inequality rule, the program should determine what kind of triangle (scalene, isoceles or equilateral) and output what kind of triangle the sides form.
 Criteria 3: Given an inputted triangle with sides a,b,c, if those sides satisfy the Pythagorean Theorem, and satisfy the triangle inequality rule, the program's output should have "Right" appeneded to what kind of triangle the sides would form
 
 AI Disclosure notice: I used Copilot's autocomplete feature to help fill out this program. The tests were also written using the help of Copilot autocomplete. I manually looked over the code written prior to accepting it, and used pytest to make sure the program and tests worked correctly.

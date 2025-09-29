print("Hello Python programming language")
# ex1_var=45
# print(ex1_var)
# ex1_var=4
# print(ex1_var)
# boo_value=True
# boo_value2=False
# ex2_var=-200
# decimal_value=0.56
# print(decimal_value)
# print(ex2_var)
# print(boo_value)
# print(boo_value2)
# Declaring some variables to understand different data types in Python.
# Understanding different types of expressions
add_two_numbers=5+5
print(add_two_numbers)
sub_two_numbers=50.98-5
print(sub_two_numbers)
mul_two_numbers=5*5.45
print(mul_two_numbers)
div_two_numbers=13//5 # Floor division
print(div_two_numbers)
div_two_numbers=13/5
print(div_two_numbers)
exponential_factor=4**2
print(exponential_factor)
modulo_two_numbers=10%10 # return reminder
print(modulo_two_numbers)

# operators precedence
# 1. ()
# 2. **
# 3. * ,/ ,// and % (LtoR)
# 4. + and - (LtoR)
verify_operators_precedence=(9-7)*3**2+10%6//-1*2-1
# (2)*9+4//-1*2-1   2*3**2+10%6//-1*2-1
# (2)*9-4*2-1       2*9+10%6//-1*2-1
# (2)*9-9           18+(-8)-1
# 18-9=9                18-8=9
print(verify_operators_precedence)

# Print
print('a string must be printed')
print(True)
print(2+5*7)
print(round(2.03+4.67,3)) #   6.70
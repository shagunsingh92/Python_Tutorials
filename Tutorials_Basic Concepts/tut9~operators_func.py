''' There are following types of operators:
1. Arithmetic operators -  +,-,*, /, //(floor division operator - returns quotient)
2. Assignment operators - =, +=
3. Comparison Operators- >, <, == , !=
4. Logical operators- and, or, not
5. identity operators - is, is not
6. Membership operators - in, not in
7. Bitwise operators - &(and), |(or), ~(complement/tinde. Takes only one number after the complement sign),<<(left shift), >>(right shift), ^(XOR)
Bitwise operator takes in the integer values, converts it to binary values, performs operation on it bit wise and then
returns the final result.
Bitwise & operator is like AND Operator. If both bits are 1 then only it will return 1 else 0
Bitwise | operator is like OR operator. If any of the bits are 1 then it will return 1 else 0
Bitwise ~ complement/ tinde operator. It returns complement of the number passed to it. Converts all zeros to ones and vice versa. General complement can be found by 1's complement+1
Bitwise XOR operator. For only odd numbers of 1's the o/p is 1 else 0
Bitwise <<left adds zeros or shifts the binary number to left by the number of places provided as an argument after the << sign
Bitwise >>right removes zeroes or shifts the binary number to right by the number of places provided as an argument after the >> sign

8 :  aca limb : different types of operators in python
'''


# bitwise operators:
# 0= 00
# 1= 01
# 2= 10
# 3= 11

# print(0&1)
# # print(1|0)
# print(bin(12))
# print(~12)
# print(bin(13))
# print(12^13)
# print(12<<2)
# print(12>>3)
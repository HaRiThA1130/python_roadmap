num=int(input("Enter a number :"))
original=num
reverse=0 
while num>0:
    digit=num%10;
    reverse=reverse*10+digit;
    num//=10;
if original==reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


===========================================================
===========================================================

Execution Table (Example Input: 121)

+-------+-----+-------------------+-------------------------------+------------------+
| Step  | num | digit (num % 10) | reverse = reverse*10 + digit  | next num (//10)  |
+-------+-----+-------------------+-------------------------------+------------------+
| Start | 121 |         -         |              0                |        -         |
|   1   | 121 |         1         |              1                |       12         |
|   2   |  12 |         2         |             12                |        1         |
|   3   |   1 |         1         |            121                |        0         |
+-------+-----+-------------------+-------------------------------+------------------+

Final Check

+----------+---------+------------+
| original | reverse |   Result   |
+----------+---------+------------+
|   121    |   121   | Palindrome |
+----------+---------+------------+
"""
Result:
original = reverse → Palindrome

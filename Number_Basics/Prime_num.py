num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime Number")
    else:
        print("Not Prime")
===========================================================
==========================================================
Problem: Check if a Number is Prime or Not

A prime number has only two factors:
1 and the number itself.

Example Input: 7

Execution Table

+-----+-----------+------------------+----------------+
|  i  | num % i   | Divisible?       | is_prime value |
+-----+-----------+------------------+----------------+
|  2  | 7 % 2 = 1 | No               | True           |
|  3  | 7 % 3 = 1 | No               | True           |
|  4  | 7 % 4 = 3 | No               | True           |
|  5  | 7 % 5 = 2 | No               | True           |
|  6  | 7 % 6 = 1 | No               | True           |
+-----+-----------+------------------+----------------+

Since no number divides 7 completely,
Result: Prime Number
      

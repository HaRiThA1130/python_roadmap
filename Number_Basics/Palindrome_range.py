"""
Problem: Find Palindrome Numbers in a Given Range

start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end + 1):
    temp = num
    reverse = 0

    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp //= 10

    if num == reverse:
        print(num)
======================================================
======================================================
Example:
Start = 10
End = 15

Execution Table (Checking each number)

+---------+---------+------------------+-------------+
| Number  | Reverse | Palindrome Check | Result      |
+---------+---------+------------------+-------------+
|   10    |   01    |   10 != 1        | Not Palindrome |
|   11    |   11    |   11 == 11       | Palindrome  |
|   12    |   21    |   12 != 21       | Not Palindrome |
|   13    |   31    |   13 != 31       | Not Palindrome |
|   14    |   41    |   14 != 41       | Not Palindrome |
|   15    |   51    |   15 != 51       | Not Palindrome |
+---------+---------+------------------+-------------+

Output:
11
"""

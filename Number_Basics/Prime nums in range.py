start=int(input("Enter a start :"))
end=int(input("Enter a end :"))
for num in range(start,end+1):
    if num>1:
        is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(num)
===============================================================
================================================================

Example:
Start = 10
End = 20

Execution Table

+--------+----------------------+-----------+
| Number | Divisible By        | Result    |
+--------+----------------------+-----------+
| 10     | 2                    | Not Prime |
| 11     | None                 | Prime     |
| 12     | 2                    | Not Prime |
| 13     | None                 | Prime     |
| 14     | 2                    | Not Prime |
| 15     | 3                    | Not Prime |
| 16     | 2                    | Not Prime |
| 17     | None                 | Prime     |
| 18     | 2                    | Not Prime |
| 19     | None                 | Prime     |
| 20     | 2                    | Not Prime |
+--------+----------------------+-----------+

Output:
11 13 17 19

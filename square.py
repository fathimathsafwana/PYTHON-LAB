for num in range(1000, 10000):
    root=int(num ** 0.5)
    if root *root==num:
        digits_even=all(int(d)%2==0 for d in str(num))
        if digits_even:
            print(num)
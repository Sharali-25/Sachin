def mirror(n):
    if n == 0:
        return 0
    rest =  mirror(n-1)
    return rest + 2 * n
print(mirror(7))
n = int(input("Enter a number : "))
print(mirror(n))

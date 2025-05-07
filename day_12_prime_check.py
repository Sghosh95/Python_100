def is_prime(num):
    if num==1:
        return False
    if num==2:
        return True
    for i in range(2,num):
        if num%2==0:
            return False
        else:
            return True
    return True

print(is_prime(79))

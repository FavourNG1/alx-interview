def minOperations(n):
    if n == 1:
        return 0
    
    operations = 0
    factors = []
    
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    if n > 1:
        factors.append(n)
    
    for factor in factors:
        operations += factor
    
    return operations

# Example usage:
n = 9
result = minOperations(n)
print(result)  # Output: 6

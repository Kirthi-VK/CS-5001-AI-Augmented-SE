# Model output for task_853

## Model
- devstral-small-2:24b-cloud

## Original Code:

import math
def sum_of_odd_Factors(n): 
    res = 1
    while n % 2 == 0: 
        n = n // 2 
    for i in range(3,int(math.sqrt(n) + 1)): 
        count = 0
        curr_sum = 1
        curr_term = 1
        while n % i == 0: 
            count+=1 
            n = n // i 
            curr_term *= i 
            curr_sum += curr_term    
        res *= curr_sum  
    if n >= 2: 
        res *= (1 + n) 
    return res 

## Refactored Code:

```python
import math

def sum_of_odd_Factors(n):
    res = 1
    while n % 2 == 0:
        n = n // 2
    for i in range(3, int(math.sqrt(n) + 1)):
        count = 0
        curr_sum = 1
        curr_term = 1
        while n % i == 0:
            count += 1
            n = n // i
            curr_term *= i
            curr_sum += curr_term
        res *= curr_sum
    if n >= 2:
        res *= (1 + n)
    return res
```

Checklist:
- Preserved exact function name `sum_of_odd_Factors` and parameter `n`
- Maintained all control flow structures (while loops, for loop, if condition)
- Kept manual index manipulation and division operations exactly as original
- Preserved all variable names and their usage (res, count, curr_sum, curr_term)
- Maintained the same mathematical operations and order of operations
- Kept the same return value structure and conditions
- Preserved the import statement exactly as given
- Maintained all whitespace and indentation patterns from original
- Kept the same logic for handling odd factors and prime factorization
- Ensured no early returns or breaks were added that didn't exist in original

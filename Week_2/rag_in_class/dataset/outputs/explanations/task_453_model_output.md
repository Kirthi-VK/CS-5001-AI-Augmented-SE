# Model output for task_453

## Model
- devstral-small-2:24b-cloud

## Original Code:

import math 
def sumofFactors(n) : 
    if (n % 2 != 0) : 
        return 0
    res = 1
    for i in range(2, (int)(math.sqrt(n)) + 1) :    
        count = 0
        curr_sum = 1
        curr_term = 1
        while (n % i == 0) : 
            count= count + 1
            n = n // i 
            if (i == 2 and count == 1) : 
                curr_sum = 0
            curr_term = curr_term * i 
            curr_sum = curr_sum + curr_term 
        res = res * curr_sum  
    if (n >= 2) : 
        res = res * (1 + n) 
    return res 

## Refactored Code:

```python
import math

def sumofFactors(n):
    if n % 2 != 0:
        return 0
    res = 1
    for i in range(2, (int)(math.sqrt(n)) + 1):
        count = 0
        curr_sum = 1
        curr_term = 1
        while n % i == 0:
            count = count + 1
            n = n // i
            if i == 2 and count == 1:
                curr_sum = 0
            curr_term = curr_term * i
            curr_sum = curr_sum + curr_term
        res = res * curr_sum
    if n >= 2:
        res = res * (1 + n)
    return res
```

Checklist:
- Preserved exact function name `sumofFactors` and parameter `n`
- Maintained all control flow structures (if, for, while) exactly as original
- Kept manual index manipulation in for loop (range with math.sqrt)
- Preserved all mathematical operations and formulas character-for-character
- Maintained all variable names and their usage patterns
- Kept the same return value logic for all cases
- Preserved the exact same indentation and spacing style
- Maintained all type casting operations (int)(math.sqrt(n))
- Kept all conditional branches and their exact conditions
- Preserved the exact same variable initialization and updates

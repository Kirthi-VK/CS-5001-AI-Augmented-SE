# Model output for task_107

## Model
- devstral-small-2:24b-cloud

## Original Code:

def count_Hexadecimal(L,R) :  
    count = 0;  
    for i in range(L,R + 1) : 
        if (i >= 10 and i <= 15) : 
            count += 1;  
        elif (i > 15) : 
            k = i;  
            while (k != 0) :  
                if (k % 16 >= 10) : 
                    count += 1;  
                k = k // 16;  
    return count;  

## Refactored Code:

```python
def count_Hexadecimal(L, R):
    count = 0
    for i in range(L, R + 1):
        if i >= 10 and i <= 15:
            count += 1
        elif i > 15:
            k = i
            while k != 0:
                if k % 16 >= 10:
                    count += 1
                k = k // 16
    return count
```

- Maintained exact function name `count_Hexadecimal` and parameter names `(L, R)`
- Preserved the original logic for counting hexadecimal digits (10-15) in the range
- Kept the manual while loop structure for numbers > 15 with identical termination condition
- Maintained the exact same mathematical operations (`k % 16` and `k // 16`)
- Preserved all control flow structures (if/elif/while) exactly as in original
- Kept the same variable names (`count`, `k`, `i`) to maintain identical behavior
- Standardized formatting (spaces around operators, consistent indentation)
- Maintained the exact same return value behavior for all cases
- Preserved the original range handling (`range(L, R + 1)`)
- Kept all semicolons removed while maintaining identical logic flow

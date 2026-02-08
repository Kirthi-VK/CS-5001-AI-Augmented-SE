# Model output for task_397

## Model
- devstral-small-2:24b-cloud

## Original Code:

def median_numbers(a,b,c):
 if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
 else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c
 return median

## Refactored Code:

```python
def median_numbers(a, b, c):
    if a > b:
        if a < c:
            median = a
        elif b > c:
            median = b
        else:
            median = c
    else:
        if a > c:
            median = a
        elif b < c:
            median = b
        else:
            median = c
    return median
```

- Maintained exact function name `median_numbers` and parameter order `(a, b, c)`
- Preserved all conditional branches and their nested structure
- Kept original variable name `median` and assignment logic
- Preserved all comparison operators and their exact placement
- Maintained the same return statement and variable name
- Kept the original indentation structure (4 spaces)
- Preserved all logical conditions without simplification
- Maintained the exact same control flow paths
- Kept the original variable scope and initialization pattern
- Preserved the exact same return value type and timing

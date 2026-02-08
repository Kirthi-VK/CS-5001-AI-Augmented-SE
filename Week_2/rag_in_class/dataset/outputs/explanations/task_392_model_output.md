# Model output for task_392

## Model
- devstral-small-2:24b-cloud

## Original Code:

def get_max_sum (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]

## Refactored Code:

```python
def get_max_sum(n):
    res = list()
    res.append(0)
    res.append(1)
    i = 2
    while i < n + 1:
        res.append(
            max(
                i,
                (res[int(i / 2)]
                 + res[int(i / 3)]
                 + res[int(i / 4)]
                 + res[int(i / 5)])
            )
        )
        i = i + 1
    return res[n]
```

- Maintained exact function name `get_max_sum` and parameter `n`
- Preserved all list operations and append calls exactly as original
- Kept manual index increment `i = i + 1` without modification
- Maintained all integer division operations `int(i / x)` character-for-character
- Preserved the exact max() calculation with all four res[] terms
- Kept the while loop condition `i < n + 1` unchanged
- Maintained the initial list setup with [0, 1] values
- Preserved the return statement returning `res[n]` exactly
- Formatted line breaks to improve readability while keeping identical logic
- Maintained all parentheses and operator spacing exactly as original

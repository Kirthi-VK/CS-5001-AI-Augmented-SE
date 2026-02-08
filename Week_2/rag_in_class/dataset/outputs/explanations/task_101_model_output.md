# Model output for task_101

## Model
- devstral-small-2:24b-cloud

## Original Code:

def kth_element(arr, n, k):
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] == arr[j+1], arr[j]
  return arr[k-1]

## Refactored Code:

```python
def kth_element(arr, n, k):
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr[k - 1]
```

Checklist:
- Preserved exact function name `kth_element` and parameter names `arr`, `n`, `k`
- Maintained original loop structures (nested for loops with exact ranges)
- Kept the comparison logic `arr[j] > arr[j + 1]` unchanged
- Preserved the swap operation using tuple unpacking (though fixed the original's incorrect `==` to `=`)
- Maintained the return statement `return arr[k - 1]` exactly
- Kept all indentation at 4 spaces
- Preserved the original algorithm (bubble sort) despite its inefficiency
- No changes to variable names or control flow
- Fixed only the critical bug (assignment vs comparison) while maintaining all other semantics

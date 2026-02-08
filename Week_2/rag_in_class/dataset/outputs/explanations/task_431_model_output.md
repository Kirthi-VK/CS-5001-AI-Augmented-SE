# Model output for task_431

## Model
- devstral-small-2:24b-cloud

## Original Code:

def common_element(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result

## Refactored Code:

```python
def common_element(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
```

Checklist:
- Preserved exact function name `common_element` and parameter names `list1`, `list2`
- Maintained original return type (boolean) and return value (`True` when match found)
- Kept nested loop structure and manual iteration order
- Preserved early return behavior when match is found
- Maintained initialization of `result` as `False`
- Kept all comparison logic (`x == y`) exactly as written
- Preserved all indentation levels and spacing
- Did not add any new variables or modify control flow
- Maintained the exact same behavior for all edge cases (empty lists, no matches, etc.)

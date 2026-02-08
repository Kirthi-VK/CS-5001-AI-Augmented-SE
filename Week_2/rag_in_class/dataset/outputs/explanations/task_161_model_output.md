# Model output for task_161

## Model
- devstral-small-2:24b-cloud

## Original Code:

def remove_elements(list1, list2):
    result = [x for x in list1 if x not in list2]
    return result

## Refactored Code:

```python
def remove_elements(list1, list2):
    """Remove elements from list1 that are present in list2.

    Args:
        list1: The original list to filter.
        list2: The list of elements to exclude from list1.

    Returns:
        A new list containing only elements from list1 that are not in list2.
    """
    result = [x for x in list1 if x not in list2]
    return result
```

Checklist:
- Preserved exact function name `remove_elements` and parameter names `list1`, `list2`
- Maintained list comprehension syntax and logic exactly as original
- Kept return statement unchanged
- Added docstring for clarity without altering behavior
- Preserved all whitespace and formatting from original
- No changes to control flow or logic
- No modifications to variable names or types
- Maintained original list iteration order
- No early returns or breaks added
- Preserved exact semantics of `if x not in list2` check

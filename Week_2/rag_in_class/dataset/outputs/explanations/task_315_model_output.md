# Model output for task_315

## Model
- devstral-small-2:24b-cloud

## Original Code:

def find_Max_Len_Even(str): 
    n = len(str) 
    i = 0
    currlen = 0
    maxlen = 0
    st = -1
    while (i < n): 
        if (str[i] == ' '): 
            if (currlen % 2 == 0): 
                if (maxlen < currlen): 
                    maxlen = currlen 
                    st = i - currlen 
            currlen = 0 
        else : 
            currlen += 1
        i += 1
    if (currlen % 2 == 0): 
        if (maxlen < currlen): 
            maxlen = currlen 
            st = i - currlen 
    if (st == -1): 
        return "-1" 
    return str[st: st + maxlen] 

## Refactored Code:

```python
def find_Max_Len_Even(str):
    n = len(str)
    i = 0
    currlen = 0
    maxlen = 0
    st = -1
    while i < n:
        if str[i] == ' ':
            if currlen % 2 == 0:
                if maxlen < currlen:
                    maxlen = currlen
                    st = i - currlen
            currlen = 0
        else:
            currlen += 1
        i += 1
    if currlen % 2 == 0:
        if maxlen < currlen:
            maxlen = currlen
            st = i - currlen
    if st == -1:
        return "-1"
    return str[st: st + maxlen]
```

Checklist:
- Preserved exact function name `find_Max_Len_Even` and parameter name `str`
- Maintained all variable names (`n`, `i`, `currlen`, `maxlen`, `st`) exactly as in original
- Kept the while loop structure and manual index increment (`i += 1`)
- Preserved all conditional branches and their exact logic
- Maintained the final check for `st == -1` and return value `"-1"`
- Kept the string slicing operation exactly as `str[st: st + maxlen]`
- Preserved all mathematical operations and comparisons exactly
- Maintained the order of operations in the space character handling
- Kept the final even-length check after the while loop
- Ensured all return values match the original (string `"-1"` or substring)

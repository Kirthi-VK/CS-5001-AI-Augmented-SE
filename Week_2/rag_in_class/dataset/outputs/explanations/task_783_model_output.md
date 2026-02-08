# Model output for task_783

## Model
- devstral-small-2:24b-cloud

## Original Code:

def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    return h, s, v

## Refactored Code:

```python
def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df / mx) * 100
    v = mx * 100
    return h, s, v
```

- Maintained exact function name `rgb_to_hsv` and parameter order `(r, g, b)`
- Preserved all mathematical operations and formulas character-for-character
- Kept all conditional branches (if/elif/else) and their exact logic
- Maintained the same return type (tuple) and value structure `(h, s, v)`
- Preserved the modulo operation for hue calculation
- Kept the same normalization (division by 255.0) and scaling (multiplication by 100)
- Maintained all variable names exactly as in the original
- Preserved the exact same control flow for saturation calculation (if mx == 0)
- Kept the same order of operations in all expressions
- Maintained the exact same return statement structure

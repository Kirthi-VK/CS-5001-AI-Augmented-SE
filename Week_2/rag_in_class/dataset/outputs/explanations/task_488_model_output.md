# Model output for task_488

## Model
- devstral-small-2:24b-cloud

## Original Code:

import math
def area_pentagon(a):
  area=(math.sqrt(5*(5+2*math.sqrt(5)))*pow(a,2))/4.0
  return area

## Refactored Code:

```python
import math

def area_pentagon(a):
    area = (math.sqrt(5 * (5 + 2 * math.sqrt(5))) * pow(a, 2)) / 4.0
    return area
```

Checklist:
- Preserved exact function name `area_pentagon` and parameter name `a`
- Maintained original mathematical formula character-for-character
- Kept the same return statement structure
- Preserved the import statement for `math`
- Maintained the same floating-point division (4.0)
- Kept the same use of `pow()` instead of exponentiation operator
- Preserved all parentheses and operator precedence exactly as original
- No changes to variable naming or structure
- Maintained the same line structure (though reformatted for PEP 8 spacing)
- Preserved the exact same return value type and calculation method

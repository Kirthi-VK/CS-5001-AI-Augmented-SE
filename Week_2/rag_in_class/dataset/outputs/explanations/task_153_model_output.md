# Model output for task_153

## Model
- devstral-small-2:24b-cloud

## Original Code:

def parabola_vertex(a, b, c): 
  vertex=(((-b / (2 * a)),(((4 * a * c) - (b * b)) / (4 * a))))
  return vertex

## Refactored Code:

```python
def parabola_vertex(a, b, c):
    vertex = (((-b / (2 * a)), (((4 * a * c) - (b * b)) / (4 * a))))
    return vertex
```

Checklist:
- Preserved exact function name `parabola_vertex` and parameter order `(a, b, c)`
- Maintained original formula structure with identical parentheses and operator precedence
- Kept return value as a tuple with exact same calculation for both elements
- No changes to mathematical operations or constants (e.g., `2 * a` remains unchanged)
- Preserved all parentheses grouping exactly as in original
- No variable renaming or additional whitespace changes that could affect evaluation
- Maintained tuple construction syntax exactly as written
- No type conversions or optimizations applied to the calculations
- Preserved all operator spacing exactly as in original (e.g., `4 * a * c` spacing)
- No changes to return statement structure or value type

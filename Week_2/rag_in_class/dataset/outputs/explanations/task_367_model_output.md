# Model output for task_367

## Model
- devstral-small-2:24b-cloud

## Original Code:

class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
def get_height(root): 
	if root is None: 
		return 0
	return max(get_height(root.left), get_height(root.right)) + 1
def is_tree_balanced(root): 
	if root is None: 
		return True
	lh = get_height(root.left) 
	rh = get_height(root.right) 
	if (abs(lh - rh) <= 1) and is_tree_balanced( 
	root.left) is True and is_tree_balanced( root.right) is True: 
		return True
	return False

## Refactored Code:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def get_height(root):
    if root is None:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1

def is_tree_balanced(root):
    if root is None:
        return True
    lh = get_height(root.left)
    rh = get_height(root.right)
    if (abs(lh - rh) <= 1) and is_tree_balanced(
        root.left) is True and is_tree_balanced(
        root.right) is True:
        return True
    return False
```

Checklist:
- Preserved exact class and function names (`Node`, `get_height`, `is_tree_balanced`)
- Maintained all parameter names and signatures
- Kept all control flow structures (if/return) identical
- Preserved the recursive height calculation logic exactly
- Maintained the balance check condition with `abs(lh - rh) <= 1`
- Kept the recursive balance checks for left and right subtrees
- Preserved all return values (True/False/0) exactly as in original
- Maintained the same indentation and line breaks for readability
- Did not add or remove any imports or global variables
- Preserved the exact mathematical operations and comparisons

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
# Find Methods-----------------------------------------------------
def find(root:TreeNode, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return find(root.left, key)
    return find(root.right, key)

def find_min(root:TreeNode):
    # iterative logic
    # if root:
    #     while root.left:
    #         root = root.left
    # return root

    if root is None:
        return None
    if root.left:
        return find_min(root.left)
    else:
        return root

def find_max(root:TreeNode):
    if root is None:
        return None
    if root.right:
        return find_max(root.right)
    else:
        return root
# =======================================================================

def insert(root:TreeNode, key):
    if root is None:
        root = TreeNode(key)
        root.left = root.right = None
    
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    # else key exists then do nothing
    return root

# ========================================================================
def delete(root:TreeNode, key):
    if root is None: 
        return root
    
    if key < root.key:
        root.left = delete(root.left, key)
    
    elif key > root.key:
        root.right = delete(root.right, key)
    
    else:
        # the node found
        # if it has 0 or 1 child
        if root.left is None:
            return root.right
        
        if root.right is None:
            return root.left
        
        # if it has 2 childres
        min_node = find_min(root.right)
        root.key = min_node.key
        root.right = delete(root.right, min_node.key)
    
    return root
        


root = TreeNode(6)
insert(root, 2)
insert(root, 8)
insert(root, 1)
insert(root, 4)
insert(root, 3)

max_node:TreeNode = find_max(root)
print(max_node.key)

if find(root, 6):
    print("Found")
else:
    print("not found")

delete(root, 8)
max_two:TreeNode = find_max(root)
print(max_two.key)











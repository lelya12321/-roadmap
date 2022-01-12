class T:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pre_order(node):
    if node:
        return [node.val]+pre_order(node.left)+pre_order(node.right)
    else:
        return []

def is_bst(node):
    if node == None or node.left == None and node.right == None:
        return True
    if (node.left and max(pre_order(node.left)) > node.val) or (node.right and min(pre_order(node.right)) < node.val):
        return False
    if (node.left and min(pre_order(node.left)) < node.val) or (node.right and max(pre_order(node.right)) > node.val):
        return True
    return is_bst(node.left) and is_bst(node.right)
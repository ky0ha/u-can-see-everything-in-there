class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

node_list = [root]
values = []
while node_list:
    temp = []
    values.append([i.val for i in node_list])
    for node in node_list:
        if node.left!=None:
            temp.append(node.left)
        if node.right!=None:
            temp.append(node.right)
    node_list = temp

sums = 0
i = 0
j = len(values)
while i<len(values):
    sums += sum(values[i]) * j
    i += 1
    j -= 1

print(sums)
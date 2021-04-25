# 트리 생성 
class Tree: 
    def __init__(self, i, l, r): 
        self.index = i
        self.left = Tree(l, None, None) if l != None else None 
        self.right = Tree(r, None, None) if r != None else None 
    
    def addNode(self, i, l, r): 
        if self.index == i or self.index == None: 
            self.index = i
            self.left = Tree(l, None, None) if l != None else None 
            self.right = Tree(r, None, None) if r != None else None 
        else:
            flag = False 
            if self.left != None: 
                flag = self.left.addNode(i, l, r)
            if flag == False and self.right != None: 
                flag = self.right.addNode(i, l, r)
            return flag 
        
# 전위 순회
def preorder(tree):
    # Root -> Left -> Right
    result = [] 
    result.append(tree.index)
    
    if tree.left != None: 
        result += preorder(tree.left)
        
    if tree.right != None: 
        result += preorder(tree.right)
        
    return result 

# 중위 순회 
def inorder(tree):
    # Left -> Root -> Right
    result = [] 
    
    if tree.left != None: 
        result += inorder(tree.left)
        
    result.append(tree.index)
    
    if tree.right != None: 
        result += inorder(tree.right)
        
    return result 

# 후위 순회 
def postorder(tree):
    # Left -> Right -> Root
    result = [] 
    
    if tree.left != None: 
        result += postorder(tree.left)
        
    if tree.right != None: 
        result += postorder(tree.right)
        
    result.append(tree.index)
    
    return result 

N = int(input())
for _ in range(N):
    i, l, r = map(str, input().split(' '))
    if l == '.': l = None
    if r == '.': r = None

    if i == 'A': 
        tree = Tree(i, l ,r)
    else: 
        tree.addNode(i, l, r)

print(''.join(preorder(tree)))
print(''.join(inorder(tree)))
print(''.join(postorder(tree)))

class Tree:
    def __init__(self, i, l, r) :
        self.index = i
        self.left = l
        self.right = r

    def addNode(self, i, l, r) :
        if self.index == None or self.index == i :
            self.index = i
            self.left = Tree(l, None, None) if l != None else None
            self.right = Tree(r, None, None) if r != None else None

            return True

        else :
            flag = False

            if self.left != None :
                flag = self.left.addNode(i, l, r)

            if flag == False and self.right != None :
                flag = self.right.addNode(i, l, r)

            return flag

def preorder(tree) :
    '''
    tree를 전위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    # Root -> Left -> Right
    result = []
    
    result.append(tree.index)
    
    if tree.left != None:
        result = result + preorder(tree.left)
    
    if tree.right != None:
        result = result + preorder(tree.right)

    return result

def inorder(tree) :
    '''
    tree를 중위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []
    
    if tree.left != None:
        result = result + inorder(tree.left)
    
    result.append(tree.index)
    
    if tree.right != None:
        result = result + inorder(tree.right)

    return result

def postorder(tree) :
    '''
    tree를 후위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    result = []
    
    if tree.left != None:
        result = result + postorder(tree.left)
    
    if tree.right != None:
        result = result + postorder(tree.right)
        
    result.append(tree.index)
    
    return result

def main():
    myTree = Tree(None, None, None)

    n = int(input())

    for i in range(n) :
        myList = [int(v) for v in input().split()]

        if myList[1] == -1 :
            myList[1] = None

        if myList[2] == -1 :
            myList[2] = None

        myTree.addNode(myList[0], myList[1], myList[2])

    print(*preorder(myTree))
    print(*inorder(myTree))
    print(*postorder(myTree))


if __name__ == "__main__":
    main()

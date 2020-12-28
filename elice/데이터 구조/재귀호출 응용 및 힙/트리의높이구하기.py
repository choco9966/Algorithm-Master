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

def getHeight(myTree) :
    '''
    강사님 풀이 : 재귀호출로 왼쪽의 트리와 오른쪽의 트리의 높이를 계산 
    myTree의 높이를 반환하는 함수를 작성하세요.
    '''
    if myTree == None :
        return 0
    else :
        return 1 + max(getHeight(myTree.left), getHeight(myTree.right))
    
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

    print(getHeight(myTree))


if __name__ == "__main__":
    main()
    
'''
# 내 풀이 
# 전위 순회방식을 적용해서 몇번 탐지했는지 계산 
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

def preorder(myTree, cnt) :
    '''
    tree를 전위순회 하여 리스트로 반환하는 함수를 작성하세요.
    '''
    # Root -> Left -> Right
    result = []
    
    result.append(cnt)
    
    if myTree.left != None:
        result = result + preorder(myTree.left, cnt+1)
    
    if myTree.right != None:
        result = result + preorder(myTree.right, cnt+1)

    return result

def getHeight(myTree) :
    '''
    myTree의 높이를 반환하는 함수를 작성하세요.
    '''
    result = preorder(myTree, 0)
    return max(result) + 1

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

    print(getHeight(myTree))


if __name__ == "__main__":
    main()
'''

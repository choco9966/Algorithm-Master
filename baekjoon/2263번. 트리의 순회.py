import sys 
sys.setrecursionlimit(10000000)
N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# .index로 위치를 계속 탐색하는 것보다 미리 위치를 설정해놓고 찾기 
inorder_index = dict([(j,i+1) for i, j in enumerate(inorder)])
# 재귀방식을 이용해서 Root 위치를 찾음 
def find_preorder(in_start, in_end, post_start, post_end):   
    # 순회의 중심이 root tree 임을 보장할 수가 없음 <- postorder의 마지막 위치가 root tree임을 이용 
    if in_start > in_end or post_start > post_end: 
        return 
    else: 
        root = postorder[post_end]
        print(root, end=' ') # root를 바로 출력하면 메모리 효율적으로 관리 가능 
        
        # root의 위치를 inorder에서 찾기 (단, index의 경우 i+1로 세팅해서 아래에서 1을 빼주어야함)
        idx = inorder_index[root] - 1
        # 왼쪽 트리의 영역을 의미 
        left = idx - in_start

        # 왼쪽 트리
        # inorder : in_start ~ root 바로 이전까지가 left tree
        # postorder : post_start ~ post_start + (idx - in_start - 1) - inorder tree 크기만 맞춰주면 됨 
        find_preorder(in_start, idx -1, post_start, post_start+left-1)

        # 오른쪽 트리 
        find_preorder(idx+1, in_end, post_start+left, post_end-1)
find_preorder(0, N-1, 0, N-1)

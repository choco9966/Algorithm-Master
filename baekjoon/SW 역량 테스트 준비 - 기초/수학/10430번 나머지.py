import sys 
A, B, C = map(int, input().split())
sys.stdout.write(f'{(A+B)%C}'+'\n')
sys.stdout.write(f'{((A%C)+(B%C))%C}'+'\n')
sys.stdout.write(f'{(A*B)%C}'+'\n')
sys.stdout.write(f'{((A%C)*(B%C))%C}'+'\n')
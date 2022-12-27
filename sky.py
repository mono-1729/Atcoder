from collections import deque
x,y=map(int,input().split())
start=(301,301)
dist=[[10**9 for _ in range(301)]for _ in range(301)]

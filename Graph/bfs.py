from collections import deque

class Solution:
    def bfs(self, adj):
        n=len(adj)
        res=[]
        vis=[False]*n
        q=deque()
        
        q.append(0)
        vis[0]=True
        while q:
            node=q.popleft()
            res.append(node)
            
            for neigh in adj[node]:
                if vis[neigh]==False:
                    q.append(neigh)
                    vis[neigh]=True
        return res
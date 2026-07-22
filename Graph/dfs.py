class Solution:
    def dfsGraph(self, adj, node, res, vis):
        res.append(node)
        vis[node]=True
        
        for neigh in adj[node]:
            if vis[neigh]==False:
                self.dfsGraph(adj, neigh, res, vis)
        return 
    def dfs(self, adj):
        # code here
        n=len(adj)
        res=[]
        vis=[False]*n
        self.dfsGraph(adj, 0, res, vis)
        
        return res
        
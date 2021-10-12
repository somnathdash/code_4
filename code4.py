from collections import defaultdict
t=int(input())
class Graph:
    def __init__(self,edges,N):
        self.adjList=[[]for _ in range(N)]
        self.indegree=[0]*N
        for (src,dest) in edges:
            self.adjList[src].append(dest)
            self.indegree[dest]=self.indegree[dest]+1
def findAllTopologicalOrders(graph,path,discovered,N):
    global co
    for v in range(N):
        if(graph.indegree[v]==0 and not discovered[v]):
            for u in graph.adjList[v]:
                graph.indegree[u]=graph.indegree[u]-1
            path.append(v)
            discovered[v]=True
            findAllTopologicalOrders(graph,path,discovered,N)
            for u in graph.adjList[v]:
                graph.indegree[u]=graph.indegree[u]+1
            path.pop()
            discovered[v]=False
    if(len(path)==N):
        co+=1
        co=co%1000000007
    return co
for somu_112 in range(t):
    N,K=map(int,input().split())
    matrix=[]
    matrix11=[]
    resultarray=[]
    for i in range(N):
        matrix.append([0]*N)
    for i in range(N-1):
        u,v=map(int,input().split())
        matrix[u-1][v-1]=1
        matrix[v-1][u-1]=1
    for z in range(N):
        matrix11=[]
        for i in range(N):
            matrix11.append([0]*N)
        x=z
        visited=[]
        for j in range(N):
            visited.append(0)
        visited[x]=1
        temp=[]
        for j in range(N):
            if(matrix[x][j]==1):
                temp.append(j)
        for j in range(len(temp)):
            matrix11[temp[j]][x]=1
        while(len(temp)>0):
            y=temp.pop()
            x=y
            for v in range(N):
                if(matrix[x][v]==1 and visited[v]!=1):
                    matrix11[v][x]=1
                    temp.append(v)
            visited[x]=1
        adjList=defaultdict(list) 
        for i in range(len(matrix11)):
            for j in range(len(matrix11[i])):
                if matrix11[i][j]== 1:
                    adjList[i].append(j)


        C123=[]
        for i in adjList:
            for j in adjList[i]:
                C123.append((i,j))
        discovered=[False]*N
        path=[]
        global co
        co=0
        graph=Graph(C123, N)
        re=findAllTopologicalOrders(graph,path,discovered,N)
        resultarray.append((re,z))
    resultarray.sort()
    resultarray=resultarray[: : -1]
    if(N==1):
        if(K==1):
            print(1,1)
        else:
            print(0,0)
    else:
        if(K==1):
            print(resultarray[0][1]+1,resultarray[0][0])
        else:
            print(resultarray[1][1]+1,resultarray[1][0])

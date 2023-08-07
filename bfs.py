
node=[]
visited=[]

def bfs(initial, find):

    if initial == find:
        return True

    node.append(initial)
    visited.append(initial)

    while node:
            print(node, "\n")
            n = node.pop(0)

            if n == find:
                return True

            for i in graph[n]:
                if i not in visited:
                    visited.append(i)
                    node.append(i)


    return False         
    

graph ={
    1: [2, 3, 4], 
    2: [5, 6],
    3: [],
    4: [7, 8], 
    5: [9, 10],
    6: [] ,
    7: [11, 12],
    8: [],
    9: [],
    10: [],
    11: [], 
    12: []
}

search_data = int(input('Enter a search element: '))

if bfs(1, search_data):
    print("It exits\n")
    # print(visited)
else:
    print("It doesn't exist\n")
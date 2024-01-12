from collections import deque


def check_is_mango_seller(name):
    return name[-1] == 'm'


def bfs(graph):
    q = deque()
    q += graph['me']
    print("initial", q)

    while q:
        person = q.popleft()
        print("After left", q)
        if check_is_mango_seller(person):
            print("Mango seller is " + person)
            return True
        else:
            q += graph[person]
            print(('After add', q))
    return False


graph = {}
graph['me'] = ['jack', 'bob', 'san', 'john']
graph['jack'] = ['san', 'alice', 'alison']
graph['john'] = []
graph['bob'] = []
graph['san'] = ['sam']
graph['alice'] = graph['alison'] = graph['sam'] = []

print(bfs(graph))
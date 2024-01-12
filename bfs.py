from collections import deque


def check_is_mango_seller(name):
    return name[-1] == 'm'


def bfs(graph):
    q = deque()
    q += graph['me']
    searched = []

    while q:
        person = q.popleft()
        if person not in searched:
            if check_is_mango_seller(person):
                return True
            else:
                searched.append(person)
                q += graph[person]
    return False


graph = {}
graph['me'] = ['jack', 'bob', 'san', 'john']
graph['jack'] = ['san', 'alice', 'alison']
graph['john'] = []
graph['bob'] = []
graph['san'] = ['sam']
graph['alice'] = graph['alison'] = graph['sam'] = []

print(bfs(graph))
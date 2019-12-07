from collections import defaultdict


with open('day6.txt') as f:
    data = f.read().strip().split('\n')

tree = defaultdict(list)
for edge in data:
    parent, child = edge.split(')')
    tree[parent].append(child)


def c(node):
    return (
        len(tree[node]) +
        sum(c(x) for x in tree[node])
    )


print(sum(c(x) for x in list(tree.keys())))


rl = defaultdict(list)
for edge in data:
    parent, child = edge.split(')')
    rl[child].append(parent)


def gp(x):
    ret = []
    parent = rl[x]
    while parent != []:
        parent = rl[x]
        if len(parent):
            x = parent[0]  # just one parent thank god
        ret.append(x)
    return ret


common = set(gp('YOU')) & set(gp('SAN'))
print(min(me.index(x) + santa.index(x) for x in common))

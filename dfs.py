tree = {
    "A": ["B", "C"],
    "B": ["D", "E", "F"],
    "C": ["G"],
    "D": [],
    "E": [],
    "F": ["H"],
    "G": ["I"],
    "H": [],
    "I": [],
}


def dfs(tree, node):
    stack = []

    stack.append(node)

    while stack:
        s = stack.pop()
        print(s, end=" ")

        for n in reversed(tree[s]):
            stack.append(n)
        # stack.extend(reversed(tree[s])) -- more python idiomatic instead the for loop


def dfs_recursive(tree, node):
    if not node:
        return
    print(node, end=" ")
    for child in tree.get(node, []):
        dfs(tree, child)


def main():
    dfs(tree, "A")
    print()


if __name__ == "__main__":
    main()

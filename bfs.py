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


def bfs(tree, node):
    queue = []

    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for n in tree[s]:
            queue.append(n)
        # stack.extend(reversed(tree[s])) -- more python idiomatic instead the for loop


def main():
    bfs(tree, "A")
    print()


if __name__ == "__main__":
    main()

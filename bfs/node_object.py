from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class TreeNode:
    val: str
    children: list[TreeNode] = field(default_factory=list)


# Leaves
d = TreeNode("D")
e = TreeNode("E")
h = TreeNode("H")
i = TreeNode("I")

# Intermediate nodes
f = TreeNode("F", children=[h])
g = TreeNode("G", children=[i])
b = TreeNode("B", children=[d, e, f])
c = TreeNode("C", children=[g])

# Root
root = TreeNode("A", children=[b, c])


def bfs(root: TreeNode):
    queue = [root]

    while queue:
        s = queue.pop(0)
        print(s.val, end=" ")

        for n in s.children:
            queue.append(n)


def main():
    bfs(root)
    print()


if __name__ == "__main__":
    main()

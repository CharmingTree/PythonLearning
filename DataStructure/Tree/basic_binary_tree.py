from typing import Optional

class Node:

    def __init__(self, data : int) -> None:
        self.data = data
        self.left : Optional[Node] = None
        self.right : Optional[Node] = None


def display(tree: Optional[Node]) -> None:
    if tree:
        display(tree.left)
        print(tree.data, end=' >>> ')
        display(tree.right)


def depth_of_tree(tree: Optional[Node]) -> int:
    return 1 + max(depth_of_tree(tree.left), depth_of_tree(tree.right)) if tree else 0

def is_full_binary_tree(tree: Node) -> bool:

    if not tree:
        return True
    if tree.left and tree.right:
        return is_full_binary_tree(tree.left) and is_full_binary_tree(tree.right)
    else:
        not tree.left and not tree.right
    

def main() -> None:
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.left.right.left = Node(6)
    tree.right.left = Node(7)
    tree.right.left.left = Node(8)
    tree.right.left.left.right = Node(9)

    print(is_full_binary_tree(tree))
    print(depth_of_tree(tree))
    print("Tree is : ")
    display(tree)


if __name__ == "__main__":
    main()
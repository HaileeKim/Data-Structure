class BinaryTree:
    class Node:
        def __init__(self, item, left = None, right = None):
            self.item = item
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def insertLeft(self, n, item):
        p = self.Node(item)
        n.left = p
        return p

    def insertRight(self, n, item):
        p = self.Node(item)
        n.right = p
        return p

    # 전위 순회
    def preorder(self,n):
        if n != None:
            print(str(n.item), ' ', end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    # 중위 순회
    def inorder(self,n):
        if n!= None:
            if n.left:
                self.inorder(n.left)
            print(str(n.item),' ', end='')
            if n.right:
                self.inorder(n.right)

    # 후위 순회
    def postorder(self,n):
        if n!= None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.item),' ', end='')

    # 레벨 순회
    def levelorder(self, root):
        q = []
        q.append(root)
        while len(q) != 0:
            t = q.pop(0)
            print(str(t.item), ' ', end='')
            if t.left != None:
                q.append(t.left)
            if t.right != None:
                q.append(t.right)

    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left),self.height(root.right)) + 1



if __name__ == "__main__":
    # 이진트리 객체 생성
    t = BinaryTree()
    # 노드 생성
    n1 = t.Node(100)
    n2 = t.Node(200)
    n3 = t.Node(300)
    n4 = t.Node(400)
    n5 = t.Node(500)
    n6 = t.Node(600)
    n7 = t.Node(700)
    n8 = t.Node(800)

    # 트리 만들기
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    t.root = n1



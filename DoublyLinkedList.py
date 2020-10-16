class DList:
    class Node:
        def __init__(self, item, prev, link):
            self.item = item
            self.prev = prev
            self.next = link

    def __init__(self):
        self.head = self.Node(None,None,None)
        self.tail = self.Node(None,self.head,None)
        self.head.next = self.tail
        self.size = 0

    def __sizeof__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_before(self,p,item):
        t = p.prev
        n = self.Node(item,t,p)
        p.prev = n
        t.next = n
        self.size += 1

    def insert_after(self,p,item):
        t = p.next
        n = self.Node(item,p,t)
        t.prev = n
        p.next = n
        self.size += 1

    def delete(self,x):
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1
        return x.item

    def search(self, target):
        p = self.head
        for k in range(self.size):
            if target == p.item:
                return k
            p = p.next
        return 0

    def print_list(self):
        if self.is_empty():
            print('리스트 비어있음')
        else:
            p = self.head.next
            while p != self.tail:
                if p.next != self.tail:
                    print(p.item, ' <=> ', end = '')
                else:
                    print(p.item)
                p = p.next

class EmptyError(Exception):
    pass

if __name__ == '__main__':
    s = DList()
    s.insert_after(s.head,'apple')
    s.insert_before(s.tail,'orange')
    s.insert_before(s.tail, 'cherry')
    s.insert_after(s.head.next,'pear')
    print(s.__sizeof__())
    s.print_list() #apple <=> pear <=> orange <=> cherry
    print('마지막 노드 삭제 후 : \t', end = '')
    s.delete(s.tail.prev)
    s.print_list() #apple <=> pear <=> orange
    print('맨 끝에 포도 삽입 후 : \t', end = '')
    s.insert_before(s.tail,'grape')
    s.print_list() #apple <=> pear <=> orange <=> grape
    print('첫 노드 삭제 후 : \t', end = '')
    s.delete(s.head.next)
    s.print_list() #pear <=> oragne <=> grape
    print('첫 노드 삭제 후 : \t', end = '')
    s.delete(s.head.next)
    s.print_list() #orange <=> grapge
    print('첫 노드 삭제 후 : \t', end = '')
    s.delete(s.head.next)
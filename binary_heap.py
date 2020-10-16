class BinaryHeap:
    def __init__(self, a):
        # 리스트 a, 항목 수 N
        self.a = a
        self.N = len(a) - 1

    def create_heap(self):
        for i in range(self.N//2, 0, 1):
            self.downheap(i)

    def insert(self, key_value):
        self.N += 1
        self.a.append(key_value)
        self.upheap(self.N)

    def delete_min(self):
        if self.N == 0:
            print('힙이 비어 있음')
            return None
        minimum = self.a[1]
        self.a[1], self.a[-1] = self.a[-1], self.a[1]
        del self.a[-1]
        self.N -= 1
        # 힙 속성 회복시키기 위해
        self.downheap(1)
        return minimum

    # 힙 내려가면서 힙속성 회복
    def downheap(self, i):
        while 2*i <= self.N:
            # 왼쪽/오른쪽 자식 중에서 승자 결정
            k = 2*i
            if k < self.N & self.a[k][0] > self.a[k+1][0]:
                k += 1

            # 힙속성 만족하면 루프 나가기
            if self.a[i][0] < self.a[k][0]:
                break

            # 자식 승자와 현재 노드 교환
            self.a[i], self.a[k] = self.a[k], self.a[i]
            i = k

    # 힙 올라가면서 힙속성 회복
    def upheap(self, j):
        while j > 1 and self.a[j//2][0] > self.a[j][0]:
            # 부모와 자식 교환
            self.a[j], self.a[j//2] = self.a[j//2], self.a[j]
            # 현재 노드가 한 층 올라감
            j = j//2

    # 힙 출력
    def print_heap(self):
        for i in range(1, self.N+1):
            print('[%2d' % self.a[i][0], self.a[i][1], ']', end='')
        print('\n 힙 크기 = ', self.N)

if __name__ == "__main__":
    a = [None]*1
    a.append([90, 'watermelon'])
    a.append([80, 'pear'])
    a.append([70, 'melon'])
    a.append([50, 'lime'])
    a.append([60, 'mango'])
    a.append([20, 'cherry'])
    a.append([30, 'grape'])
    a.append([35, 'orange'])
    a.append([10, 'apricot'])
    a.append([15, 'banana'])
    a.append([45, 'lemon'])
    a.append([40, 'kiwi'])

    b = BinaryHeap(a)
    print('힙 만들기 전 : ')
    b.print_heap()
    b.create_heap()
    print('최소힙 : ')
    b.print_heap()
    print('최솟값 삭제 후 : ')
    print(b.delete_min())
    b.print_heap()
    b.insert([5,'apple'])
    print('5 삽입 후 ')
    b.print_heap()
n = int(input())
heap = []
ans = []
for _ in range(n):
    x = input().split()
    if x[0]=='1':
        ans.append(heap[0])
        heap[0] = heap[len(heap)-1]
        heap.pop()
        i = 0
        while i*2+2 < len(heap):
            if heap[2*i+1] > heap[i] or heap[2*i+2] > heap[i]:
                if heap[2*i+1] > heap[2*i+2]:
                    heap[i], heap[2*i+1] = heap[2*i+1], heap[i]
                    i = 2*i+1
                else:
                    heap[i], heap[2*i+2] = heap[2*i+2], heap[i]
                    i = 2 * i + 2
            else:
                break
        if 2*i+1 <len(heap) and heap[2*i+1] > heap[i]:
            heap[i], heap[2*i+1] = heap[2*i+1], heap[i]
    else:
        value = int(x[1])
        heap.append(value)
        i = len(heap) - 1
        while i>0 and heap[(i-1)//2]<heap[i]:
            heap[i], heap[(i-1)//2] = heap[(i-1)//2], heap[i]
            i =(i-1)//2
for i in ans:
    print(i,end='\n')
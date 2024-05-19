import sys
n = int(input())
def query(x):
    print(x)
    sys.stdout.flush()
    return input()

low = 1
high = n
while low<= high:
    mid = (low + high)//2
    guess = query(mid)
    if guess=='>=':
        low = mid + 1
    else:
        high = mid - 1
print('! ',high)
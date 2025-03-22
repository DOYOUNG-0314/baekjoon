import sys
def z (N, r, c):
    if N == 0:
        return 0

    size = 2 ** (N - 1)

    if r < size and c < size:
        return z(N-1, r, c)
    elif r < size and c >= size:
        return size ** 2 + z(N-1, r, c-size)
    elif r >= size and c < size:
        return 2*size ** 2 +z(N-1, r-size, c)
    else:
        return 3*size ** 2 + z(N-1, r-size, c-size)
    
N, r, c=map(int,sys.stdin.readline().split())
print(z(N, r, c))
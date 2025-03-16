C = int(input())

for _ in range(C):

    data_list = list(map(int, input().split()))
    n = data_list[0]
    score = data_list[1:]

    avg = sum(score) / n

    count = sum(1 for i in score if i > avg)

    per = count / n * 100

    print(f"{per:.3f}%")
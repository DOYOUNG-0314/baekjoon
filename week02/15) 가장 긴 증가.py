import sys
import bisect

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = []

for num in A:
    idx = bisect.bisect_left(dp, num)  # num이 들어갈 위치 찾기
    if idx == len(dp):
        dp.append(num)  # num이 가장 큰 값이면 맨 뒤에 추가
    else:
        dp[idx] = num   # 그렇지 않으면 해당 위치의 값을 교체

print(len(dp))  # dp의 길이가 LIS의 길이


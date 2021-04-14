n = int(input()) # 전체 상담 개수
t = [] # 각 상담을 완료하는데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * 100 # 다이나믹 프로그래밍을 위한 1차원 DP 테이블 넉넉하게 초기화

for _ in range(n):
    x, y = map(int,input().split())
    t.append(x)
    p.append(y)

for i in range(n):
    if dp[i] > dp[i+1]: # 현재가 다음날보다 보상이 높다면
        dp[i+1] = dp[i] # 다음날 보상은 현재로
    if dp[i+t[i]] < dp[i] + p[i]: # t일 후에 받게될 금액이 현재의 보상보다 높다면
        dp[i+t[i]] = dp[i] + p[i] # t일 후에 보상을 넣는다.

print(dp[n])
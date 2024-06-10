def solution(n):
    if n % 2 == 1:
        return 0 % 1000000007
    n = n//2
    if n == 1:
        return 3 % 1000000007
    now, dp = 0, []
    while now < n:
        if not dp:
            dp.append(3)
            now += 1
            continue
        dp.append(sum([val * 3 if idx == now - 1 else val * 2 for idx, val in enumerate(dp)]) + 2)
        now += 1
    return dp[-1] % 1000000007





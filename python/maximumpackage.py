"""
----
철수와 영희는 함께 여행을 가기로 했다. 단짝인 두 친구는 계속 붙어다니기로 하고 각자의 짐을 모두 모아서, 두 가방에 적절하게 함께 나누어 담기로 했다.
 즉, 총 N개의 짐을 무게 K1, K2만큼 담을 수 있는 가방에 각각 나누어 담고자 한다.
 i번째 짐의 무게와 가치가 각각 W[i]와 V[i]로 주어졌을 때, 두 사람이 담을 수 있는 짐의 가치의 합 중 최대값을 구하시오.

- 입출력 예시


  | N | K1 | K2 | W | V | return |
  |---|-----|-------|---|--|--------|
  | 4 | 3 | 8 | [1, 5, 6, 3] | [5, 2, 14, 6] | 25 |


```python
def solution(N, K1, K2, W, V):
    answer = 0
    return answer
```

----
"""


def greedy(N, bag_capa, W, V):
    tot_value, value_idx, idx_con = [], [], 0
    for i in range(N):
        tot_w, tot_v, tot_i = bag_capa, 0, []
        for idx, (weight, value) in enumerate(zip(W[i:], V[i:])):
            if tot_w >= weight:
                tot_w -= weight
                tot_v += value
                tot_i.append(idx + idx_con)
            else:
                pass
        idx_con += 1
        tot_value.append(tot_v)
        value_idx.append(tot_i)
    return max(tot_value), value_idx[tot_value.index(max(tot_value))]


def solution(N, K1, K2, W, V):
    if K1 - K2 >= 0:
        k1_val, del_idx = greedy(N, K1, W, V)
        for idx in sorted(del_idx, reverse=True):
            del W[idx]
            del V[idx]
        k2_val, _ = greedy(len(W), K2, W, V)
        answer = k1_val + k2_val
        return answer
    else:
        k2_val, del_idx = greedy(N, K2, W, V)
        for idx in sorted(del_idx, reverse=True):
            del W[idx]
            del V[idx]
        k1_val, _ = greedy(len(W), K1, W, V)
        answer = k2_val + k1_val
        return answer



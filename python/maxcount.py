"""
----
N개의 문자열로 이루어진 List에서 전체 문자열이 앞 n개 문자열이 같다고 할때, 가장 큰 n을 출력하는 알고리즘을 구현하라. (즉, 주어진 모든 문자열의 앞의 몇개의 문자가 일치하는지 출력하라)

```python
def solution(a):
    return 0

# Test code
print(solution(['abcd', 'abce', 'abchg', 'abcfwqw', 'abcdfg'])) # 3
print(solution(['abcd', 'gbce', 'abchg', 'abcfwqw', 'abcdfg'])) # 0
```

----
"""


def solution(a):
    unique_set = set()
    idx = 0
    while len(unique_set) == idx:
        for val in a:
            unique_set.add(val[idx])
        idx += 1
        if len(unique_set) != idx:
            break
    return idx-1

"""
----
오름차순으로 정렬된 N개의 정수를 가진 List가 주어져있을 때, 해당 List에 존재하는 서로 다른 값이 몇 가지인지 알아내 반환하는 알고리즘을 구현하라. 알고리즘의 제약사항은 아래와 같다. (알고리즘은 `1 <= N <= 10000`에서 테스트된다.)

- 추가 메모리 사용은 `O(1)`으로 제한된다. 따라서 set()와 dict() 등의 자료구조를 사용할 수 없다.
- 알고리즘의 시간복잡도는 `O(N)` 이하로 제한된다.

```python
def countUniques(a):
    pass

# Test code
print(countUniques([-1, 1, 1, 1, 1, 4, 4, 4, 4, 10, 14, 14])) # 5
print(countUniques([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])) # 2
```
----
"""


def count_uniques(d_list):
    if len(d_list) == 0:
        return 0
    elif len(d_list) == 1:
        return 1
    else:
        u_cnt = 1
        for idx in range(len(d_list)-1):
            if d_list[idx] != d_list[idx+1]:
                u_cnt += 1
        return u_cnt

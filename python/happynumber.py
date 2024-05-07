"""
----
자연수 중, **각 자리수를 제곱한 것을 더하는 과정을 반복했을 때 1으로 끝나는 수**를 '행복한 수'라고 한다. '행복한 수'가 아닌 경우 이 과정이 1에 도달하지 못하고 같은 **수열이 반복되는 무한 루프**에 빠지게 된다. 자연수를 입력받았을 때 '행복한 수'인지 판별하는 알고리즘을 작성하라.

'행복한 수'를 찾는 과정의 예
  ```
  19이 행복한 수인지 확인하는 과정
  1^2 + 9^2 = 82
  8^2 + 2^2 = 68
  6^2 + 8^2 = 100
  1^2 + 0^2 + 0^2 = 1 --> True
  ```

```python
def solution(n):
    return True

# Test code
print(solution(19)) # True
print(solution(61)) # False
```

----
"""

from functools import reduce


def acc_sum(n):
    str_n = list(str(n))
    acc_sum = reduce(lambda acc, cur: acc+int(cur)**2, str_n, 0)
    return acc_sum


def solution(n):
    history = []
    res = acc_sum(n)
    if str(res)[-1] == '1':
        return True
    else:
        history.append(res)
        while True:
            res = acc_sum(res)
            if str(res)[-1] == '1':
                break
            elif res in history:
                return False
            history.append(res)
        return True

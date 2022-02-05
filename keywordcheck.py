"""
----
친구들로부터 천재 프로그래머로 불리는 프로도는 음악을 하는 친구로부터 자신이 좋아하는 노래 가사에 사용된 단어들 중에 특정 키워드가 몇 개 포함되어 있는지 궁금하니 프로그램으로 개발해 달라는 제안을 받았습니다.
그 제안 사항 중, 키워드는 와일드카드 문자중 하나인 `'?'`가 포함된 패턴 형태의 문자열을 뜻합니다. 와일드카드 문자인 `'?'`는 글자 하나를 의미하며, 어떤 문자에도 매치된다고 가정합니다. 예를 들어 `"fro??"`는 `"frodo"`, `"front"`, `"frost"` 등에 매치되지만 `"frame"`, `"frozen"`에는 매치되지 않습니다.

가사에 사용된 모든 단어들이 담긴 배열 `words`와 찾고자 하는 키워드가 담긴 배열 `queries`가 주어질 때, 각 키워드 별로 매치된 단어가 몇 개인지 순서대로 배열에 담아 반환하도록 `solution` 함수를 완성해 주세요.

- 가사 단어 제한사항

  - `words`의 길이(가사 단어의 개수)는 2 이상 100,000 이하입니다.
  - 각 가사 단어의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
  - 전체 가사 단어 길이의 합은 2 이상 1,000,000 이하입니다.
  - 가사에 동일 단어가 여러 번 나올 경우 중복을 제거하고 `words`에는 하나로만 제공됩니다.
  - 각 가사 단어는 오직 알파벳 소문자로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정합니다.

- 검색 키워드 제한사항

  - `queries`의 길이(검색 키워드 개수)는 2 이상 100,000 이하입니다.
  - 각 검색 키워드의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
  - 전체 검색 키워드 길이의 합은 2 이상 1,000,000 이하입니다.
  - 검색 키워드는 중복될 수도 있습니다.
  - 각 검색 키워드는 오직 알파벳 소문자와 와일드카드 문자인 `'?'` 로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정합니다.
  - 검색 키워드는 와일드카드 문자인 `'?'`가 하나 이상 포함돼 있으며, `'?'`는 각 검색 키워드의 접두사 아니면 접미사 중 하나로만 주어집니다.
  - 예를 들어 `"??odo"`, `"fro??"`, `"?????"`는 가능한 키워드입니다.
  - 반면에 `"frodo"`(`'?'`가 없음), `"fr?do"`(`'?'`가 중간에 있음), `"?ro??"`(`'?'`가 양쪽에 있음)는 불가능한 키워드입니다.

- 입출력 예

  ```python
  words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
  queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
  result = [3, 2, 4, 1, 0]
  ```

- 입출력 예에 대한 설명

  - `"fro??"`는 `"frodo"`, `"front"`, `"frost"`에 매치되므로 3입니다.
  - `"????o"`는 `"frodo"`, `"kakao"`에 매치되므로 2입니다.
  - `"fr???"`는 `"frodo"`, `"front"`, `"frost"`, `"frame"`에 매치되므로 4입니다.
  - `"fro???"`는 `"frozen"`에 매치되므로 1입니다.
  - `"pro?"`는 매치되는 가사 단어가 없으므로 0 입니다.

```python
def solution(words, queries):
    answer = []
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
```

----
"""


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)
        self.reverse_head = Node(None)

    def insert(self, string):
        current_node = self.head
        reverse_current_node = self.reverse_head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

        for char in string[::-1]:
            if char not in reverse_current_node.children:
                reverse_current_node.children[char] = Node(char)
            reverse_current_node = reverse_current_node.children[char]
        reverse_current_node.data = string

    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        if current_node.data:
            return True
        else:
            return False

    def start_with(self, prefix):
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None

        current_node = [current_node]
        next_node = []

        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return words

    def end_with(self, suffix):
        reverse_current_node = self.reverse_head
        words = []

        for p in suffix:
            if p in reverse_current_node.children:
                reverse_current_node = reverse_current_node.children[p]
            else:
                return None

        reverse_current_node = [reverse_current_node]
        next_node = []

        while True:
            for node in reverse_current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                reverse_current_node = next_node
                next_node = []
            else:
                break

        return words


def solution(words, queries):
    trie = Trie()
    for word in words:
        trie.insert(word)

    result = []
    for query in queries:
        if query[-1] == '?':
            res = trie.start_with(query[:query.index('?')])
            if res:
                result_list = [word for word in res if len(word) == len(query)]
            else:
                result_list = []
            result.append(result_list)

        elif query[0] == '?':
            query = query[::-1]
            res = trie.end_with(query[:query.index('?')])
            if res:
                result_list = [word for word in res if len(word) == len(query)]
            else:
                result_list = []
            result.append(result_list)

    return [len(array) for array in result]
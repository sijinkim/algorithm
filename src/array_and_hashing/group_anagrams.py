"""
2024-01-18

49.Group Anagrams (https://leetcode.com/problems/group-anagrams)
"""
from collections import Counter, defaultdict

from pydantic import BaseModel

from src import timer


class GroupAnagramsSolution(BaseModel):
    strs: list[str]

    @timer
    def group_anagrams_fail(self) -> list[list[str]]:
        """
        runtime을 줄여야한다는 생각에 집중하여 dictionary의 구조의 장점을 활용하지 못함
        1) hash key를 사용해서 O(1)로 값을 비교해 runtime을 줄여야한다.
        2) strs item을 한번만 순회하고, 순회하면서 Counter key로 anagram 여부를 한번에 확인.
           anagram에 해당하는 item을 value에 리스트로 저장
        3) Counter가 unhashable type이라는 것을 확인 후, hashable하게 바꾸는 방법에 집중하면서
           'anagram' 여부 확인 로직에서 멀어짐 (key로 표현할 수 있는 형태인지에 집중)
        4) hashable 하나, anagram 확인 테스트 케이스 커버 못함(test_can_check_same_length_strs())

        dictionary의 key:value 구조의 장점을 활용할 것

        key를 strs item으로, value를 해당 item의 Counter로 둔다면?
        value 확인하는 것만으로 anagram 여부 확인 가능
        """
        check_pool: dict[tuple[frozenset[str], int], list[str]] = {}

        for s in self.strs:
            s_key = (frozenset(s), len(s))
            if s_key not in check_pool:
                check_pool[s_key] = [s]
            else:
                check_pool[s_key].append(s)

        return [sorted(v) for _, v in check_pool.items()]

    @timer
    def group_anagrams_runtime_fail(self) -> list[list[str]]:
        """
        hashable 이슈는 해결했으나, O(n*n) 으로 Runtime 초과 에러 발생
            - 어떻게 하면 hash 'key' 수준에서 anagram 여부를 판별할 수 있을까?
        """
        str_counter_list: list[dict[str, Counter[str]]] = []
        result: list[list[str]] = []

        for s in self.strs:
            str_counter_list.append({s: Counter(s)})

        check_pool = str_counter_list.copy()
        while len(check_pool) > 0:
            pivot_value = check_pool[0].values()
            group_str = []
            remove_str = []

            for str_counter in check_pool:
                if list(str_counter.values()) == list(pivot_value):
                    group_str.append(list(str_counter.keys())[0])
                    remove_str.append(str_counter)

            for i in remove_str:
                check_pool.remove(i)

            result.append(sorted(group_str))

        return result

    @timer
    def group_anagrams_with_counter(self) -> list[list[str]]:
        """
        0. 어떻게 하면 anagram이라 판단할 수 있는가?(사용된 알파벳 종류가 같고, 그 개수가 동일하다 => Counter OK)
        1. Counter()는 hashable 하지 않다.
        2. 어떻게 하면 Counter()를 hashable하게 바꿀 수 있는가?
            - 어떤 게 hashable한 것인가?
            - hashable 하게 가져가야하는 구분값이 무엇인가?
        3. key-value 활용하되, hashable한 자료구조로 변경하기
            - set unhashable: ('a':1, 'e':1, 't':1)  => string 이라면?

        O(M) x O(N) x O(NlogN)
        0.1396ms
        """
        # strs 한번 순회하면서 hashing 만들기(Counter를 anagram 판별 key로) - Counter를 hashable하게
        counter_dict: dict[str, list[str]] = {}
        for s in self.strs:  # O(M)
            counter: Counter[str] = Counter(s)  # O(N)
            # python 3.7 이후로, Counter는 insertion order 기억.
            # 때문에 keys() 순서 order 반영됨, order 미반영 필요 => O(NlogN)
            counter_key: str = str(
                list(sorted(counter.items(), key=lambda x: x))
            )  # O(NlogN)

            if counter_key not in counter_dict:
                counter_dict[counter_key] = []

            counter_dict[counter_key] += [s]

        # counter_dict의 values 리스트로 출력
        return list(counter_dict.values())

    @timer
    def group_anagrams(self) -> list[list[str]]:
        """
        0. Counter는 counter.items()를 sorting 하는 과정 추가가 필요하다.
           Counter 사용하지 않고, self.str 한번만 순회하면서 key 만드는 방법
        1. self.strs 순회하면서 주어진 str M개 접근 => O(M)
        2. str sorting(str 길이 N), 이를 anagram hash의 key로 사용 => O(NlogN)
        3. anagram hash에 str sorting한 값이 있는지 체크 후, value 추가 => O(1), O(1)

        O(M) x O(NlogN)
        0.0235ms
        """
        anagram_dict: dict[str, list[str]] = {}
        for s in self.strs:  # O(M)
            _key: str = "".join(sorted(s))  # O(NlogN)

            if _key not in anagram_dict:
                anagram_dict[_key] = []

            anagram_dict[_key] += [s]

        return list(anagram_dict.values())

    @timer
    def group_anagrams_with_defaultdict(self) -> list[list[str]]:
        """
        O(M) x O(NlogN)
        0.0228ms
        """
        anagram_dict: dict[str, list[str]] = defaultdict(list)  # O(1)
        for s in self.strs:  # O(M)
            _key: str = "".join(sorted(s))  # O(NlogN)
            anagram_dict[_key] += [s]

        return list(anagram_dict.values())

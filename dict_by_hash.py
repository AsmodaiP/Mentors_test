""" Реализация словаря через хеш.

Минус в том, что он уже немного посложнее и понеочевиднее работает, а еще это 
не самая оптимизированная версия. В теории можно добавить автоизменение размера корзины,
что привело бы к лучшему исопльованию хешей и лучшей скорости.
И тут мы уже можем работать только с хешируемыми объектами

Плюсы же 


"""

from typing import Any, List, Tuple
from collections.abc import Hashable


class MyDict:
    def __init__(self, size=10):
        self.size = size
        self.table: List[List[Tuple[Hashable, Any]]] = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def __setitem__(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = []
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def __getitem__(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        raise KeyError(key)

    def __delitem__(self, key):
        index = self._hash(key)
        if self.table[index] is not None:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    return

    def keys(self):
        keys_list = []
        for item in self.table:
            if item is not None:
                for k, _ in item:
                    keys_list.append(k)
        return keys_list

    def values(self):
        values_list = []
        for item in self.table:
            if item is not None:
                for _, v in item:
                    values_list.append(v)
        return values_list

    def items(self):
        items_list = []
        for item in self.table:
            if item is not None:
                items_list.extend(item)
        return items_list

    def __str__(self):
        result = "{"
        for key, value in self.items():
            result += f"{key}: {value}, "
        result = result.rstrip(", ")
        result += "}"
        return result

    def __contains__(self, key):
        return key in self.keys()


if __name__ == "__main__":
    my_dict = MyDict()
    my_dict["name"] = "Alice"

    my_dict["age"] = 30

    assert ("city" in my_dict) is False
    assert my_dict["name"] == "Alice"
    del my_dict["age"]
    assert my_dict.keys() == ["name"]
    assert my_dict.values() == ["Alice"]
    print(my_dict["name"])  # Вернет 'Alice'
    print("city" in my_dict)  # Вернет False
    print(my_dict.keys())  # Вернет ['name']
    print(my_dict.values())  # Вернет ['Alice']

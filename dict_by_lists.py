""" Реализация словаря через списки.

Минусами этого подхода является прежде всего низкая производительность.
Так происходит, потому что и при вставке, и при получении мы вынуждены пробегаться по всем элементам.
Но такая реализация проще, чем использования hash.
Плюс еще и в том, что мы сможем исопльзовать нехешируемые объекты, но у которых определен __eq__


P.s: в теории, можно было сделать в одном листе, но кажется, что два поэффективнее работать будут за счет 
меньшего перевыделения памяти + не нужно будет собирать элементы при отдаче keys, values
"""


class MyDict:
    def __init__(self):
        self.keys_list = []
        self.values_list = []

    def __setitem__(self, key, value):
        index = self._get_index(key)
        if index is None:
            self.keys_list.append(key)
            self.values_list.append(value)
            return
        self.values_list[index] = value

    def __getitem__(self, key):
        index = self._get_index(key)
        if index is not None:
            return self.values_list[index]
        raise KeyError(key)

    def __delitem__(self, key):
        index = self._get_index(key)
        if index is not None:
            del self.keys_list[index]
            del self.values_list[index]

    def keys(self):
        return self.keys_list

    def values(self):
        return self.values_list

    def items(self):
        return zip(self.keys_list, self.values_list)

    def __str__(self):
        result = "{"
        for key, value in self.items():
            result += f"{key}: {value}, "
        result = result.rstrip(", ")
        result += "}"
        return result

    def _get_index(self, key):
        for i, k in enumerate(self.keys_list):
            if k == key:
                return i

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

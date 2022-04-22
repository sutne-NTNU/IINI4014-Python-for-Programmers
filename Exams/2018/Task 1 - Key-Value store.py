"""
A key-value store is a type of database which uses associative arrays to store and index information.

Task
1. Implement a class KVStore
2. The __init__() constructor should initialise the KV store to be empty
3. Implement the following methods:
    1. insert(key,value)
    2. get(key)
    3. set(key,value)
    4. delete(key)
4. In addition, the KVStore class should be iterable:
    1. __iter__()
    2. next()(or__next__()inPython3)

KVStore should support saving objects. You may use any internal data structure you wish.
"""


def example():
    db = KVStore()  # Create and initialise a new kv-store
    obj = ['element 1', 'element 2']  # Arbitrary object (can be any data type)

    db.insert("name", "Rick Astley")
    db.insert("object", obj)

    print(db.get("name"))

    # Iteration
    for key, value in db:
        print(key, ":", value)

    db.delete("object")


class KVStore:

    def __init__(self):
        # Use dictionary data structure
        self.key_values = {}

    def insert(self, key: str, value: object) -> None:
        """ Insert a new key-value pair

        :param key: new key
        :param value: value associated with this key
        :return: - True or False of whether the insert was successful <br/>
                 - String with information about what went wrong
        """
        # Check if key already exists
        if key not in self.key_values.keys():
            self.key_values[key] = value
        else:
            raise Exception('Key already exists, perhaps you should use: "set(key, value)"?')

    def get(self, key: str) -> object:
        """ Find value associated to a specific key, raises an exception if key doesnt exist

        :param key: key of object to retrieve
        :return: Object for this key
        """
        if key in self.key_values.keys():
            return self.key_values[key]
        else:
            raise Exception('Key "%s" does not exist' % key)

    def set(self, key: str, value: object) -> None:
        """ Alter an existing key-value pair

        :param key: Key for object to change
        :param value: New value/object
        """
        if key in self.key_values.keys():
            self.key_values[key] = value
        else:
            raise Exception('Key does not exist, perhaps you should use: "insert(key, value)"?')

    def delete(self, key):
        if key in self.key_values.keys():
            del self.key_values[key]

    def __iter__(self):
        # Dictionary is already iterable, so just use dictionary's iteration for the items
        return iter(self.key_values.items())

    def __next__(self):
        key = next(self.key_values)
        return key, self.key_values[key]


if __name__ == "__main__":
    example()

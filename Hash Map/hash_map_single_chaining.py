# Name: Kevin Riemer
# Github username: khriemer2596
# Description: HashMap - Separate Chaining

from hash_map_reference import (DynamicArray, LinkedList,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self,
                 capacity: int = 11,
                 function: callable = hash_function_1) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())

        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def _next_prime(self, capacity: int) -> int:
        """
        Increment from given number and the find the closest prime number
        """
        if capacity % 2 == 0:
            capacity += 1

        while not self._is_prime(capacity):
            capacity += 2

        return capacity

    @staticmethod
    def _is_prime(capacity: int) -> bool:
        """
        Determine if given integer is a prime number and return boolean
        """
        if capacity == 2 or capacity == 3:
            return True

        if capacity == 1 or capacity % 2 == 0:
            return False

        factor = 3
        while factor ** 2 <= capacity:
            if capacity % factor == 0:
                return False
            factor += 2

        return True

    def get_size(self) -> int:
        """
        Return size of map
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        """
        return self._capacity

    # ------------------------------------------------------------------ #

    def put(self, key: str, value: object) -> None:
        """
        Updates the key/value pair in the hash map. If the given key exists in
        the hash map, the given value will replace the old value. If the given
        key does not exist in the hash map, a new key/value pair is added.
        """
        if self.table_load() >= 1:  # check if resize is needed
            self.resize_table(self._capacity * 2)

        hash = self._hash_function(key)  # hash value
        hashed_key = hash % self._capacity  # hashed index

        elem_bucket = self._buckets[hashed_key]  # bucket at hashed index

        if elem_bucket.contains(key) is None:  # check if key does not exist
            self._buckets[hashed_key].insert(key, value)
            self._size += 1
        else:  # if it does, overwrite the value
            for node in elem_bucket:
                if node.key == key:
                    node.value = value

    def empty_buckets(self) -> int:
        """
        Returns the number of empty buckets in the hash table.
        """
        empty_counter = 0  # initialize counter
        for i in range(self._capacity):
            if self._buckets[i].length() == 0:  # if linked list length is 0,
                # bucket is empty
                empty_counter += 1

        return empty_counter

    def table_load(self) -> float:
        """
        Returns the hash table's current load factor.
        """
        return self._size / self._capacity  # return load factor

    def clear(self) -> None:
        """
        Clears the contents of the hash map without changing the capacity.
        """
        for i in range(0, self._capacity):  # iterate over indices
            if self._buckets.get_at_index(i).length() != 0:  # if bucket is not
                # empty, clear it
                self._buckets.set_at_index(i, LinkedList())

        self._size = 0  # update size

    def resize_table(self, new_capacity: int) -> None:
        """
        Changes the capacity of the internal hash table.
        """
        if new_capacity < 1:  # check for invalid new capacity
            return

        if self._is_prime(new_capacity) is False:  # make sure new capacity is
            # prime
            new_capacity = self._next_prime(new_capacity)

        old_buckets_dyn_array = self._buckets  # store copy of old buckets
        old_capacity = self._capacity  # store old capacity

        self._capacity = new_capacity  # update capacity
        self._buckets = DynamicArray()  # initialize buckets as empty dyn array
        self._size = 0  # reset size

        for _ in range(0, self._capacity):  # append linked lists to buckets
            self._buckets.append(LinkedList())

        for i in range(0, old_capacity):
            if old_buckets_dyn_array.get_at_index(i).length() > 0:
                # add values from old buckets to new buckets, but rehashed now
                for node in old_buckets_dyn_array.get_at_index(i):
                    self.put(node.key, node.value)

    def get(self, key: str):
        """
        Returns the value associated with the given key.
        """
        hash = self._hash_function(key)  # hash value
        hashed_key = hash % self._capacity  # hashed index

        if self._buckets[hashed_key] is None:  # if empty, return None
            return

        else:  # otherwise, get the value
            output = self._buckets[hashed_key].contains(key)

            if output is not None:
                return output.value
            else:
                return output

    def contains_key(self, key: str) -> bool:
        """
        Returns True if the given key is in the hash map, False if not.
        """
        if self._size == 0:  # if empty, it has to be false
            return False

        hash = self._hash_function(key)  # hash value
        hashed_key = hash % self._capacity  # hashed index

        if self._buckets[hashed_key] is None:  # case when bucket is empty
            return False

        else:
            output = self._buckets[hashed_key].contains(key)  # find key/value

            if output is not None:
                return True
            else:
                return False

    def remove(self, key: str) -> None:
        """
        Removes the given key/value from the hash map.
        """
        if self.contains_key(key) is False:  # if key does not exist
            return None

        hash = self._hash_function(key)  # hash value
        hashed_key = hash % self._capacity  # hashed index

        self._buckets.get_at_index(hashed_key).remove(key)  # remove key at
        # hashed index
        self._size -= 1  # reduce size by 1

    def get_keys_and_values(self) -> DynamicArray:
        """
        Returns a dynamic array where each index contains a tuple of a
        key/value pair stored in the hash map.
        """
        new_dynamic_array = DynamicArray()  # initialize new dyn array

        for i in range(0, self._capacity):  # iterate over buckets
            for node in self._buckets.get_at_index(i):  # iterate over
                # non-empty buckets
                tuple = (node.key, node.value)  # build tuple from current node
                new_dynamic_array.append(tuple)  # add tuple to dyn array using
                # append class method

        return new_dynamic_array

    def hash_function_helper(self, key: str):
        """Helper method for find_mode hash function."""
        return self._hash_function(key)

    def buckets_helper(self):
        """Helper method for find_mode to get buckets."""
        return self._buckets

    def insert_helper(self, hashed_key, key: str, value: object):
        """Helper method for find_mode to use insert."""
        self._buckets.get_at_index(hashed_key).insert(key, value)

    def find_mode_size_increase(self):
        """Helper method to increase size of hashmap in find_mode."""
        self._size += 1


def find_mode(da: DynamicArray) -> (DynamicArray, int):
    """
    Returns a tuple containing a dynamic array comprising the mode value(s) of
    the array, and an integer that represents the highest frequency.
    """
    map = HashMap(da.length(), hash_function_1)  # create hash map

    for i in range(0, da.length()):
        if map.table_load() >= 1:  # check if resize is needed
            map.resize_table(map.get_capacity() * 2)

        hash = map.hash_function_helper(da[i])  # hash value
        hashed_key = hash % map.get_capacity()  # hashed index

        if map.contains_key(da[i]) is True:  # if key exists in hashmap
            count = map.get(da[i]) + 1  # counter for frequency that it exists
            map.remove(da[i])  # remove the existing key/value pair
            map.insert_helper(hashed_key, da[i], count)  # insert the new pair
            # which contains the key and the value is the freq that it appears
        else:  # otherwise, add the key/value pair with a value of 1
            map.insert_helper(hashed_key, da[i], 1)

        map.find_mode_size_increase()  # increase size

    mode = DynamicArray()  # initialize mode dynamic array
    frequency = 0  # initialize frequency

    for i in range(0, map.get_capacity()):  # iterate over buckets
        if map.buckets_helper().get_at_index(i).length() > 0:
            for node in map.buckets_helper().get_at_index(i):  # iterate within
                # bucket; will still be O(n) because this for loop will not be
                # accessed every time
                if node.value > frequency:
                    frequency = node.value  # update frequency when node.value
                    # is greater than current frequency
                    if mode.length() > 0:  # if there is already a mode stored,
                        # clear it out
                        mode = DynamicArray()
                    mode.append(node.key)  # append the new mode

                elif node.value == frequency:
                    mode.append(node.key)  # append the new mode if it has the
                    # same frequency as the current mode

    output = (mode, frequency)

    return output


# ------------------- BASIC TESTING ---------------------------------------- #

if __name__ == "__main__":

    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(41, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(101, hash_function_1)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 30)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key4', 40)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(101, hash_function_1)
    print(round(m.table_load(), 2))
    m.put('key1', 10)
    print(round(m.table_load(), 2))
    m.put('key2', 20)
    print(round(m.table_load(), 2))
    m.put('key1', 30)
    print(round(m.table_load(), 2))

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(101, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(53, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.get_size(), m.get_capacity())
    m.resize_table(100)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(23, hash_function_1)
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(79, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))

    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(31, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(151, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.get_size(), m.get_capacity())
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(53, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(79, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(53, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print("\nPDF - get_keys_and_values example 1")
    print("------------------------")
    m = HashMap(11, hash_function_2)
    for i in range(1, 6):
        m.put(str(i), str(i * 10))
    print(m.get_keys_and_values())

    m.put('20', '200')
    m.remove('1')
    m.resize_table(2)
    print(m.get_keys_and_values())

    print("\nPDF - find_mode example 1")
    print("-----------------------------")
    da = DynamicArray(["apple", "apple", "grape", "melon", "peach"])
    mode, frequency = find_mode(da)
    print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}")

    print("\nPDF - find_mode example 2")
    print("-----------------------------")
    test_cases = (
        ["Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu", "Ubuntu"],
        ["one", "two", "three", "four", "five"],
        ["2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}\n")

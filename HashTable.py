class HashTable:
    def __init__(self,size = 7):
        self.data_map = [None] * size

    def __hash(self,key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def set_item(self,key,value):
        key_value_list = [key,value]
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append(key_value_list)

    def get_item(self,key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []

        for hash in self.data_map:
            if hash is not None:
                for inner_hash_list in hash:
                    all_keys.append(inner_hash_list[0])
        return all_keys

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i,": ",val)


my_hash= HashTable()
my_hash.set_item("bolts",1200)
my_hash.set_item("washers",50)
my_hash.set_item("lumber",88)
my_hash.print_table()

print(my_hash.get_item("bolts"))
print(my_hash.keys())

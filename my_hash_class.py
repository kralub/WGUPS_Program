# Caleb Bayles ID: 001271009 WORKS

# set up using Joe James' video on youtube about hash functions

# hash will need to have:
# id as key,
# delivery add.,
# delivery deadline,
# delivery city,
# delivery state,
# delivery zipcode,
# package weight,
# delivery status(delivered, en route, at hub)
# note
# start time
# deliver time

# it needs 10 values including 0

class MyHash:
    # initialize hash O(1)
    def __init__(self):
        self.map = []
        for i in range(10):
            self.map.append([])

    # find the key for the values, where it will go in the table O(n)
    def __get_hash(self, key):
        # print('we here')
        the_hash = int(key) % len(self.map)
        return the_hash

    # adding package to the hash table O(n)
    def add_to_hash(self, key, value):
        key_hash = self.__get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            self.map[key_hash].append(key_value)
            return True

    # now we need a way to get a hash value O(n)
    def get_package(self, key):
        key_hash = self.__get_hash(key)
        # get value if pair is there
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if int(pair[0]) == key:
                    return pair[1]
        # if key isn't found then it will print not found
        print('package not found!')
        return True

    # function to delete packages O(n)
    def delete_package(self, key):
        key_hash = self.__get_hash(key)
        # if key isnt found
        if self.map[key_hash] is None:
            print('key not found')
            return False
        # if it is found
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                print(key, ' has been deleted.')
                return True

    # printing all packages has to be done like so the_package_hash.print() O(n)
    def print(self):
        print('the packages: ')
        for item in self.map:
            if item is not None:
                print(str(item))

    # this is used when we need to update a hash value O(n)
    def update(self, key, value):
        my_hash = self.__get_hash(key)
        if self.map[my_hash] is not None:
            for pair in self.map[my_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
        else:
            print('ERROR!')

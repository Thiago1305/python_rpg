class Character:
    def __init__(self, name, age: int, friends: list):
        self.__name = name
        self.__age = age
        self.__friends = friends
    
    def get_friends(self):
        return self.__friends
    
    def add_friend(self, newFriend):
        if newFriend in self.__friends:
            print(f"{newFriend} já é seu amigo(a)")
        else:
            self.__friends.append(newFriend)

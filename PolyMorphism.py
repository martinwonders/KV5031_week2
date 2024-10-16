class GameItem:
    def __init__(self, type):
        self.type = type

    def use(self):
        raise NotImplementedError("Subclasses must implement this method")


class Weapon(GameItem):
    def __init__(self, name):
        super().__init__("Weapon")
        self.name = name

    def use(self):
        print(f"Attacking with your {self.name}!")

class Armor(GameItem):
    def __init__(self):
        super().__init__("Armor")

    def use(self):
        print("You are now protected by armor!")

class Potion(GameItem):
    def __init__(self, name):
        super().__init__("Potion")
        self.name = name

    def use(self):
        print(f"using a {self.name} potion!")

actions = [Weapon("sword"), Armor(), Potion("healing"), Weapon("knife"), Potion("boost")]

for action in actions:
    action.use()

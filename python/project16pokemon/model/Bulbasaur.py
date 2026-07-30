class Bulbasaur:
    def __init__(self):
        self.name = "이상해씨"
        self.atk = 500
        self.hp = 1000

    def __str__(self):
        return f"{self.name} {self.atk} {self.hp}"
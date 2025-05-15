class Diamond:
    def __init__(self, count: int = 1):
        if count < 0:
            raise ValueError("Number of diamonds cannot be negative.")
        self.count = count

    def get_diamonds(self):
        return self.count

    def set_diamonds(self, count: int):
        if count < 0:
            raise ValueError("Number of diamonds cannot be negative.")
        self.count = count

    def __str__(self):
        return f"Number of Diamonds: {self.count}"

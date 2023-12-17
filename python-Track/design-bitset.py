class Bitset:
    def __init__(self, size: int):
        self.bits = [0] * size
        self.count_on = 0
        self.size = size
        self.flipped = False

    def fix(self, idx: int) -> None:
        if self.flipped:
            if self.bits[idx] == 1:
                self.count_on += 1
                self.bits[idx] = 0
        else:
            if self.bits[idx] == 0:
                self.count_on += 1
                self.bits[idx] = 1

    def unfix(self, idx: int) -> None:
        if self.flipped:
            if self.bits[idx] == 0:
                self.count_on -= 1
                self.bits[idx] = 1
        else:
            if self.bits[idx] == 1:
                self.count_on -= 1
                self.bits[idx] = 0

    def flip(self) -> None:
        self.flipped = not self.flipped
        self.count_on = self.size - self.count_on

    def all(self) -> bool:
        return self.size == self.count_on

    def one(self) -> bool:
        return self.count_on > 0

    def count(self) -> int:
        return self.count_on

    def toString(self) -> str:
        s = ""
        for bit in self.bits:
            if self.flipped:
                s += "0" if bit else "1"
            else:
                s += "1" if bit else "0"
        return s

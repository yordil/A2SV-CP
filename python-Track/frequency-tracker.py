class FrequencyTracker:

    def __init__(self):
        self.freq = defaultdict(int)
        self.freq2 = defaultdict(int)

    def add(self, number: int) -> None:
        old_freq = self.freq[number]
        new_freq = old_freq + 1
        self.freq[number] = new_freq
        self.freq2[old_freq] -= 1
        self.freq2[new_freq] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.freq and self.freq[number] > 0:
            old_freq = self.freq[number]
            new_freq = old_freq - 1
            self.freq[number] = new_freq
            self.freq2[old_freq] -= 1
            self.freq2[new_freq] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq2 and self.freq2[frequency] > 0

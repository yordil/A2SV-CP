class ATM:
    def __init__(self):
        self.myhash = defaultdict(int)
        self.money = [500, 200, 100, 50, 20]

    def deposit(self, banknotesCount):
        j = 4
        for i, money in enumerate(self.money):
            self.myhash[money] += banknotesCount[j-i]

    def withdraw(self, amount):
        withdrawals = [0] * 5
        for i, m in enumerate(self.money):
            num = min(self.myhash[m], amount // m)
            amount -= num * m
            withdrawals[i] = num
            self.myhash[m] -= num

        if amount == 0:
            return withdrawals[::-1]
        else:
            # Roll back the changes
            for i, j in enumerate(self.money):
                self.myhash[j] += withdrawals[i]
            return [-1]



# on the way know what greedy algorithm is










# previous bad*s implmentation not passed

# class ATM:
#     def __init__(self):
#         self.myhash = defaultdict(int)

#     def deposit(self, banknotesCount: List[int]) -> None:
#         t, f, o, two, five = banknotesCount
#         self.myhash[20] = t
#         self.myhash[50] = f
#         self.myhash[100] = o
#         self.myhash[200] = two
#         self.myhash[500] = five

#     def withdraw(self, amount: int) -> List[int]:
#         cpy = int(amount)
#         arr = [0] * 5
#         first = amount // 500
#         amount -= first * 500
#         second = amount // 200
#         amount -= second * 200
#         third = amount // 100
#         amount -= third * 100
#         fourth = amount // 50
#         amount -= fourth * 50
#         fifth = amount // 20
#         amount -= fifth * 20
        
#         Sum = 0

#         if self.myhash[500] >= first:
#             self.myhash[500] -= first
#             arr[4] = first
#             Sum += first * 500
#         if self.myhash[200] >= 1:
#             self.myhash -= min(self.myhash[second])
#             self.myhash[200] -= second
#             arr[3] = second
#             Sum += second * 200  # Corrected
#         if self.myhash[100] >= third:
#             self.myhash[100] -= third
#             arr[2] = third
#             Sum += third * 100  # Corrected
#         if self.myhash[50] >= fourth:
#             self.myhash[50] -= fourth
#             arr[1] = fourth
#             Sum += fourth * 50
#         if self.myhash[20] >= fifth:
#             self.myhash[20] -= fifth
#             arr[0] = fifth
#             Sum += fifth * 20

#         print(Sum)
#         return arr if Sum == cpy else [-1]  # Corrected

# # Example usage:
# # obj = ATM()
# # obj.deposit([10, 5, 3, 2, 1])
# # result = obj.withdraw(370)
# # print(result)

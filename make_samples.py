import os
os.makedirs("samples", exist_ok=True)
a = '''def total(nums):
    s = 0
    for n in nums:
        s = s + n
    return s

def average(nums):
    return total(nums) / len(nums)

print(average([1, 2, 3, 4]))
'''
c = '''# calculates stuff
def add_all(values):
    result = 0  # start
    for v in values:
        result = result + v
    return result

def mean(values):
    return add_all(values) / len(values)

print(mean([5, 6, 7, 8]))
'''
d = '''def average(nums):
    return total(nums) / len(nums)

def total(nums):
    s = 0
    for n in nums:
        s = s + n
    return s

print(average([1, 2, 3, 4]))
'''
e = '''import random
words = ["cat", "dog", "bird"]
class Game:
    def __init__(self):
        self.pick = random.choice(words)
    def guess(self, w):
        return w == self.pick
g = Game()
print(g.guess("cat"))
'''
for name, code in [("a.py", a), ("b.py", a), ("c.py", c), ("d.py", d), ("e.py", e)]:
    open("samples/" + name, "w").write(code)
    
from sortedcontainers import SortedSet

class NumberContainers:

    def __init__(self):
        self.nums: Dict[int, Set[int]] = {} # {val: List[index]}
        self.indexes: Dict[int, int] = {} # {index: val}

    def change(self, index: int, number: int) -> None:
        prev_num = self.indexes.get(index)
        if prev_num is not None:
            self.nums[prev_num].remove(index)
            if not self.nums[prev_num]:
                del self.nums[prev_num]

        self.indexes[index] = number
        if self.nums.get(number) is None:
            self.nums[number] = SortedSet([index])
        else:
            self.nums[number].add(index)

    def find(self, number: int) -> int:
        if self.nums.get(number):
            return self.nums[number][0]
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
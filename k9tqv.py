"""Simulated plagiarism-like sample for analysis tools."""

def two_sum(nums, target):
    lookup = {}
    for i, value in enumerate(nums):
        required = target - value
        if required in lookup:
            return [lookup[required], i]
        lookup[value] = i
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))

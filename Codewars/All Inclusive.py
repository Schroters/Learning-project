# All Inclusive?
# https://www.codewars.com/kata/5700c9acc1555755be00027e
# A boolean true if all rotations of strng are included in arr


def contain_all_rots(strng, arr):
    everything = []
    for i in range(len(strng)):     # classic rotation of a string
        everything.append(strng[i:] + strng[:i])
    print(everything)
    for i in everything:
        if arr.count(i) == 0:
            return False
    return True


print(contain_all_rots("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]))   # True
print(contain_all_rots("XjYABhR", ["TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX", "XjYABhR", "ABhRXjY"]))  # False
print(contain_all_rots("", ["bsjq", "qbsj"]))     # True
print(contain_all_rots("", []))    # True

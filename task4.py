s = "anagram"
t = "nagaram"
#______________________-

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    count = [0] * 26

    for char in s:
        count[ord(char) - ord('a')] += 1

    for char in t:
        index = ord(char) - ord('a')
        count[index] -= 1
        if count[index] < 0:
            return False

    return True


print(isAnagram(s, t))
# 11/33 FAILED tests
def makePalindrome(s, n):
    changes = 0
    mid = None
    s = list(s)
    if len(s) % 2 == 0:
        s_even = list(s)
    else:
        mid_pos = len(s)//2
        mid = s[mid_pos]
        s_even = list(s[0:mid_pos] + s[mid_pos+1:])
    for dig_pos in range(0, int(len(s_even)/2)):
        if s_even[dig_pos] != s_even[-(dig_pos+1)]:
            maxi = max(s_even[dig_pos], s_even[-(dig_pos+1)])
            s_even[dig_pos] = maxi
            s_even[-(dig_pos+1)] = maxi
            changes += 1
    return changes, s_even, mid


def directHigh(s, n):
    s = list(s)
    for i in range(0, 10):
        pass


def highestValuePalindrome(s, n, k):
    # Write your code here
    changes, s_even, mid = makePalindrome(s, n)
    if changes > k:
        return "-1"
    elif changes == k:
        if mid is not None:
            return "".join(s_even[0:int(len(s_even)/2)]+[mid]+s_even[int(len(s_even)/2):])
        else:
            return "".join(s_even)
    elif changes < k:
        left = k-changes
        rem, quo = left % 2, left//2
        pos = 0
        while quo > 1:
            if pos+1 > len(s_even)/2:
                break
            if s_even[pos] != "9":
                s_even[pos] = "9"
                s_even[-(pos+1)] = "9"
                quo -= 1
                pos += 1
            else:
                pos += 1
        left = min(rem+quo, 1)

        if left == 1 and mid is not None:
            return "".join(s_even[0:int(len(s_even)/2)]+["9"]+s_even[int(len(s_even)/2):])
        elif left == 0 and mid is not None:
            return "".join(s_even[0:int(len(s_even)/2)]+[mid]+s_even[int(len(s_even)/2):])
        elif mid is None:
            return "".join(s_even)


if __name__ == "__main__":
    print(makePalindrome("092282", 4))

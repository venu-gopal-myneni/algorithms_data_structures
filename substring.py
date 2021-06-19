import time
import random
import string


def timeit(func):
    def timed(*args, **kw):
        ts = time.time()
        result = func(*args, **kw)
        te = time.time()

        print('%r  %2.2f ms' % (func.__name__, (te - ts) * 1000))
        return result
    return timed


@timeit
def naive(sub_str, full_str):
    '''
        complexity = len(sub_str) * len(full_str)
    '''
    lsub = len(sub_str)
    lfull = len(full_str)
    for i in range(0, lfull-lsub+1):
        if sub_str == full_str[i:lsub+i]:
            print("Pattern found at index " + str(i))


d = 256

# pat  -> pattern
# txt  -> text
# q    -> A prime number


@timeit
def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0    # hash value for pattern
    t = 0    # hash value for txt
    h = 1

    # The value of h would be "pow(d, M-1)%q"
    for i in range(M-1):
        h = (h*d) % q

    # Calculate the hash value of pattern and first window
    # of text
    for i in range(M):
        p = (d*p + ord(pat[i])) % q
        t = (d*t + ord(txt[i])) % q

    # Slide the pattern over text one by one
    for i in range(N-M+1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if p == t:
            # Check for characters one by one
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break
                else:
                    j += 1

            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j == M:
                print("Pattern found at index " + str(i))

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M])) % q

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t+q


if __name__ == "__main__":
    ss = 200000
    fs = 20000000
    sub_str = ''.join(random.choices(
        string.ascii_uppercase, k=ss))
    full_str = ''.join(random.choices(
        string.ascii_uppercase, k=fs))
    # print(sub_str)
    naive(sub_str, full_str)
    print("KR : ")
    search(sub_str, full_str, 61)

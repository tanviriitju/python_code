def count_substring(txt, pat):
    M = len(pat)
    N = len(txt)

    lps = [0] * M
    j = 0  # index for pat[]
    #print(type(lps))
    computeLPSArray(pat, M, lps)
    pe = 0
    i = 0  # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            pe += 1
            j = lps[j - 1]
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    # print(pe)
    return pe


def computeLPSArray(pat, M, lps):
    len = 0

    lps[0]
    i = 1

    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1

string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)

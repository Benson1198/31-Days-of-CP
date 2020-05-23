def marsExploration(s):
    count = 0
    expect = "SOS"
    i = 0
    while i < len(s):
        if s[i:i + 3] == expect:
            i = i+3
        else:
            j = 0
            while j < 3:
                if s[i] != expect[j]:
                    count += 1
                i += 1
                j += 1
    return count 

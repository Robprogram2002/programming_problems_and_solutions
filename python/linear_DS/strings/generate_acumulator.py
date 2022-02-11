# 5._ The examples below show you how to write function accum:

# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accumulator(s: str) -> str:
    return '-'.join((s[k].upper() + s[k].lower() * k) for k in range(len(s)))


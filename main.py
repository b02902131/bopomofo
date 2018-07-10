from .loader import words
import sys


def trans_word(text):
    if text in words:
        return words[text]
    else:
        return text

# Bigyo:
# 看起來他是前面如果沒字才往後加 buffer
# 但也不太確定
# 之後有需要再改
# 先擺著

def trans_sentense(text):
    ret = ""
    buf = ""
    for x in text:
        if x not in words:
            ret = ret + ' ' + trans_word(buf)
            buf = ""
            ret = ret + ' ' + trans_word(x)
            continue
        if buf + x not in words:
            ret = ret + ' ' + trans_word(buf)
            buf = x
        else:
            buf = buf + x
    ret = ret + ' ' + trans_word(buf)
    return ret[1:]

if __name__ == "__main__":
    while True:
        x = input(">>> ")
        print(trans_sentense(x))

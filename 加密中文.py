from xpinyin import Pinyin

def jia(i):
    p = Pinyin()
    a = ""
    result1 = p.get_pinyin(i)
    result = p.get_pinyin(i, tone_marks='marks')
    for i in range(0, len(result1), 2):
        a += result1[i]
    for i in range(1, len(result1), 2):
        a += result1[i]
    a += "|"
    for i in range(0, len(result1), 2):
        a += result[i]
    for i in range(1, len(result1), 2):
        a += result[i]
    return a


print(jia("我很牛逼"))

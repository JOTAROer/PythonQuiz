#10.利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
from collections import Counter
import re

string = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"

words = re.findall(r'\w+', string)

word_counts = Counter(words)

print(word_counts)

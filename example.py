from information_summary_filter.memory_filter import MemoryFilter

filter = MemoryFilter()
data = ['111','qwe','222','333','qwe']

for d in data:
    if filter.is_exists(d):
        print('no',d)
    else:
        filter.save(d)
        print('ok',d)

from bloom_filter import Bloom_filter

filter = Bloom_filter()
data = ['111','qwe','222','333','qwe']
for d in data:
    if filter.is_exist(d):
        print('no',d)
    else:
        filter.save(d)
        print('ok',d)

# information_summary_filter

# 实现请求过滤封装
1 MemoryFilter python内存去重
2 RedisFilter  redis去重
3 MySQLFilter  mysql去重
4 Bloom_filter 布隆过滤器

save() 保存数据 
is_exite() 判断数据是否存在


exapmle：
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

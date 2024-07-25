# 给定两个扭结的 PD_CODE
# 计算他们连通和的 PD_CODE

import json
from input_sanity import input_sanity
from in_out_code  import in_out_code

def __renumber(pd_code: list) -> list: # 对 PD_CODE 中的弧线从 1 开始重新编号
    int_val = []
    for crossing in pd_code:           # 获得所有出现过的弧线编号
        for x in crossing:
            if x not in int_val:
                int_val.append(x)
    int_val = sorted(int_val)           # 把编号重新排序
    int_dic = {}
    for idx, val in enumerate(int_val): # 构建编号映射
        int_dic[val] = idx + 1          # 保证编号为从 1 开始的一段连续自然数
    new_pd_code = []
    for crossing in pd_code:            # 对所有弧线进行重新编号
        new_crossing = [int_dic[x] for x in crossing]
        new_pd_code.append(new_crossing)
    return new_pd_code

def __max_arc_index(pd_code: list) -> int: # 获得最大的弧线编号
    return max([max(crossing) for crossing in pd_code])

def __shift_arc_index(pd_code: list, shift_len: int) -> list: # 对所有编号进行整体平移
    new_pd_code = []
    for crossing in pd_code:
        new_crossing = [x + shift_len for x in crossing]
        new_pd_code.append(new_crossing)
    return new_pd_code

def __get_in_out_code(pd_code:list) -> list:
    return in_out_code(pd_code)

def __update(pd_code, in_out_code, val_old, status, val_new): # 更新一个位置
    assert status in ["IN", "OUT"]
    new_pd_code = json.loads(json.dumps(pd_code))
    for i in range(len(pd_code)):
        for j in range(4):
            if pd_code[i][j] == val_old and in_out_code[i][j] == status:
                new_pd_code[i][j] = val_new
    return new_pd_code

# 假定 pd_code1 和 pd_code2 都满足编号连续
# 且 pd_code1 的最小弧线编号为 1
# 且 pd_code2 的最小弧线编号为 n1 + 1
# 将两个 pd_code 合并得到连通和的 pd_code
def __merge_pd_code(pd_code1, pd_code2, n1, n2) -> list:
    in_out_code1 = __get_in_out_code(pd_code1) # 获得与 pd_code 结构一致的 in_out_code
    in_out_code2 = __get_in_out_code(pd_code2)
    new_pd_code1 = __update(pd_code1, in_out_code1, 1   , "OUT", n1 + 1)
    new_pd_code2 = __update(pd_code2, in_out_code2, n1+1, "OUT",      1)
    return new_pd_code1 + new_pd_code2

# 计算两个扭结的连通和
# 这个算法不一定正确，这个算法假定两个扭结的 1 号弧线都位于扭结的 “最外圈
# 将来可能会对这个算法进行必要的修改
def connected_sum(pd_code1: list, pd_code2: list) -> list:
    pd_code1 = input_sanity(pd_code1)           # 对输入数据的格式进行必要的检查
    pd_code2 = input_sanity(pd_code2)
    if len(pd_code1) < len(pd_code2):
        pd_code1, pd_code2 = pd_code2, pd_code1 # 让 pd_code2 中存储的 list 更短
    if len(pd_code2) == 0:                      # 考虑平凡扭结的连通和情况
        return pd_code1
    pd_code1 = __renumber(pd_code1)             # 对 PD_CODE 中的所有弧线，进行重编号
    pd_code2 = __renumber(pd_code2)
    n1       = __max_arc_index(pd_code1)        # 计算两个扭结的最大弧线编号
    n2       = __max_arc_index(pd_code2)
    pd_code2 = __shift_arc_index(pd_code2, n1)  # 对所有第二个扭结中的编号 + n1
    return __merge_pd_code(pd_code1, pd_code2, n1, n2)

if __name__ == "__main__":
    print(connected_sum(
        [[1,5,2,4],[3,9,4,8],[5,11,6,10],[7,3,8,2],[9,7,10,6],[16,14,1,13],[14,12,15,11],[12,16,13,15]],
        [[1, 5, 2, 4], [3, 9, 4, 8], [5, 1, 6, 10], [7, 3, 8, 2], [9, 7, 10, 6]]
    ))

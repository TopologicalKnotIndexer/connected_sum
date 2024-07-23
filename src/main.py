# 从标准输入读入两行，每行为一个扭结的 PD_CODE
# 输出这两个扭结的连通和的 PD_CODE（算法正确性有待测试）

import sys
from connected_sum import connected_sum

# 我们并不能保证这个扭结连通和算法的正确性
# 因此当有 sage 可用时，我们强烈建议使用 sage 提供的连通和算法
def main():
    pd_code1 = sys.stdin.readline() # 输入两行，每行包含一个扭结的 PD_CODE
    pd_code2 = sys.stdin.readline()
    print(connected_sum(pd_code1, pd_code2))

if __name__ == "__main__":
    main()
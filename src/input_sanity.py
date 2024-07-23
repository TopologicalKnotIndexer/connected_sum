# 桥接：https://github.com/TopologicalKnotIndexer/pd_code_input_sanity
import os
DIRNOW = os.path.dirname(os.path.abspath(__file__))
SUBDIR = os.path.join(DIRNOW, "pd_code_input_sanity", "src") # 子包路径


# ======================================== BEGIN IMPORT FROM PATH ======================================== #
import importlib
import json
import sys
def load_module_from_path(path: str, mod_name: str): # 从指定路径导入一个包
    assert os.path.isdir(path)                       # 路径必须存在
    path         = os.path.abspath(path)             # 获得绝对路径
    old_sys_path = json.loads(json.dumps(sys.path))  # 存档旧的 sys.path
    sys.path     = [path] + sys.path                 # 将新的路径加入 sys.path
    mod          = importlib.import_module(mod_name) # 加载指定的包
    sys.path     = old_sys_path                      # 恢复旧的 sys.path
    return mod
# ======================================== END IMPORT FROM PATH ======================================== #



# 如果 PD_CODE 字符串合法，返回字符串形式的 PD_CODE
# 否则报错
def input_sanity(pd_code_value) -> list:
    if not isinstance(pd_code_value, str): # 考虑如果输入的数据不是字符串，那就将其转化为字符串
        pd_code_value = str(pd_code_value)
    return load_module_from_path(SUBDIR, "pd_code_input_sanity").input_sanity(pd_code_value)

if __name__ == "__main__":
    print(input_sanity([]))
    print(input_sanity([[1, 2, 2, 1]])) # 不会报错
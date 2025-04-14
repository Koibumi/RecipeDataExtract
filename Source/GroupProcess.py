from DataStructures import *

def flatten_group(group: GroupView) -> List[str]:
    """
    将 GroupView 对象转换为列表形式，方便写入 CSV：
    - name: 组名称
    - items: 对于 items 中的每个 ItemView，只使用item名称，使用分号拼接
    """
    name_str = group.name
    items_str = ";".join(f"{item.item}" for item in group.items)
    return [name_str, items_str]

def process_groups(groups: list[GroupView]) -> List[List[str]]:
    '''
    处理 GroupView 对象列表：
      对每个对象调用 flatten_group 得到 CSV 行（列表形式）
    返回：
      - flat_rows: 二维列表，每个子列表为一行 CSV 数据
    '''
    flat_rows = []
    for group in groups:
        row = flatten_group(group)
        flat_rows.append(row)
    
    return flat_rows
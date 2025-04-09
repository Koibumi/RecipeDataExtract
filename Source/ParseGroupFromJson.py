from DataStructures import *
import json

def load_groups_from_json(file_path: str) -> list:
    """
    从给定的 JSON 文件中读取数据，
    文件内容应为一个包含序列化 GroupView 对象的 JSON 列表，
    并返回 GroupView 实例的集合。
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    groups = {parse_group(group_dict) for group_dict in data}
    return groups
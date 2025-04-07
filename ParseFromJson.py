from DataStructures import *
import json

def parse_item(item_dict: dict) -> ItemView:
    """将 JSON 中表示 ItemView 的字典转换为 ItemView 实例"""
    return ItemView(
        item=item_dict["item"],
        quantity=item_dict["quantity"]
    )

def parse_recipe(recipe_dict: dict) -> RecipeView:
    """
    将 JSON 中表示 RecipeView 的字典转换为 RecipeView 实例。
    注意：JSON 中的键 'output' 对应 Python 中的字段 result，
    'workstations'、'conditions' 和 'ingredients' 会分别转换为 set 类型。
    """
    workstations = frozenset(recipe_dict.get("workstations", []))
    conditions = frozenset(recipe_dict.get("conditions", []))
    # 'output' 键对应 result 字段
    result = parse_item(recipe_dict["output"]) if "output" in recipe_dict else None
    # 'ingredients' 是一个包含字典的列表，转换为 ItemView 的 frozenset
    ingredients = frozenset({parse_item(item) for item in recipe_dict.get("ingredients", [])})
    version = recipe_dict.get("version", "")
    return RecipeView(workstations, conditions, result, ingredients, version)

def load_recipes_from_json(file_path: str) -> list:
    """
    从给定的 JSON 文件中读取数据，
    文件内容应为一个包含序列化 RecipeView 对象的 JSON 列表，
    并返回 RecipeView 实例的列表。
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # data 应为一个字典列表，逐个转换为 RecipeView 实例
    recipes = {parse_recipe(recipe_dict) for recipe_dict in data}
    return recipes
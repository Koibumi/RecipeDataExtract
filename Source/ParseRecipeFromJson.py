from DataStructures import *
import json

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
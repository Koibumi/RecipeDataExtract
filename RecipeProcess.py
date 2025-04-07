from DataStructures import *

def update_recipes(old: set[RecipeView], new: set[RecipeView]) -> set[RecipeView]:
    """
    基于 old 集合更新，并加入 new 集合中的 RecipeView 对象：
      - 如果 new 中的对象与 old 中的某对象“相等”（不考虑 version 字段），
        则用 new 中的对象替换 old 中的对象；
      - 其他对象保持共存。
    返回更新后的 RecipeView 集合。
    """
    updated = set(old)
    for recipe in new:
        if recipe in updated:
            # 如果存在相等的对象，则先移除旧对象，再加入新的对象
            updated.remove(recipe)
        updated.add(recipe)
    return updated

# 压平函数，将 RecipeView 对象转换为列表形式，方便写入 CSV
def flatten_recipe(recipe: RecipeView) -> List[str]:
    """
    返回一个列表，每个元素对应 CSV 中的一个字段：
      - workstations: 使用分号拼接字符串
      - conditions: 使用分号拼接字符串
      - result: 格式为 "item:quantity"（如果存在，否则为空字符串）
      - ingredients: 对于 ingredients 中的每个 ItemView，以 "item:quantity" 格式表示，使用分号拼接
      - version: 原始 version 字段
    """
    workstations_str = ";".join(recipe.workstations)
    conditions_str = ";".join(recipe.conditions)
    result_str = f"{recipe.result.item}:{recipe.result.quantity}" if recipe.result else ""
    ingredients_str = ";".join(f"{ing.item}:{ing.quantity}" for ing in recipe.ingredients)
    return [workstations_str, conditions_str, result_str, ingredients_str, recipe.version]

def process_recipes(recipes_set: Set[RecipeView]
                   ) -> Tuple[List[List[str]], dict, dict]:
    """
    处理 RecipeView 对象集合：
      1. 将集合转换为列表，并对每个对象调用 flatten_recipe 得到 CSV 行（列表形式）；
      2. 为 workstations 和 ingredients 分别建立倒排索引，
         键为名称，值为包含该名称的 RecipeView 对象在列表中的 index 列表。
    返回：
      - flat_rows: 二维列表，每个子列表为一行 CSV 数据；
      - workstation_index: {workstation_name: [index, ...]} 倒排索引；
      - ingredient_index: {ingredient_name: [index, ...]} 倒排索引。
    """
    recipes_list = list(recipes_set)
    flat_rows = []
    workstation_index = {}  # workstation_name -> list of row indices
    ingredient_index = {}   # ingredient_name -> list of row indices

    for idx, recipe in enumerate(recipes_list):
        row = flatten_recipe(recipe)
        flat_rows.append(row)
        
        for ws in recipe.workstations:
            workstation_index.setdefault(ws, []).append(idx)
        for ing in recipe.ingredients:
            ingredient_index.setdefault(ing.item, []).append(idx)
    
    return flat_rows, workstation_index, ingredient_index

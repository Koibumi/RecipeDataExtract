from RecipeProcess import *
from openpyxl import Workbook

def write_xlsx_files(flat_rows: List[List[str]],
                     workstation_index: dict,
                     ingredient_index: dict,
                     flattened_file: str = "flattened_recipes.xlsx",
                     workstation_file: str = "workstation_index.xlsx",
                     ingredient_file: str = "ingredient_index.xlsx") -> None:
    """
    将压平的 RecipeView 数据和倒排索引写入 XLSX 文件：
      - flattened_file: 每一行对应一个 RecipeView 对象（字段顺序为 workstations, conditions, result, ingredients, version）；
      - workstation_file: 每一行包含 workstation 名称和该名称在 flattened 表中的行索引（用分号分隔多个索引）；
      - ingredient_file: 每一行包含 ingredient 名称和对应的行索引（用分号分隔）。
    """
    # 写入压平后的 RecipeView 数据
    wb = Workbook()
    ws = wb.active
    ws.title = "Flattened Recipes"
    ws.append(["workstations", "conditions", "result", "ingredients", "version"])
    for row in flat_rows:
        ws.append(row)
    wb.save(flattened_file)

    # 写入 workstation 倒排索引
    wb = Workbook()
    ws = wb.active
    ws.title = "Workstation Index"
    ws.append(["workstation", "row_indices"])
    for ws_name, indices in workstation_index.items():
        ws.append([ws_name, ";".join(map(str, indices))])
    wb.save(workstation_file)

    # 写入 ingredient 倒排索引
    wb = Workbook()
    ws = wb.active
    ws.title = "Ingredient Index"
    ws.append(["ingredient", "row_indices"])
    for ing_name, indices in ingredient_index.items():
        ws.append([ing_name, ";".join(map(str, indices))])
    wb.save(ingredient_file)
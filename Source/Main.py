from WriteOutput import *
from ParseFromExcel import *
from ParseFromJson import *
import os

# 示例使用：
if __name__ == "__main__":
    # 假设 "old_recipes.xlsx" 和 "new_recipes.json" 分别保存了旧集合和新集合数据
    old_recipes_file = "../Data/old_recipes.xlsx"
    new_recipes_file = "../Data/new_recipes.json"
    
    # 尝试加载旧数据，如果文件不存在或加载失败，则使用空集合
    try:
        if os.path.exists(old_recipes_file):
            old_recipes = load_recipes_from_xlsx(old_recipes_file)
        else:
            print(f"{old_recipes_file} 不存在，使用空集合")
            old_recipes = set()
    except Exception as e:
        print(f"加载 {old_recipes_file} 失败，错误信息：{e}，使用空集合")
        old_recipes = set()
        
    new_recipes = load_recipes_from_json(new_recipes_file)
    
    combined_recipes = update_recipes(old_recipes, new_recipes)
    
    # 处理 RecipeView 集合，得到压平后的行和倒排索引
    flat_rows, ws_index, ing_index = process_recipes(combined_recipes)
    
    # 写入三个 CSV 文件
    write_xlsx_files(flat_rows, ws_index, ing_index, "../Output/recipes.xlsx", "../Output/recipes_ws_index.xlsx", "../Output/recipes_ing_index.xlsx")
    
    print("数据处理完成，文件已保存。")
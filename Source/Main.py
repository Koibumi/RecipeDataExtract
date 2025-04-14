from WriteOutput import *
from ParseRecipeFromExcel import *
from ParseRecipeFromJson import *
from ParseGroupFromJson import *
import os

# 示例使用：
if __name__ == "__main__":
    # 假设 "old_recipes.xlsx" 和 "new_recipes.json" 分别保存了旧集合和新集合数据
    old_recipes_file = "../Data/old_recipes.xlsx"
    new_recipes_file = "../Data/new_recipes.json"
    groups_file = "../Data/groups.json"
    
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
    
    try:
        if os.path.exists(groups_file):
            groups = load_groups_from_json(groups_file)
        else:
            print(f"{groups_file} 不存在，使用空集合")
            groups = []
    except Exception as e:
        print(f"加载 {groups_file} 失败，错误信息：{e}，使用空集合")
        groups = []
        
    combined_recipes = update_recipes(old_recipes, new_recipes)
    
    # 处理 RecipeView 集合
    flat_rows_recipes = process_recipes(combined_recipes)
    write_flattened_recipes(flat_rows_recipes, "../Output/recipes.xlsx")
    
    # 处理 GroupView 列表
    flat_rows_groups = process_groups(groups)
    write_flattened_groups(flat_rows_groups, "../Output/groups.xlsx")
    
    print("数据处理完成，文件已保存。")
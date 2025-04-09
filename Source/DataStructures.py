from dataclasses import dataclass, field
from typing import *

@dataclass(frozen=True)
class ItemView:
    item: str
    quantity: int
    
def parse_item(item_dict: dict) -> ItemView:
    """将 JSON 中表示 ItemView 的字典转换为 ItemView 实例"""
    return ItemView(
        item=item_dict["item"],
        quantity=item_dict["quantity"]
    )

@dataclass(frozen=True)
class RecipeView:
    workstations: frozenset = field(default_factory=frozenset)
    conditions: frozenset = field(default_factory=frozenset)
    result: Optional[ItemView] = None
    ingredients: frozenset = field(default_factory=frozenset)
    version: str = ""
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, RecipeView):
            return NotImplemented
        # 忽略 version 字段比较
        return (
            self.workstations == other.workstations and
            self.conditions == other.conditions and
            self.result == other.result and
            self.ingredients == other.ingredients
        )

    def __hash__(self) -> int:
        # 根据忽略 version 字段的内容生成 hash
        return hash((
            self.workstations,
            self.conditions,
            self.result,
            self.ingredients
        ))
   
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
     
@dataclass(frozen=True)
class GroupView:
    name: str
    items: frozenset[ItemView] = field(default_factory=frozenset)
    
def parse_group(group_dict: dict) -> GroupView:
    """
    将 JSON 中表示 GroupView 的字典转换为 GroupView 实例
    """
    name = group_dict["name"]
    # 'items' 是一个包含字典的列表，转换为 ItemView 的 frozenset
    items = frozenset({parse_item(item) for item in group_dict.get("items", [])})
    return GroupView(name, items)
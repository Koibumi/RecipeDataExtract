from dataclasses import dataclass, field
from typing import *

@dataclass(frozen=True)
class ItemView:
    item: str
    quantity: int

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
from dataclasses import dataclass, field
from datetime import date


@dataclass(order=True)
class Item:
    _sort_index: float = field(init=False, repr=False)
    name: str
    section: float
    name_addition: str = None


    def __post_init__(self):
        self._sort_index = self.section


@dataclass
class GroceryList:
    items: list[Item] = field(default_factory=list)
    date: date = field(default_factory=lambda: date.today())

    def sort(self):
        return sorted(self.items)

    def append(self, item: Item):
        self.items.append(item)

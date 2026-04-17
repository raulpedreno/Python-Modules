from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': lambda a, b: a if a > b else b,
        'min': lambda a, b: a if a < b else b
    }
    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    pass


@lru_cache
def memoized_fibonacci(n: int) -> int:
    pass


def spell_dispatcher() -> Callable[[Any], str]:
    pass


if __name__ == "__main__":
    # Aquí irán tus tests
    pass

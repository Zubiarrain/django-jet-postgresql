from collections.abc import Callable

def get_callable(lookup_view: Callable | str) -> Callable: ...
def get_mod_func(callback: str) -> tuple[str, str]: ...
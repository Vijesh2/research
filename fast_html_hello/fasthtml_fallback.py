"""Tiny subset of python-fasthtml used as a local fallback for tests."""
from __future__ import annotations

from html import escape
from typing import Tuple, Union

Renderable = Union[str, "_Tag"]


def _render_child(child: Renderable, depth: int) -> str:
    indent = "  " * depth
    if isinstance(child, _Tag):
        return child._render(depth)
    return f"{indent}{escape(str(child))}"


class _Tag:
    name: str = ""

    def __init__(self, *children: Renderable):
        self.children: Tuple[Renderable, ...] = tuple(children)

    def _render(self, depth: int = 0) -> str:
        indent = "  " * depth
        opening = f"<{self.name}>"
        closing = f"</{self.name}>"
        if not self.children:
            return f"{indent}{opening}{closing}"
        rendered_children = "\n".join(_render_child(child, depth + 1) for child in self.children)
        return f"{indent}{opening}\n{rendered_children}\n{indent}{closing}"

    def __str__(self) -> str:  # pragma: no cover - exercised indirectly via print()
        return self._render()


class Html(_Tag):
    name = "html"

    def __str__(self) -> str:  # pragma: no cover - exercised indirectly via print()
        return "<!DOCTYPE html>\n" + super().__str__()


class Main(_Tag):
    name = "main"


class Div(_Tag):
    name = "div"


class H1(_Tag):
    name = "h1"


class P(_Tag):
    name = "p"

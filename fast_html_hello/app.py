"""Minimal FastHTML hello-world example."""
from __future__ import annotations

import sys

try:
    from fasthtml.common import Div, H1, Html, Main, P  # type: ignore[import-not-found]
    USING_FALLBACK = False
except ModuleNotFoundError:
    from fasthtml_fallback import Div, H1, Html, Main, P

    USING_FALLBACK = True


def main() -> None:
    """Render a tiny HTML document and print it to stdout."""

    if USING_FALLBACK:
        print(
            "python-fasthtml is not installed; using bundled fallback renderer.",
            file=sys.stderr,
        )

    document = Html(
        Main(
            H1("FastHTML Hello-World"),
            Div(
                P("Hello from python-fasthtml!"),
                P(
                    "If you can read this message, your environment successfully imported the primitives.",
                ),
            ),
        )
    )

    print(document)


if __name__ == "__main__":
    main()

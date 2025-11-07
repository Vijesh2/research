A brief demonstration showcases how to use the [`python-fasthtml`](https://pypi.org/project/python-fasthtml/) package to programmatically generate HTML documents from Python. The included script serves as a simple "Hello World" example and is designed for quick validation of workflow setups or CI environments, requiring minimal setup (Python 3.9+ and the dependencies in `requirements.txt`). Notably, the script provides a lightweight built-in fallback renderer to ensure operability even in restricted or offline environments, alerting the user via stderr when dependencies cannot be installed. The output is a well-formed HTML file suitable for browser display.

**Key points:**
- Demonstrates reliable HTML rendering via Python, even under constrained conditions.
- Offers a compact fallback for environments where installing dependencies is not possible.
- Example is optimized for integration into automation or CI workflows.

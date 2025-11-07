# FastHTML Hello-World

This folder contains a minimal Python script that renders a short HTML document with [`python-fasthtml`](https://pypi.org/project/python-fasthtml/). It is meant to serve as a quick test for automation or workflow setups.

## Prerequisites

- Python 3.9+
- (Recommended) Install the dependencies listed in this folder's `requirements.txt`:

  ```bash
  pip install -r requirements.txt
  ```

  When the package cannot be installed (for example, in offline CI environments), the script ships with a tiny built-in fallback so the example still runs.

## Running the example

```bash
python app.py
```

If everything is installed correctly, the script prints a complete HTML document. When the fallback renderer is used, you will also see a short notice on stderr. The output should look similar to:

```html
<!DOCTYPE html>
<html>
  <main>
    <h1>
      FastHTML Hello-World
    </h1>
    <div>
      <p>
        Hello from python-fasthtml!
      </p>
      <p>
        If you can read this message, your environment successfully imported the primitives.
      </p>
    </div>
  </main>
</html>
```

You can pipe the output to a file (e.g., `python app.py > hello.html`) and open it in a browser to confirm the rendered page.

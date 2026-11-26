"""Root entrypoint for the Worst Pizza Topping entry.

The entry program itself lives in entry/main.py; this shim runs it so the
kit finds main.py at the repository root.
"""

import runpy

if __name__ == "__main__":
    runpy.run_path("entry/main.py", run_name="__main__")

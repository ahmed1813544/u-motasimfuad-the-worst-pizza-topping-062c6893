"""Entry for 'The Worst Pizza Topping' — writes one terrible topping pitch."""

import os

OUTPUT_PATH = "/output/entry.txt"


def topping_line() -> str:
    """The pitch: one topping nobody asked for, described with pride."""
    return (
        "A thick smear of room-temperature mayonnaise, trowelled on cold "
        "and finished with one unpeeled shrimp per slice: dinner and a "
        "dare in every bite."
    )


def main() -> None:
    line = topping_line()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()

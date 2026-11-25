# u-suzy-one-line-one-laugh-roast-your-fridge-f1063521: one single-line roast of
# a fridge, 1-199 characters. The program writes that single line to
# /output/entry.txt.
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Gate: the entry is one line of 1-199 characters.
MAX_CHARS = 199

# The roast: targets a fridge (not a generic insult), lands on a specific,
# recognisable detail (the fridge humming all night over almost nothing
# inside), turns on a twist in the last few words ("one very nervous
# carrot"), reads cleanly aloud as one line, and uses fresh wording rather
# than a joke already going round the internet.
JOKE = (
    "My fridge hums all night like a bodyguard for three sauces "
    "and one very nervous carrot."
)


def validate_joke(text):
    assert 1 <= len(text) <= MAX_CHARS, f"joke is {len(text)} chars, must be 1-{MAX_CHARS}"
    assert text.strip(), "joke must not be only whitespace"
    assert "\n" not in text, "joke must be a single line"


def main():
    validate_joke(JOKE)
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

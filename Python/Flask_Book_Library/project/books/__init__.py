import re

_TEXT = re.compile(r"[\w\s.,'\-:!?()]{1,64}")

def validate_text(value, field):
    if value is None or not _TEXT.fullmatch(value):
        raise ValueError(f"Invalid {field}")
    return value
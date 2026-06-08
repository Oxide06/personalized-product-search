import re
import pandas as pd


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9 ]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def tokenize(text):
    return clean_text(text).split()


def safe_extend(parts, value):

    if value is None:
        return

    if isinstance(value, float):
        if pd.isna(value):
            return

    if isinstance(value, str):
        parts.append(value)
        return

    try:
        for item in value:
            if item is not None:
                parts.append(str(item))
    except TypeError:
        parts.append(str(value))


def build_document(row):

    parts = []

    safe_extend(parts, row.get("title"))
    safe_extend(parts, row.get("store"))
    safe_extend(parts, row.get("main_category"))
    safe_extend(parts, row.get("categories"))
    safe_extend(parts, row.get("features"))
    safe_extend(parts, row.get("description"))

    return " ".join(parts)
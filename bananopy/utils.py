import re


def is_hex(s):
    return re.fullmatch(r"^[0-9a-fA-F]+$", s or "") is not None


def is_hash(s):
    return True if len(s) == 64 and is_hex(s) else False


def process_str(v):
    r = v
    if not is_hash(v) and v.isdigit():
        r = int(v)
    if v == "":
        r = {}
    return r


def fix_json(input):
    if isinstance(input, str):
        return process_str(input)

    r = {}
    for k, v in input.items():
        if isinstance(v, dict):
            r[k] = fix_json(v)
        elif isinstance(v, list):
            r[k] = [fix_json(el) for el in v]
        else:
            r[k] = process_str(v)
    return r

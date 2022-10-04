import re

CORE_TYPES = [int, str, bool, None, dict, list]



def snake(s: str):
    # https://stackoverflow.com/q/1175208
    s = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", s)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s).lower()


def camel(s: str):
    return "".join([i[0].upper() + i[1:] for i in s.split("_")])


def get_values(value):
    if type(value) not in CORE_TYPES:
        new_value = value.json()
    else:
        if type(value) == list:
            values = []
            for v in value:
                if type(value) not in CORE_TYPES:
                    values.append(v.json())
                else:
                    values.append(v)
            new_value = values
        else:
            new_value = value
    return new_value

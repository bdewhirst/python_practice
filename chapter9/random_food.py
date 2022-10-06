import random
import json


FOODS = [
    "pizza",
    "tacos",
    "tvp",
]


def to_json(food):
    return json.dumps({"food": food})


def to_xml(food):
    return f"<response><food>{food}</food></response>"


def get_format_function(accept=None):
    """
    A comment on the signature of the .get dictionary method:
    signature of .get dictionary method is Dict.get(key, default=None)
        so if you provide 2nd value (like a lambda function), it uses that as default
    """
    formats = {
        "application/json": to_json,
        "application/xml": to_xml,
    }
    return formats.get(accept, lambda val: val)


def random_food(request):
    food = random.choice(FOODS)
    format_function = get_format_function(accept=request.headers.get("Accept"))
    return format_function(food)

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


def random_food(request):
    food = random.choice(FOODS)
    formats = {
        "application/json": to_json,
        "application/xml": to_xml,
    }
    format_function = formats.get(request.headers.get("Accept"), lambda val: val)
    # i.e., lambda to return 'food' if app not found
    # signature of .get dictionary method is Dict.get(key, default=None) -- so if you provide 2nd value, uses as default

    return format_function(food)

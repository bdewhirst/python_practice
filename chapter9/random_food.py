import random
import json


FOODS = ["pizza", "tacos", "tvp",]


def random_food(request):
    food = random.choice(FOODS)

    formats = {
        "application/json": json.dumps({"food": food}),
        "application/xml": f"<response><food>{food}</food></response>",
    }

    return formats.get(request.headers.get("Accept"), food)
    # if request.headers.get("Accept") == "application/json":
    #     return json.dumps({"food": food})
    # elif request.headers.get("Accept") =='application/xml':
    #     return
    # else:
    #     return food
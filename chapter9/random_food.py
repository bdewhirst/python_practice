import random
import json


FOODS = ["pizza", "tacos", "tvp",]


def random_food(request):
    food = random.choice(FOODS)

    if request.headers.get("Accept") == "application/json":
        return json.dumps({"food": food})
    elif request.headers.get("Accept") =='application/xml':
        return f"<response><food>{food}</food></response>"
    else:
        return food
    return food
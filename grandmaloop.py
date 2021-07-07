kitchen= {"pan":"tool","spoon":"tool","yo-yo":"toy","banana":"food","jump rope":"toy","stove":"appliance"}

def grandma_loop():
    for key in kitchen:
        if kitchen[key] == "toy": print(f"Bad news. Grandma found a {key} in the kitchen")

def short_loop():
    for k, v in kitchen.items():
        if kitchen[k] == "toy": print(f"Bad news. Grandma found a {k} in the kitchen")

if __name__ == '__main__':
    grandma_loop()
    short_loop()

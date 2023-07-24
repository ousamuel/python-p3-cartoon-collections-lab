def roll_call_dwarves(list):
    num = 1
    for item in list:
        print(f"{num}. {item}")
        num+=1


def summon_captain_planet(list):
    return [(item.capitalize()) + "!" for item in list]

def long_planeteer_calls(list):
    for item in list:
        if len(item) > 4:
            return True
    return False

def find_the_cheese(list):
    cheeses = ['cheddar', 'gouda', 'camembert']
    for item in list:
       if (item in cheeses):
           return item
    return None

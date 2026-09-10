intro = "STORY ENGINE\nExpedition Supply Calculator"
print(intro)
name = (input("What is your character's name? "))
starting_gold = float(input("How much gold does your character have? "))
health_potions_want = int(input("How many health potions do they want? "))
health_potion_cost = float(input("What is the price of each health potion? "))
expedition_timeline = int(input("How many days will the expedition last? "))
daily_food_cost = float(input("What is the daily food cost? "))

total_potion_cost = health_potions_want * health_potion_cost
expedition_food_cost = expedition_timeline * daily_food_cost

expedition_cost = total_potion_cost + expedition_food_cost

remaining_gold = starting_gold - expedition_cost

print(
    f"========================\n"
    f"EXPEDITION SUPPLY REPORT\n"
    f"========================\n"
    f"Character: {name}\n"
    f"Staring Gold: {starting_gold}\n"
    f"Potion Cost: {total_potion_cost}\n"
    f"Food Cost: {expedition_food_cost}\n"
    f"Total Cost: {expedition_cost}\n"
    f"Gold Remaining: {remaining_gold}\n"
    f"========================"
)

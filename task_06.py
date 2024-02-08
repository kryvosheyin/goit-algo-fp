def greedy_algorithm(items, budget):
    # calculating calorie-to-cost ratio for each item
    ratios = {item: (info["calories"] / info["cost"]) for item, info in items.items()}
    # sorting items by their ratio in descending order
    sorted_items = sorted(ratios.items(), key=lambda x: x[1], reverse=True)

    selected_items = []
    total_cost = 0
    total_calories = 0

    for item, ratio in sorted_items:
        if total_cost + items[item]["cost"] <= budget:
            selected_items.append(item)
            total_cost += items[item]["cost"]
            total_calories += items[item]["calories"]
        else:
            break

    return {
        "Selected items": selected_items,
        "Total cost": total_cost,
        "Total calories": total_calories,
    }


def dynamic_programming(items, budget):

    item_list = list(items.items())
    num_items = len(item_list)
    dp_table = [[0] * (budget + 1) for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        item_name, item_info = item_list[i - 1]
        item_cost, item_calories = item_info["cost"], item_info["calories"]
        for budget_left in range(1, budget + 1):
            if item_cost > budget_left:
                dp_table[i][budget_left] = dp_table[i - 1][budget_left]
            else:
                dp_table[i][budget_left] = max(
                    dp_table[i - 1][budget_left],
                    dp_table[i - 1][budget_left - item_cost] + item_calories,
                )

    selected_items = []
    budget_left = budget
    total_cost = 0
    total_calories = 0

    for i in range(num_items, 0, -1):
        item_name, item_info = item_list[i - 1]
        item_cost, item_calories = item_info["cost"], item_info["calories"]
        if dp_table[i][budget_left] != dp_table[i - 1][budget_left]:
            selected_items.append(item_name)
            budget_left -= item_cost
            total_cost += item_cost
            total_calories += item_calories

    selected_items.reverse()

    return {
        "selected_items": selected_items,
        "total_cost": total_cost,
        "total_calories": total_calories,
    }


def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    print(f"Greedy Algorithm Result: {greedy_algorithm(items, 300)}")
    print(f"Dynamic Programming Result: {dynamic_programming(items, 300)}")


if __name__ == "__main__":
    main()

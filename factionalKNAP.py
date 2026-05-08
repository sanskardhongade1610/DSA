class Item:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit
        self.ratio = profit / weight


def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_profit = 0.0
    remaining_capacity = capacity

    print("\nSelected Parcels:")
    print("Weight\tProfit\tTaken")

    for item in items:
        if item.weight <= remaining_capacity:
            remaining_capacity -= item.weight
            total_profit += item.profit
            print(f"{item.weight}   \t{item.profit}   \t100%")
        else:
            fraction = remaining_capacity / item.weight
            total_profit += item.profit * fraction
            print(f"{item.weight}    \t{item.profit}    \t{fraction*100:.2f}%")
            break  # Truck is full

    return total_profit

if __name__ == "__main__":
    parcels = [
        (10, 60),
        (20, 100),
        (30, 120),
        (50, 300)
    ]

    items = [Item(weight, profit) for weight, profit in parcels]        

    capacity = 50

    print("Parcels (Weight, Profit):", parcels)
    max_profit = fractional_knapsack(items, capacity)

    print(f"\nMaximum Profit that can be earned = {max_profit}")

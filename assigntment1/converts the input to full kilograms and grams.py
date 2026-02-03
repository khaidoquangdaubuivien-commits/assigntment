talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
total_lots = (talents * 20 + pounds) * 32 + lots
total_grams = total_lots * 13.3
kg = int(total_grams // 1000)
gr = total_grams % 1000
print(f"The weight in modern units: {kg} kilograms and {gr:.2f} grams.")
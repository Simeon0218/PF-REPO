weight = float(input())
service_type = input()
destination_range = float(input())

total = 0
standard_charge = 0
express_charge = 0

if weight < 1:
    standard_charge += 0.03 * destination_range
    total += standard_charge
elif weight <= 10:
    standard_charge += 0.05 * destination_range
    total += standard_charge
elif weight <= 40:
    standard_charge += 0.10 * destination_range
    total += standard_charge
elif weight <= 90:
    standard_charge += 0.15 * destination_range
    total += standard_charge
elif weight <= 150:
    standard_charge += 0.20 * destination_range
    total += standard_charge

if service_type == "express":
    if weight < 1:
        express_charge = 0.03 * 0.8 * weight * destination_range
    elif weight < 10:
        express_charge = 0.05 * 0.4 * weight * destination_range
    elif weight <= 40:
        express_charge = 0.1 * 0.05 * weight * destination_range
    elif weight <= 90:
        express_charge = 0.15 * 0.02 * weight * destination_range
    elif weight <= 150:
        express_charge = 0.2 * 0.01 * weight * destination_range

    total += express_charge

print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {total:.2f} lv.")

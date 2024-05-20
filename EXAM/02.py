LOVE_MESSAGE_PRICE = 0.6
WAX_ROSE_PRICE = 7.2
KEYHOLDER_PRICE = 3.6
CARICATURE_PRICE = 18.2
LUCKY_SURPRISE_PRICE = 22

party_price = float(input())

love_message_count = int(input())
wax_roses_count = int(input())
keyholder_count = int(input())
caricatures_count = int(input())
lucky_surprise_count = int(input())

all_total = love_message_count + wax_roses_count + \
    keyholder_count + caricatures_count + lucky_surprise_count

total_sales = love_message_count * LOVE_MESSAGE_PRICE + \
              wax_roses_count * WAX_ROSE_PRICE + \
              keyholder_count * KEYHOLDER_PRICE + \
              caricatures_count * CARICATURE_PRICE + \
              lucky_surprise_count * LUCKY_SURPRISE_PRICE


if all_total >= 25:
    total_sales *= 0.65

total_sales *= 0.90

if total_sales >= party_price:
    print(f"Yes! {total_sales - party_price:.2f} lv left.")
else:
    print(f"Not enough money! {party_price - total_sales:.2f} lv needed.")

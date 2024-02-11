# lost_fights = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armour_price = float(input())
# repair_expenses = 0
# shield_repair_counter = 0
#
# for current_lost_fight in range(1, lost_fights + 1):
#     if current_lost_fight % 2 == 0:
#         repair_expenses += helmet_price
#     if current_lost_fight % 3 == 0:
#         repair_expenses += sword_price
#     if current_lost_fight % 2 == 0 and current_lost_fight % 3 == 0:
#         repair_expenses += shield_price
#         shield_repair_counter += 1
#         if shield_repair_counter % 2 == 0:
#             repair_expenses += armour_price
#
# print(f'Gladiator expenses: {repair_expenses:.2f} aureus')


# ===================== different solution ====================
# =============================================================

lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())

total_helmet_broken = lost_fights // 2
total_sword_broken = lost_fights // 3
total_shield_broken = lost_fights // (2 * 3)
total_armour_broken = total_shield_broken // 2

expenses = total_helmet_broken * helmet_price + total_sword_broken * sword_price\
    + total_shield_broken * shield_price + total_armour_broken * armour_price

print(f'Gladiator expenses: {expenses:.2f} aureus')
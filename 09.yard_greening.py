COST_SQUAR_METER=7.61
FIRM_DISCOUNT = 0.18

square_meters_to_be_landscaped = float(input())

cost_landscaping_entire_yard = square_meters_to_be_landscaped*COST_SQUAR_METER
discount = FIRM_DISCOUNT*cost_landscaping_entire_yard
final_price = cost_landscaping_entire_yard-discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")

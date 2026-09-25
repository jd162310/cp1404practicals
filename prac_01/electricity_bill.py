  # get price per kWh in cents
  # get daily kWh use
  # number of days in the billing period
print("Electricity bill calculator")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff = int(input("which tariff? 11 or 31: "))
valid_tariff = 0
while valid_tariff == 0:
    if tariff == 11:
        valid_tariff = 1
    elif tariff == 31:
        valid_tariff = 1
    else:
        tariff = int(input("invalid tariff, enter 11 or 31: "))
if tariff == 11:
    per_kwh_in_cents = TARIFF_11
else:
    per_kwh_in_cents = TARIFF_31
daily_kwh_use = float(input("what is your daily kWh use: "))
days_in_bill_period = float(input("what is your billing period: "))
total_kwh_cost = (per_kwh_in_cents * daily_kwh_use) * days_in_bill_period
print(f"Total electricity cost: ${total_kwh_cost:.2f}")
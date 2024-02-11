b_shares = 2000
b_shares_price = 40.0
tax_broker_b = 3

s_shares = 2000
s_shares_price = 42.75
tax_broker_s = 3

profit = ((s_shares * s_shares_price) - (s_shares / 100 * 3) -
          (b_shares * 40.0) + (b_shares / 100 * 3))

print(f"При приобретении акций потрачено включая комиссию брокеру 3%\n\t{(b_shares * 40.0) + (b_shares / 100 * 3)}$")
print(f"При продаже акций спустя 2 недели с учетом вычита комисси брокеру"
      f"выручено\n\t{(s_shares * s_shares_price) - (s_shares / 100 * 3)}$")
print(f"Выручка после сделки составила:\n\t{profit}$")

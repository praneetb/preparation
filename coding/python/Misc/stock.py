#
# stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
#
# get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)
#

def get_max_profit(st_price):
  profit = 0
  idx = -1
  least = st_price[0]
  while 1:
    idx += 1
    try:
      p1 = st_price[idx]
      p2 = st_price[idx+1]
      if p2 < least:
        least = p2
        continue
      new_profit = p2-least
      if profit < new_profit:
        profit = new_profit
    except:
      return profit
  
  return 0

def main():
  #stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
  stock_prices_yesterday = [10, 7, 5, 4, 3, 2]
  max = get_max_profit(stock_prices_yesterday)
  print "Max Profit : %d" %max

if __name__ == '__main__':
  main()

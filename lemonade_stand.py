import random
import lemonade
day_count = 1
money = 100.00
while day_count <= 7:
    weather = ""
    rand_w = random.randint(1,4)
    if rand_w == 1:
        weather = "hot"
    elif rand_w == 2:
        weather = "sunny"
    elif rand_w == 3:
        weather = "overcast"
    elif rand_w == 4:
        weather = "cold"
    print("day" + str(day_count))
    print("the weather is: " + weather)
    print("you have $" + str(money) + " total")
    print()
    glasses = int(input("how many glasses of lemonade will you make? ($.50/glass) "))
    cost = float(input("how much will you charge per glass? (1$ - 5$) "))
    ads = int(input("how many ads will you place? (5/ad) "))
    glasses_cost = (.5 * glasses)
    ads_cost = (5 *ads)
    if money >= glasses_cost:
              money -= glasses_cost
              money -= glasses_cost
    else:
              glasses = int(money/.5)
              money -= (glasses * .5)
              print("You only had enough moeny for " + str(glasses) + " glasses")
    if money >= ads_cost:
              money -= ads_cost
    else:
              ads = int(money/5)
              money -= (ads *5)
              print("You only had enough for " + str(ads) + " ads")
    sold = lemonade.sell_lemonade(rand_w, glasses, cost, ads)
    profit = sold * cost
    money += profit
    print("You sold " + str(sold) + " glasses of lemonade today and made $" +str(profit))
    print()
    day_count += 1
print("It's been a week! You earned your time with $" + str(money))
print("That's a total profit of $" + str(money - 100.0))
    

team1= 120
team2 = 85
team3 = 150
team4 = 95
team5 = 110
total = team1 + team2 + team3 + team4 + team5
average = total/5
print("Total point : ", total, "pts")
print("Average per team : ", average, "pts")
stars_per_point = 2
earnings = total * stars_per_point
print("Total points : points ", earnings)
bags = total//25
leftover = total % 25
print("Full bags packed : ", leftover, "pts")
last_year = 500
print("Better than last year? :", total>last_year)
print("Same as last year? :", total==last_year)
print("At least as good? :", total>= last_year)
total+=30
print("After bonus crop :", total, "pts")
total -= 15
print("After seed reserve :", total, "pts")
bags = total//25
print("Final stars scored :", bags)
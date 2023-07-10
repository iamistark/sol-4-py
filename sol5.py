def arrange_coins(n):
    complete_rows = 0
    total_coins = 0
    row = 1

    while total_coins + row <= n:
        total_coins += row
        complete_rows += 1
        row += 1

    return complete_rows
#Driver code
n = 8
print(arrange_coins(n))

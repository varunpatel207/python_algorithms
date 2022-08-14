

def minimum_to_target(coin_list, target):
    coin_count = target
    if target in coin_list:
        return 1
    else:
        temp_coin_list = [coin for coin in coin_list if coin <= target]
        for i in temp_coin_list:
            temp_count = 1 + minimum_to_target(coin_list, target - i)
            if temp_count < coin_count:
                coin_count = temp_count
    return coin_count

print(minimum_to_target([1,10,25], 85))

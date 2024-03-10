


def parse_trade_message(trade_string: str, take_lowest: bool = True) -> dict:
    parts = trade_string.split()
    index = parts[0] + ' ' + parts[1][:5] + ' ' + parts[1][-2:]
    action = parts[2].upper()
    price_range = parts[-1].split('-')
    if take_lowest:
        price = int(price_range[0])
    else:
        price = int(price_range[1])
    return {'index': index, 'action': action, 'price': price}

def parse_new_trade_message(trade_string: str):
    trade_string_upper = trade_string.upper() # converted to upper case

    parts_list = trade_string_upper.split() # split the string into individual words

    if 'ABOVE' in parts_list:
        parts_list.remove('ABOVE') # remove the word 'ABOVE' from the list

    print('parts_list: ', parts_list)

    if 'BANK' in parts_list:
        index = parts_list[0] + ' ' + parts_list[1] + ' ' + parts_list[2][:5] + ' ' + parts_list[2][-2:]
        del parts_list[0:3]
    else:
        index = parts_list[0] + ' ' + parts_list[1][:5] + ' ' + parts_list[1][-2:]
        del parts_list[0:2]


    action = parts_list[0]

    lowest_price = int(parts_list[1].split('-')[0])
    highest_price = int(parts_list[1].split('-')[1])


    order_type = parts_list[2]

    order_type_amount = int(parts_list[3])

    lowest_target = int(parts_list[5])
    highest_target = int(parts_list[7])


    return {'index': index, 'action': action, 'lowest_price': lowest_price, 'highest_price': highest_price, 'order_type': order_type, 'order_type_amount': order_type_amount, 'lowest_target': lowest_target, 'highest_target': highest_target}


# if __name__ == "__main__":
#     trade_string = """Nifty 22400CE

#     BUY ABOVE 100-115

#     SI 80 Target 135 Target 155"""

#     tradee_string = """Bank nifty 47900ce buy 400-460

#     SL 360

#     TARGET 510 TARGET 580"""

#     ans = parse_new_trade_message(trade_string)
#     print(ans)


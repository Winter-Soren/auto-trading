


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


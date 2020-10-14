import faster_than_requests as r

# Currency enum
curAbbrev = {
    'USD': 1,
    'GBP': 2,
    'EUR': 3,
    'CHF': 4,
    'RUB': 5,
    'PLN': 6,
    'BRL': 7,
    'JPY': 8,
    'NOK': 9,
    'IDR': 10,
    'MYR': 11,
    'PHP': 12,
    'SGD': 13,
    'THB': 14,
    'VND': 15,
    'KRW': 16,
    'TRY': 17,
    'HRN': 18,
    'MXN': 19,
    'CAD': 20,
    'AUD': 21,
    'NZD': 22,
    'CNY': 23,
    'INR': 24,
    'CLP': 25,
    'PEN': 26,
    'COP': 27,
    'ZAR': 28,
    'HKD': 29,
    'TWD': 30,
    'SAR': 31,
    'AED': 32,
    'ARS': 34,
    'NIS': 35,
    'KZT': 37,
    'KWD': 38,
    'QAR': 39,
    'CRC': 40,
    'UYU': 41
}


def get_item(appid, name, currency='USD'):
    r"""
    Gets item listings from the `Steam Marketplace`.

    @appid ID of game item belongs to.

    @name: Name of item to lookup.

    @currency: Abbreviation of currency to return listing prices in.
    Accepted currencies:`USD,GBP,EUR,CHF,RUB,KRW,CAD`

    Defaults to `USD`.
    Please lookup the proper abbreviation for your currency of choice.

    Returns a json object
    Example:
    ```
    {
        "success": true,
        "lowest_price": "0,92€",
        "volume": "15",
        "median_price": "$34"
    }
    ```
    """
    url = f'http://steamcommunity.com//market/priceoverview/?appid={appid}&currency=curAbbrev[currency]&market_hash_name='
    geturl = url + r.urlencode(name)
    try:
        return r.get2json(geturl)
    except Exception as e:
        print(e)


def get_multiple(items, appid, currency='USD'):
    """Fetch multiple items using get_item()."""
    return {item: get_item(appid, item, currency) for item in items}


def get_multiple_tf2(items, currency='USD'):
    """Fetch multiple tf2 items using get_item()."""
    return {item: get_tf2_item(item, currency) for item in items}


def get_multiple_csgo(items, currency='USD'):
    """Fetch multiple csgo items using get_item()."""
    return {item: get_csgo_item(item, currency) for item in items}


def get_multiple_cards(items, currency='USD'):
    """Fetch multiple csgo items using get_item()."""
    return {item: get_steam_cards(item, currency) for item in items}


def get_multiple_pubg(items, currency='USD'):
    """Fetch multiple csgo items using get_item()."""
    return {item: get_pubg_item(item, currency) for item in items}


def get_steam_cards(item, currency='USD'):
    """Fetches an item from Steam Items. (Defaults the `appid` to 753)"""
    return get_item('753', item, currency)


def get_tf2_item(item, currency='USD'):
    """Fetches an item from TF2. (Defaults the `appid` to 440)"""
    return get_item('440', item, currency)


def get_csgo_item(item, currency='USD'):
    """Fetches an item from CSGO. (Defaults the `appid` to 730)"""
    return get_item('730', item, currency)


def get_pubg_item(item, currency='USD'):
    """Fetches an item from PUBG. (Defaults the `appid` to 578080)"""
    return get_item('578080', item, currency)


def get_dota2_item(item, currency='USD'):
    """Fetches an item from Dota 2. (Defaults the `appid` to 570)"""
    return get_item('570', item, currency)


def get_rust_item(item, currency='USD'):
    """Fetches an item from Rust. (Defaults the `appid` to 252490)"""
    return get_item('252490', item, currency)

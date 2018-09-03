slow = {}
slow["sniadanie"] = "szynka"
slow["obiad"] = "kurczak"
slow["kolacja"] = "burgery"


def in_slow(wanted_food) :
    """taka funkcja ktora narazie nie dziala"""
    try :
        a = slow.keys()
        for i in range(len(slow)) :
            if slow[a[i]] == wanted_food :
                key = a[i]
    except KeyError :
        key = 0
    return key

print in_slow("szynka")

def do_plus(a,b):
    if (type(a) == type(1) or type(a) == type("")) and (type(b) == type(1) or type(b) == type("")):
        return a+b
    else :
        raise TypeError, "zly typ danych elo"

print do_plus(5,8)
print do_plus([],8)

class Fridge:
    items = {}
    def __is_in_a_fridge(self, food):
        if type(food) == type(''):
            try:
                count = self.items[food]
            except KeyError:
                count = 0
            return count
        else :
            raise TypeError, "zly typ danych elo"

    def __all_ingredients(self, recipes):
        lack = {}
        nf = {}
        for i in recipes :
            in_fridge = self.__is_in_a_fridge(i)
            if in_fridge >= recipes[i]:
                print "jest %s" % i
                nf[i] = in_fridge - recipes[i]
            else :
                lack[i] = recipes[i] - in_fridge
        if bool(lack):
            print "nie masz %s" % lack
        else :
            print "masz wszystkie skladniki"
            return nf
    def cook(self, recipes) :
        nf = self.__all_ingredients(recipes)
        if bool(nf):
            self.items = nf
            print "gotowanie zakonczone, twoja lodowka: %s" % self.items
        else:
            print "gotwanie niemozliwe usupelnij skladniki"
f = Fridge()
f.items = {'maslo':1, 'chleb':20, 'ser':6, 'szynka':5}
sand = {'maslo':2, 'chleb':1, 'ser':1, 'szynka':1}



f.cook(sand)

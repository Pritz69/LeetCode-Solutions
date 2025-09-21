from sortedcontainers import SortedList

class MovieRentingSystem:
    def __init__(self, n, entries):
        self.shops = defaultdict(SortedList)   #movie -> (price, shop)
        self.shop_movie = {}    #(shop, movie) -> price
        self.rented = SortedList()  # (price, shop, movie)
        for s, m, p in entries:
            self.shops[m].add((p, s))
            self.shop_movie[s, m] = p

    def search(self, movie):
        return [y for _,y in self.shops[movie][:5]]
        
    def rent(self, shop, movie):
        price = self.shop_movie[shop, movie]
        self.shops[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop, movie):
        price = self.shop_movie[shop, movie]
        self.shops[movie].add((price, shop))
        self.rented.remove((price, shop, movie))
        
    def report(self):
        return [[y,z] for _,y,z in self.rented[:5]]
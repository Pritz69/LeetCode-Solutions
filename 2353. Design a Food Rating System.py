from sortedcontainers import SortedSet
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cf=defaultdict(SortedSet)
        self.c={}
        self.r={}
        for i in range(len(foods)) :
            self.cf[cuisines[i]].add((-ratings[i],foods[i]))
            self.c[foods[i]]=cuisines[i]
            self.r[foods[i]]=ratings[i]
    def changeRating(self, food: str, newRating: int) -> None:
        cuis=self.c[food]
        rate=self.r[food]
        self.cf[cuis].remove((-rate,food))
        self.cf[cuis].add((-newRating,food))
        self.r[food]=newRating

    def highestRated(self, cuisine: str) -> str:
        return self.cf[cuisine][0][1]

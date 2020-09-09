class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> \
    list[int]:
        restaurants = filter(lambda restaurant: restaurant[4] <= maxDistance, restaurants)
        if veganFriendly:
            restaurants = filter(lambda restaurant: veganFriendly == restaurant[2], restaurants)
        restaurants = list(filter(lambda restaurant: restaurant[3] <= maxPrice, restaurants))
        restaurants = sorted(restaurants, key=lambda x: (x[1], x[0]), reverse=True)
        return [restaurant[0] for restaurant in restaurants]

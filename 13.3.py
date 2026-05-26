class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 0.0

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}\n")

    def update_rating(self, new_rating):
        self.rating = new_rating

my_restaurant = Restaurant("Central Park", "Итальянская")

my_restaurant.describe_restaurant()

my_restaurant.update_rating(8.3)

print("После обновления рейтинга:")
my_restaurant.describe_restaurant()
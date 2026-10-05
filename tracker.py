from models import Meal, User
def remaining_calories(goal: int, consumed: int) -> int:
    return goal - consumed
class DietTracker:
    def __init__(self, user: User):
        self.user = user
        self.meals: list[Meal] = []
    def add_meal(self, meal: Meal) -> None:
        self.meals.append(meal)
    def total_consumed(self) -> int:
        return sum(meal.total_calories() for meal in self.meals)
    def remaining_calories(self) -> int:
        return remaining_calories(self.user.daily_calorie_target, self.total_consumed())
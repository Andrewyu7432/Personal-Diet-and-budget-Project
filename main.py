from models import Food, Meal, User
from tracker import DietTracker


def build_sample_tracker() -> DietTracker:
    user = User(
        name="Andre",
        age=25,
        weight_kg=75.0,
        height_cm=178.0,
        goal="maintain",
        daily_calorie_target=2200,
    )

    breakfast = Meal("Breakfast", [Food("Eggs", 210), Food("Toast", 180)])
    lunch = Meal("Lunch", [Food("Chicken", 330), Food("Rice", 260), Food("Vegetables", 90)])

    tracker = DietTracker(user)
    tracker.add_meal(breakfast)
    tracker.add_meal(lunch)
    return tracker


def print_daily_summary(tracker: DietTracker) -> None:
    print(f"User: {tracker.user.name}")
    print(f"Goal: {tracker.user.goal}")
    print(f"Target calories: {tracker.user.daily_calorie_target}")
    print(f"Consumed calories: {tracker.total_consumed()}")
    print(f"Remaining calories: {tracker.remaining_calories()}")


if __name__ == "__main__":
    print_daily_summary(build_sample_tracker())

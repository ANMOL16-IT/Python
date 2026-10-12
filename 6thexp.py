from functools import wraps
def track_activity(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"\nStarting activity: {func.__name__.title()}")
        result = func(*args,**kwargs)
        print(f"Activity completed:{func.__name__.title()}")
        return result
    return wrapper
def create_activity_tracker():
    total_calories = 0
    def add_activity(calories):
      nonlocal total_calories
      total_calories += calories
      print(f"Calories burned: {calories}")
      print(f"Total Calories: {total_calories}")
    return add_activity
calorie_tracker = create_activity_tracker()
@track_activity
def walking(steps, calories):
    print(f"Steps: {steps}")
    calorie_tracker(calories)
@track_activity
def running(distance, calories):
    print(f"Distance: {distance} km")
    calorie_tracker(calories)
@track_activity
def cycling(distance, calories):
    print(f"Distance: {distance} km")
    calorie_tracker(calories)
walking(5000, 200)
running(3, 250)
cycling(5, 150)
def calculate_bmi(weight_kg, height_cm):
    try:
        if weight_kg <= 0 or height_cm <= 0:
            raise ValueError("Weight and height must be positive numbers.")
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        return round(bmi, 2)
    except TypeError:
        raise ValueError("Weight and height must be numbers.")


def workout_recommendation(bmi):
    if bmi < 18.5:
        return (
            "You are underweight. Aim for 30-45 minutes of moderate exercise daily and a high-calorie diet. "
            "Home workouts are sufficient to build muscle mass."
        )
    elif 18.5 <= bmi < 24.9:
        return (
            "You have a normal weight. Aim for 45-60 minutes of moderate to intense exercise daily. "
            "You can work out at home or in a gym, depending on your preference."
        )
    elif 25 <= bmi < 29.9:
        return (
            "You are overweight. Aim for 60-75 minutes of intense exercise daily and a balanced diet. "
            "Gym workouts are recommended for better equipment access."
        )
    else:
        return (
            "You are obese. Aim for 60-90 minutes of intense exercise daily and a low-calorie diet. "
            "Gym workouts with professional supervision are advised for effective results."
        )


def main():
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in cm: "))
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is {bmi}.")
        print(workout_recommendation(bmi))
    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()

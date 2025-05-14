import pytest
from workout_time_planner import calculate_bmi, workout_recommendation

def test_calculate_bmi():
    # Test normal BMI calculation
    assert calculate_bmi(70, 175) == 22.86
    assert calculate_bmi(50, 160) == 19.53
    # Test edge cases
    with pytest.raises(ValueError, match="Weight and height must be positive numbers."):
        calculate_bmi(-70, 175)
    with pytest.raises(ValueError, match="Weight and height must be numbers."):
        calculate_bmi("seventy", 175)
    with pytest.raises(ValueError, match="Weight and height must be positive numbers."):
        calculate_bmi(70, -175)


def test_workout_recommendation():
    # Test various BMI ranges
    assert workout_recommendation(17) == "You are underweight. Aim for 30-45 minutes of moderate exercise daily and a high-calorie diet."
    assert workout_recommendation(22) == "You have a normal weight. Aim for 45-60 minutes of moderate to intense exercise daily."
    assert workout_recommendation(27) == "You are overweight. Aim for 60-75 minutes of intense exercise daily and a balanced diet."
    assert workout_recommendation(32) == "You are obese. Aim for 60-90 minutes of intense exercise daily and a low-calorie diet."

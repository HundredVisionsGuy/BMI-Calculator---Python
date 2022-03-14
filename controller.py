def calculate_bmi(weight, height):
    """ returns weight / height ^ 2 x 703 """
    weight = float(weight)
    height = float(height)
    return round((weight / height ** 2 * 703), 1)

def get_height(feet, inches):
    """ returns height in total inches """
    if feet:
        feet = float(feet)
    else:
        return 0.0
    if inches:
        inches = float(inches)
    else:
        inches = 0.0
    return feet * 12 + inches

def get_results(pounds, feet, inches):
    """ returns the BMI results as a string """
    height = get_height(feet, inches)
    if height and pounds:
        bmi = calculate_bmi(pounds, height)
        results = "You have a BMI of {}".format(bmi) 
    else:
        results = "You are missing information. Please enter the values."
    return results

def validate_input(pounds_str, feet_str, inches_str):
    """ returns string on the validation status """
    # Check for values within reasonable ranges:
    # can we convert our strings to floats?
    results = ""
    try:
        pounds = float(pounds_str)
        feet = float(feet_str)
        # inches could be blank
        if inches_str:
            inches = float(inches_str)
        else:
            inches = 0.0
    except ValueError as er:
        results += "Cannot convert one or more inputs to float.\n"

    # feet should be positive numbers between 1 and 9
    if feet < 1 or feet > 9:
        results += "Feet must be a number between 1 and 9.\n"
    if pounds < 50 or pounds > 250:
        results += "Pounds must be a number between 50 and 250."
    if results:
        return results
    else:
        return "Valid"


if __name__ == '__main__':
    # Test our modules locally
    bmi = calculate_bmi("37.25", "41.5")
    print(bmi)
    height = get_height(5, 0)
    print(calculate_bmi("100", height))
    height = get_height(6, 4)
    print(calculate_bmi(100, height))
    
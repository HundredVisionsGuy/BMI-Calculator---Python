def calculate_bmi(weight, height):
    """ returns weight / height ^ 2 x 703 """
    weight = float(weight)
    height = float(height)
    return round((weight / height ** 2 * 703), 1)

def get_height(feet, inches):
    """ returns height in total inches """
    feet = float(feet)
    inches = float(inches)
    return feet * 12 + inches

def get_results(pounds, feet, inches):
    """ returns the BMI results as a string """
    height = get_height(feet, inches)
    bmi = calculate_bmi(pounds, height)
    results = "You have a BMI of {}".format(bmi) 
    return results

def validate_input(pounds_str, feet_str, inches_str):
    pass

if __name__ == '__main__':
    # Test our modules locally
    bmi = calculate_bmi("37.25", "41.5")
    print(bmi)
    height = get_height(5, 0)
    print(calculate_bmi("100", height))
    height = get_height(6, 4)
    print(calculate_bmi(100, height))
    
def calculate_optimal_weight(height_ft):
    """
    Calculate optimal weight using a standard healthy BMI value (e.g., 22).
    """
    height_cm = height_ft * 30.48
    height_m = height_cm / 100
    optimal_weight = 22 * (height_m ** 2)
    return round(optimal_weight, 1)


def extract_nutrition(recipe_text):
    # Dummy extractor using keywords
    nutrition = {}
    for line in recipe_text.splitlines():
        if 'calorie' in line.lower():
            nutrition['Calories'] = line.strip()
        elif 'protein' in line.lower():
            nutrition['Protein'] = line.strip()
        elif 'fat' in line.lower():
            nutrition['Fat'] = line.strip()
    return nutrition

def format_recipes(ai_response):
    # Splits AI response into 2 recipe sections
    parts = ai_response.split("2.")
    recipes = {
        "Healthy": parts[0].replace("1.", "").strip() if len(parts) > 0 else "",
        "Indulgent": parts[1].strip() if len(parts) > 1 else ""
    }
    return recipes

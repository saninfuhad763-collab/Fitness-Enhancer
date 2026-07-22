from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import UserProfile
from django.http import HttpResponseForbidden
from users.utils import is_premium

@login_required
def calorie_calculator(request):

    if not is_premium(request.user):
        return HttpResponseForbidden(
            "Upgrade to Premium to use the calorie calculator"
        )

    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'age': 30,
            'height': 170.0,
            'weight': 70.0,
            'goal': 'fitness',
            'experience': 'beginner'
        }
    )

    # BMI calculation
    height_m = profile.height / 100
    bmi = round(profile.weight / (height_m ** 2), 1)

    # BMR calculation (Mifflin-St Jeor)
    bmr = (10 * profile.weight) + (6.25 * profile.height) - (5 * profile.age) + 5

    # Activity factor
    activity_factor = 1.4 if profile.experience == 'beginner' else 1.6
    tdee = bmr * activity_factor

    # Goal-based calorie & macro adjustment
    if profile.goal == 'fat_loss':
        calories = tdee - 500
        protein = profile.weight * 1.6
        meals = [
            {'name': 'Breakfast', 'icon': 'sunrise', 'title': 'Oatmeal & Whey Protein', 'desc': 'Oatmeal with berries, chia seeds, and 1 scoop whey protein', 'calories': 350, 'protein': 30},
            {'name': 'Lunch', 'icon': 'sun', 'title': 'Grilled Chicken Salad', 'desc': 'Chicken breast with mixed greens, quinoa, and olive oil dressing', 'calories': 450, 'protein': 40},
            {'name': 'Dinner', 'icon': 'moon', 'title': 'Baked Salmon & Greens', 'desc': 'Wild salmon fillet with asparagus and roasted sweet potato', 'calories': 500, 'protein': 35},
            {'name': 'Snack', 'icon': 'coffee', 'title': 'Greek Yogurt & Almonds', 'desc': 'Low-fat Greek yogurt topped with raw almonds and honey', 'calories': 200, 'protein': 18},
        ]
        tips = [
            "Maintain a 500 kcal deficit consistently for steady 0.5kg/week weight loss.",
            "Consume 25-30g of fiber daily to enhance satiety and digestive health.",
            "Drink 500ml of water before major meals to assist appetite control."
        ]
    elif profile.goal == 'lean_muscle':
        calories = tdee + 300
        protein = profile.weight * 2.0
        meals = [
            {'name': 'Breakfast', 'icon': 'sunrise', 'title': 'Eggs & Avocado Toast', 'desc': '4 eggs (3 whole, 1 egg white), 2 slices whole grain toast & avocado', 'calories': 550, 'protein': 35},
            {'name': 'Lunch', 'icon': 'sun', 'title': 'Beef & Rice Bowl', 'desc': 'Lean ground beef, jasmine rice, steamed broccoli & teriyaki sauce', 'calories': 650, 'protein': 45},
            {'name': 'Dinner', 'icon': 'moon', 'title': 'Grilled Chicken & Pasta', 'desc': 'Chicken breast, whole wheat pasta with marinara & roasted veggies', 'calories': 700, 'protein': 50},
            {'name': 'Snack', 'icon': 'coffee', 'title': 'Protein Shake & Banana', 'desc': 'Whey protein, almond milk, 1 banana & peanut butter', 'calories': 350, 'protein': 30},
        ]
        tips = [
            "Prioritize post-workout nutrition with 30-40g fast-digesting protein.",
            "Maintain a slight 300 kcal surplus to support muscle hypertrophy without fat gain.",
            "Aim for 7-9 hours of quality sleep for peak growth hormone release."
        ]
    else:
        calories = tdee
        protein = profile.weight * 1.4
        meals = [
            {'name': 'Breakfast', 'icon': 'sunrise', 'title': 'Spinach & Egg Omelet', 'desc': 'Whole eggs with spinach, tomatoes, and whole grain toast', 'calories': 400, 'protein': 25},
            {'name': 'Lunch', 'icon': 'sun', 'title': 'Turkey & Veggie Wrap', 'desc': 'Sliced turkey breast, spinach, hummus in a whole wheat tortilla', 'calories': 500, 'protein': 35},
            {'name': 'Dinner', 'icon': 'moon', 'title': 'Sirloin Steak & Potatoes', 'desc': 'Lean sirloin steak with roasted potatoes and green beans', 'calories': 550, 'protein': 40},
            {'name': 'Snack', 'icon': 'coffee', 'title': 'Cottage Cheese & Fruit', 'desc': 'Low-fat cottage cheese with pineapple or fresh berries', 'calories': 250, 'protein': 20},
        ]
        tips = [
            "Focus on whole, minimally processed foods to maintain stable energy levels.",
            "Equally balance macros (protein, complex carbs, and healthy fats) across meals.",
            "Stay hydrated throughout the day to support recovery and digestion."
        ]

    # Water intake recommendation (35ml per kg bodyweight)
    water_intake = round(profile.weight * 0.035, 1)

    context = {
        'profile': profile,
        'bmi': bmi,
        'bmr': round(bmr),
        'tdee': round(tdee),
        'calories': round(calories),
        'protein': round(protein, 1),
        'water_intake': water_intake,
        'meals': meals,
        'tips': tips,
    }

    return render(request, 'tools/calorie.html', context)
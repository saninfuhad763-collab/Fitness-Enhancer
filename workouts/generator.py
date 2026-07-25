"""
Deterministic Rule-Based Workout Generator for Fitness Enhancer.
Generates personalized workout routines dynamically based on user profile metrics and current day of the week.
No AI, no ML, no database mutations, no randomness.
"""

from datetime import datetime

# Exercise Database categorized by split focus
EXERCISE_DATABASE = {
    'Upper Body': [
        {'name': 'Barbell Bench Press', 'muscle_group': 'Chest', 'desc': 'Primary compound movement for chest, front delts, and triceps.'},
        {'name': 'Bent-Over Barbell Row', 'muscle_group': 'Back', 'desc': 'Builds upper back thickness and lats strength.'},
        {'name': 'Overhead Dumbbell Press', 'muscle_group': 'Shoulders', 'desc': 'Targets anterior and lateral deltoids.'},
        {'name': 'Lat Pulldown', 'muscle_group': 'Lats', 'desc': 'Develops upper back width and upper body posture.'},
        {'name': 'Incline Dumbbell Press', 'muscle_group': 'Upper Chest', 'desc': 'Emphasizes clavicular chest head.'},
        {'name': 'Tricep Rope Pushdown', 'muscle_group': 'Triceps', 'desc': 'Isolated triceps lateral and medial head exercise.'},
        {'name': 'Dumbbell Bicep Curl', 'muscle_group': 'Biceps', 'desc': 'Classic bicep hypertrophy movement.'},
        {'name': 'Lateral Dumbbell Raise', 'muscle_group': 'Shoulders', 'desc': 'Isolates lateral deltoids for shoulder width.'},
    ],
    'Lower Body': [
        {'name': 'Barbell Back Squat', 'muscle_group': 'Quads & Glutes', 'desc': 'King of lower body compound movements.'},
        {'name': 'Romanian Deadlift', 'muscle_group': 'Hamstrings & Glutes', 'desc': 'Hinge movement targeting posterior chain.'},
        {'name': 'Leg Press', 'muscle_group': 'Quads', 'desc': 'Machine quad builder with lower back support.'},
        {'name': 'Walking Dumbbell Lunges', 'muscle_group': 'Quads & Glutes', 'desc': 'Unilateral leg strength and stability.'},
        {'name': 'Hamstring Leg Curl', 'muscle_group': 'Hamstrings', 'desc': 'Isolated hamstring knee flexion exercise.'},
        {'name': 'Standing Calf Raise', 'muscle_group': 'Calves', 'desc': 'Gastrocnemius calf development.'},
    ],
    'Push': [
        {'name': 'Barbell Bench Press', 'muscle_group': 'Chest', 'desc': 'Flat press for overall chest strength.'},
        {'name': 'Overhead Press (OHP)', 'muscle_group': 'Shoulders', 'desc': 'Strict vertical pressing power.'},
        {'name': 'Incline Dumbbell Flyes', 'muscle_group': 'Upper Chest', 'desc': 'Chest isolation stretch.'},
        {'name': 'Dips (Weighted/Bodyweight)', 'muscle_group': 'Chest & Triceps', 'desc': 'Bodyweight pressing compound.'},
        {'name': 'Lateral Dumbbell Raise', 'muscle_group': 'Shoulders', 'desc': 'Side delt isolation.'},
        {'name': 'Skullcrushers', 'muscle_group': 'Triceps', 'desc': 'Overhead triceps extension.'},
    ],
    'Pull': [
        {'name': 'Barbell Conventional Deadlift', 'muscle_group': 'Back & Posterior', 'desc': 'Total posterior chain power.'},
        {'name': 'Pull-Ups / Chins', 'muscle_group': 'Lats & Back', 'desc': 'Vertical pull for lat width.'},
        {'name': 'Seated Cable Row', 'muscle_group': 'Mid Back', 'desc': 'Horizontal rowing for mid-traps and rhomboids.'},
        {'name': 'Face Pulls', 'muscle_group': 'Rear Delts', 'desc': 'Rear delt and rotator cuff health.'},
        {'name': 'Hammer Curls', 'muscle_group': 'Biceps & Forearms', 'desc': 'Brachialis and forearm thickness.'},
        {'name': 'Incline Dumbbell Bicep Curl', 'muscle_group': 'Biceps', 'desc': 'Long head bicep isolation.'},
    ],
    'Legs': [
        {'name': 'Barbell Back Squat', 'muscle_group': 'Quads', 'desc': 'Heavy quad-focused compound lift.'},
        {'name': 'Romanian Deadlift', 'muscle_group': 'Hamstrings', 'desc': 'Posterior chain eccentric hinge.'},
        {'name': 'Bulgarian Split Squat', 'muscle_group': 'Quads & Glutes', 'desc': 'Unilateral quad & glute builder.'},
        {'name': 'Leg Extensions', 'muscle_group': 'Quads', 'desc': 'Isolated quad extension.'},
        {'name': 'Seated Leg Curl', 'muscle_group': 'Hamstrings', 'desc': 'Hamstring isolation.'},
        {'name': 'Standing Calf Raise', 'muscle_group': 'Calves', 'desc': 'Calf hypertrophy.'},
    ],
    'Full Body': [
        {'name': 'Goblet Squat', 'muscle_group': 'Quads', 'desc': 'Fundamental quad and core movement.'},
        {'name': 'Dumbbell Bench Press', 'muscle_group': 'Chest', 'desc': 'Balanced pressing exercise.'},
        {'name': 'One-Arm Dumbbell Row', 'muscle_group': 'Back', 'desc': 'Unilateral rowing for lats.'},
        {'name': 'Dumbbell Shoulder Press', 'muscle_group': 'Shoulders', 'desc': 'Vertical pressing.'},
        {'name': 'Kettlebell Swings', 'muscle_group': 'Posterior Chain', 'desc': 'Explosive hip hinge.'},
        {'name': 'Plank', 'muscle_group': 'Core', 'desc': 'Isometric core stability.'},
    ],
}

# Weekly Split Configurations based on frequency
SPLIT_CONFIGURATIONS = {
    3: {
        'Monday': {'type': 'Upper Body', 'title': 'Upper Body Power'},
        'Tuesday': None,
        'Wednesday': {'type': 'Lower Body', 'title': 'Lower Body Strength'},
        'Thursday': None,
        'Friday': {'type': 'Full Body', 'title': 'Full Body Conditioning'},
        'Saturday': None,
        'Sunday': None,
    },
    4: {
        'Monday': {'type': 'Upper Body', 'title': 'Upper Body Focus'},
        'Tuesday': {'type': 'Lower Body', 'title': 'Lower Body Focus'},
        'Wednesday': None,
        'Thursday': {'type': 'Push', 'title': 'Push Hypertrophy'},
        'Friday': {'type': 'Pull', 'title': 'Pull Hypertrophy'},
        'Saturday': None,
        'Sunday': None,
    },
    5: {
        'Monday': {'type': 'Push', 'title': 'Push Power'},
        'Tuesday': {'type': 'Pull', 'title': 'Pull Power'},
        'Wednesday': {'type': 'Legs', 'title': 'Legs & Lower Body'},
        'Thursday': {'type': 'Upper Body', 'title': 'Upper Body Volume'},
        'Friday': {'type': 'Lower Body', 'title': 'Lower Body Volume'},
        'Saturday': None,
        'Sunday': None,
    },
    6: {
        'Monday': {'type': 'Push', 'title': 'Push Hypertrophy'},
        'Tuesday': {'type': 'Pull', 'title': 'Pull Hypertrophy'},
        'Wednesday': {'type': 'Legs', 'title': 'Legs Hypertrophy'},
        'Thursday': {'type': 'Push', 'title': 'Push Power'},
        'Friday': {'type': 'Pull', 'title': 'Pull Power'},
        'Saturday': {'type': 'Legs', 'title': 'Legs Power'},
        'Sunday': None,
    }
}


def get_profile_defaults(profile=None):
    """Returns profile fields with sensible defaults if missing or empty."""
    goal = getattr(profile, 'goal', 'fitness') or 'fitness'
    if goal not in ['fat_loss', 'lean_muscle', 'fitness']:
        goal = 'fitness'

    experience = getattr(profile, 'experience', 'beginner') or 'beginner'
    if experience not in ['beginner', 'intermediate', 'advanced']:
        experience = 'beginner'

    return {
        'goal': goal,
        'experience': experience,
    }


def determine_workout_frequency(experience):
    """Determines weekly workout frequency based on user experience level."""
    if experience == 'advanced':
        return 5
    elif experience == 'intermediate':
        return 4
    return 3  # Default for beginner / fallback


def adapt_goal_parameters(goal):
    """Adapts rep ranges, rest periods, and tempo based on fitness goal."""
    if goal == 'lean_muscle':
        return {
            'reps': '6 - 8 reps',
            'rest': '90 - 120 sec rest',
            'style': 'Hypertrophy & Heavy Loads',
        }
    elif goal == 'fat_loss':
        return {
            'reps': '12 - 15 reps',
            'rest': '30 - 45 sec rest',
            'style': 'Metabolic & High Intensity',
        }
    else:  # 'fitness'
        return {
            'reps': '8 - 12 reps',
            'rest': '60 - 90 sec rest',
            'style': 'Balanced Volume & Form',
        }


def adapt_experience_parameters(experience):
    """Adapts exercise count, set volume, and difficulty badge."""
    if experience == 'advanced':
        return {
            'exercise_count': 6,
            'sets': 4,
            'badge': 'Advanced',
            'badge_class': 'ds-badge-error',
            'est_duration': '60 - 75 min',
        }
    elif experience == 'intermediate':
        return {
            'exercise_count': 5,
            'sets': 4,
            'badge': 'Intermediate',
            'badge_class': 'ds-badge-warning',
            'est_duration': '45 - 60 min',
        }
    else:  # 'beginner'
        return {
            'exercise_count': 4,
            'sets': 3,
            'badge': 'Beginner',
            'badge_class': 'ds-badge-primary',
            'est_duration': '30 - 45 min',
        }


def generate_workout_for_day(profile=None, day_name=None):
    """
    Generates a deterministic workout dictionary for a given day of the week.
    If day_name is None, defaults to current day of the week (e.g. 'Monday').
    """
    if not day_name:
        day_name = datetime.now().strftime('%A')

    defaults = get_profile_defaults(profile)
    goal = defaults['goal']
    experience = defaults['experience']

    frequency = determine_workout_frequency(experience)
    weekly_split = SPLIT_CONFIGURATIONS.get(frequency, SPLIT_CONFIGURATIONS[3])
    day_workout_info = weekly_split.get(day_name)

    # Rest Day handling
    if not day_workout_info:
        return {
            'is_rest_day': True,
            'day_name': day_name,
            'title': 'Rest & Recovery',
            'recovery_tips': [
                {'icon': 'droplet', 'text': 'Hydrate well (aim for 2.5 - 3 Liters of water daily)'},
                {'icon': 'activity', 'text': 'Stretch or perform light mobility work for 10–15 minutes'},
                {'icon': 'footprints', 'text': 'Take a light 20–30 minute active walk'},
                {'icon': 'moon', 'text': 'Prioritize 7–9 hours of deep quality sleep'},
                {'icon': 'calendar-check', 'text': 'Prepare your gear and meals for tomorrow\'s workout'},
            ],
            'badge': 'Recovery',
            'goal_display': goal.replace('_', ' ').title(),
            'experience_display': experience.title(),
        }

    # Workout Day handling
    workout_type = day_workout_info['type']
    workout_title = day_workout_info['title']

    goal_params = adapt_goal_parameters(goal)
    exp_params = adapt_experience_parameters(experience)

    base_exercises = EXERCISE_DATABASE.get(workout_type, EXERCISE_DATABASE['Full Body'])
    selected_raw_exercises = base_exercises[:exp_params['exercise_count']]

    exercises = []
    target_muscles = set()

    for idx, raw in enumerate(selected_raw_exercises, 1):
        target_muscles.add(raw['muscle_group'])
        exercises.append({
            'index': idx,
            'name': raw['name'],
            'muscle_group': raw['muscle_group'],
            'description': raw['desc'],
            'sets': exp_params['sets'],
            'reps': goal_params['reps'],
            'rest': goal_params['rest'],
        })

    return {
        'is_rest_day': False,
        'day_name': day_name,
        'title': workout_title,
        'workout_type': workout_type,
        'estimated_duration': exp_params['est_duration'],
        'difficulty_badge': exp_params['badge'],
        'badge_class': exp_params['badge_class'],
        'target_muscles': ', '.join(sorted(target_muscles)),
        'exercises': exercises,
        'exercise_count': len(exercises),
        'goal_display': goal.replace('_', ' ').title(),
        'experience_display': experience.title(),
        'training_style': goal_params['style'],
    }


def generate_full_weekly_schedule(profile=None):
    """
    Generates a deterministic 7-day schedule list for the weekly schedule view.
    """
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    schedule = []
    for day in days:
        workout = generate_workout_for_day(profile, day_name=day)
        schedule.append({
            'day_name': day,
            'workout': workout,
        })
    return schedule

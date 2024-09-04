# backend/scheduler.py
def generate_schedule(family_members):
    workouts = ['Chest', 'Back', 'Legs', 'Arms', 'Shoulders', 'Cardio', 'Rest']
    schedule = {}
    for i, member in enumerate(family_members):
        schedule[member] = workouts[i % len(workouts)]
    return schedule

'''Employee performance assessment.'''

employees = [
    {"name": "Alice", "tasks_completed": 25, "quality": 0.9},
    {"name": "Bob", "tasks_completed": 30, "quality": 0.85},
    {"name": "Charlie", "tasks_completed": 20, "quality": 0.95}
]

def evaluate_performance(employees):
    quality = {}

    for item in employees:
        performance = item["tasks_completed"] * item["quality"]
        print(f"{item["name"]}: {performance}")
        quality[item["name"]] = performance

    best_employee = max(quality, key=quality.get)
    worst_employee = min(quality, key=quality.get)

    print(f"The best employee: {best_employee}")
    print(f"The worst employee: {worst_employee}")
    
evaluate_performance(employees)
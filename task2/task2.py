class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = []


def create_schedule(subjects, teachers):
    uncovered = set(subjects)
    available_teachers = teachers.copy()

    schedule = []

    while uncovered:
        best_teacher = None
        best_coverage = set()

        for teacher in available_teachers:
            coverage = teacher.can_teach_subjects.intersection(uncovered)

            if len(coverage) > len(best_coverage):
                best_teacher = teacher
                best_coverage = coverage
            elif len(coverage) == len(best_coverage) and coverage and best_teacher is not None:
                if teacher.age < best_teacher.age:
                    best_teacher = teacher
                    best_coverage = coverage

        if not best_teacher or not best_coverage:
            return None

        best_teacher.assigned_subjects = list(best_coverage)
        schedule.append(best_teacher)
        uncovered -= best_coverage
        available_teachers.remove(best_teacher)

    return schedule
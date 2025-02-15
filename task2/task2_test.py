import unittest

from task2 import Teacher, create_schedule


class TestSchedule(unittest.TestCase):
    def test_schedule_covers_all_subjects(self):
        subjects = {'Mathematics', 'Physics', 'Chemistry', 'Computer Science', 'Biology'}

        teachers = [Teacher("Oleksandr", "Ivanenko", 45, "o.ivanenko@example.com", {"Mathematics", "Physics"}),
                    Teacher("Maria", "Petrenko", 38, "m.petrenko@example.com", {"Chemistry"}),
                    Teacher("Serhiy", "Kovalenko", 50, "s.kovalenko@example.com", {"Computer Science", "Mathematics"}),
                    Teacher("Natalia", "Shevchenko", 29, "n.shevchenko@example.com", {"Biology", "Chemistry"}),
                    Teacher("Dmytro", "Bondarenko", 35, "d.bondarenko@example.com", {"Physics", "Computer Science"}),
                    Teacher("Olena", "Hrytsenko", 42, "o.grytsenko@example.com", {"Biology"})]

        schedule = create_schedule(subjects, teachers)

        self.assertIsNotNone(schedule)

        if schedule:
            print("Schedule:")

            for teacher in schedule:
                print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} years old, email: {teacher.email}")
                print(f"   Teaches subjects: {', '.join(teacher.assigned_subjects)}\n")

        assigned = set()

        for teacher in schedule:
            self.assertTrue(set(teacher.assigned_subjects).issubset(teacher.can_teach_subjects))
            assigned.update(teacher.assigned_subjects)

        self.assertEqual(assigned, subjects)

    def test_schedule_failure(self):
        subjects = {'Mathematics', 'Physics', 'Chemistry', 'Computer Science', 'Biology', 'History'}

        teachers = [Teacher("Oleksandr", "Ivanenko", 45, "o.ivanenko@example.com", {"Mathematics", "Physics"}),
                    Teacher("Maria", "Petrenko", 38, "m.petrenko@example.com", {"Chemistry"}),
                    Teacher("Serhiy", "Kovalenko", 50, "s.kovalenko@example.com", {"Computer Science", "Mathematics"}),
                    Teacher("Natalia", "Shevchenko", 29, "n.shevchenko@example.com", {"Biology", "Chemistry"}),
                    Teacher("Dmytro", "Bondarenko", 35, "d.bondarenko@example.com", {"Physics", "Computer Science"}),
                    Teacher("Olena", "Hrytsenko", 42, "o.grytsenko@example.com", {"Biology"})]

        schedule = create_schedule(subjects, teachers)

        if schedule is None:
            print("Unable to cover all subjects with available teachers in Failure test.")

        self.assertIsNone(schedule)

    def test_teacher_assignment_matches_capabilities(self):
        subjects = {'Mathematics', 'Physics', 'Chemistry', 'Computer Science', 'Biology'}

        teachers = [Teacher("Oleksandr", "Ivanenko", 45, "o.ivanenko@example.com", {"Mathematics", "Physics"}),
            Teacher("Maria", "Petrenko", 38, "m.petrenko@example.com", {"Chemistry"}),
            Teacher("Serhiy", "Kovalenko", 50, "s.kovalenko@example.com", {"Computer Science", "Mathematics"}),
            Teacher("Natalia", "Shevchenko", 29, "n.shevchenko@example.com", {"Biology", "Chemistry"}),
            Teacher("Dmytro", "Bondarenko", 35, "d.bondarenko@example.com", {"Physics", "Computer Science"}),
            Teacher("Olena", "Hrytsenko", 42, "o.grytsenko@example.com", {"Biology"})]

        schedule = create_schedule(subjects, teachers)

        self.assertIsNotNone(schedule)

        for teacher in schedule:
            self.assertTrue(teacher.assigned_subjects)
            self.assertTrue(set(teacher.assigned_subjects).issubset(teacher.can_teach_subjects))


if __name__ == '__main__':
    unittest.main()
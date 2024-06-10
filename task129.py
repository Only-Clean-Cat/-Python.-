import unittest

from main import Student

class StudentTest(unittest.TestCase):

    def test_walk(self):
        student = Student('идет')
        for student.walk in range(11):
            result = student.walk * 5
        self.assertEqual(result, 500, 'Дистанции не равны [дистанция человека(объекта)] != 500')

    def test_run(self):
        student = Student('бежит')
        for student.run in range(11):
            result1 = student.run * 10
        self.assertLess(1000, result1, 'Дистанции не равны [дистанция человека(объекта)] != 1000')

    def test_student(self):
        student = Student('сравнение')
        for student.walk in range(11):
            result = student.walk * 5
        for student.run in range(11):
            result1 = student.run * 10
        self.assertGreater(result1, result, '[бегущий человек] должен преодолеть дистанцию больше, чем [идущий человек]')

if __name__ == '__main__':
    unittest.main()









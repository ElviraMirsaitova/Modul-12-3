import rt_with_exceptions as rt
import runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walker = runner.Runner('Вася')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        run = runner.Runner('Петя')
        for i in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        walker2 = runner.Runner('Маша')
        run2 = runner.Runner('Саша')
        for i in range(10):
            walker2.walk()
            run2.run()
        self.assertNotEqual(run2.distance, walker2.distance)
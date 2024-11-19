import unittest
import runner_and_tournament as rt

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner1 = rt.Runner('Усэйн', speed=10)
        self.runner2 = rt.Runner('Андрей', speed=9)
        self.runner3 = rt.Runner('Ник', speed=3)


    def test_challenge(self):
        tour1 = rt.Tournament(90, self.runner1, self.runner3)
        TournamentTest.all_results[1] = tour1.start()
        self.assertTrue(TournamentTest.all_results[1][2], self.runner3)

    def test_challenge2(self):
        tour2 = rt.Tournament(90, self.runner2, self.runner3)
        TournamentTest.all_results[2] = tour2.start()
        self.assertTrue(TournamentTest.all_results[2][2], self.runner3)

    def test_challenge3(self):
        tour3 = rt.Tournament(90, self.runner1, self.runner2, self.runner3)
        TournamentTest.all_results[3] = tour3.start()
        self.assertTrue(TournamentTest.all_results[3][3], self.runner3)

    @classmethod
    def tearDownClass(cls):
        for i, j in cls.all_results.items():
            print({pos: runner.name for pos, runner in j.items()})

if __name__ == '__main__':
    unittest.main()
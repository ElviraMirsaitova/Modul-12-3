import unittest
import Modul_12_1
import Modul_12_2

#Часть 1. TestSuit.
M_test = unittest.TestSuite()
M_test.addTest(unittest.TestLoader().loadTestsFromTestCase(Modul_12_1.RunnerTest))
M_test.addTest(unittest.TestLoader().loadTestsFromTestCase(Modul_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(M_test)
#Часть 2. Пропуск тестов.

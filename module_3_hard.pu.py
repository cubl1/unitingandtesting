import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self, times):
        for i in range(times):
            self.distance += 10
        return self.distance

    def walk(self, times):
        for i in range(times):
            self.distance += 5
        return self.distance

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner("h")
        self.assertEqual(runner.walk(10), 50)

    def test_run(self):
        runner = Runner("i")
        self.assertEqual(runner.run(10), 100)

    def test_challenge(self):
        runner1 = Runner("j")
        runner2 = Runner("k")
        runner1.run(10)
        runner2.walk(10)
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == "__main__":
    unittest.main()
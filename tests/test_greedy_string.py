import unittest
from Model.GreedyString import GreedyStringMerger

class TestGreedyStringMerger(unittest.TestCase):
    def test_find_overlap(self):
        # Init GreedyStringMerger
        greedyMerge = GreedyStringMerger([])

        # overlap
        overlap, result = greedyMerge.find_overlap("all is well", "ell that ends")
        self.assertEqual(overlap, 3)  # expected result "ell" 
        self.assertEqual(result, "all is well that ends")

        # no overlap Note: string concat order is s2 + s1
        overlap, result = greedyMerge.find_overlap("breaking news", "Get the latest", True)
        self.assertEqual(overlap, 0)
        self.assertEqual(result, "Get the latest breaking news")

        # full overlap
        overlap, result = greedyMerge.find_overlap("substring", "string")
        self.assertEqual(overlap, 6)
        self.assertEqual(result, "substring")

    def test_merge_strings(self):
        # init GreedyStringMerger with string list
        string_list = ["happy new year", "ear and happy", "happy long weekend"]
        greedyMerge = GreedyStringMerger(string_list)

        # greedy_merge
        is_merged = greedyMerge.greedy_merge()
        self.assertTrue(is_merged)
        self.assertEqual(len(greedyMerge.string_list), 2)  # need left two string
        self.assertIn("happy long weekend", greedyMerge.string_list)

    def test_run(self):
        # init GreedyStringMerger with strings list
        string_list = [
            "all is well",
            "ell that en",
            "hat end",
            "t ends well"
        ]
        greedyMerge = GreedyStringMerger(string_list)

        # run full processing
        result = greedyMerge.run()
        self.assertEqual(result, "all is well that ends well")

    def test_none_overlap_handling(self):
        # test none overlap
        string_list = [
            "all is well",
            "unique string",
            "another one"
        ]
        greedyMerge = GreedyStringMerger(string_list)
        result = greedyMerge.run()

        # expected keep all string
        self.assertIn("all is well", result)
        self.assertIn("unique string", result)
        self.assertIn("another one", result)

if __name__ == "__main__":
    unittest.main()

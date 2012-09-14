#!/usr/bin/env python

import unittest
from tree_utils import Node, is_balanced


class Test_Node(unittest.TestCase):
    def test_single_node(self):
        nodeA = Node(43)
        self.assertTrue(is_balanced(nodeA))

    def test_single_child(self):
        nodeA = Node(43)
        nodeB = Node(57)
        nodeA.left = nodeB
        self.assertTrue(is_balanced(nodeA))

    def test_three_in_a_row(self):
        nodeA = Node(43)
        nodeB = Node(57)
        nodeC = Node(128)
        nodeA.left = nodeB
        nodeB.right = nodeC
        self.assertFalse(is_balanced(nodeA))

if __name__ == "__main__":
    unittest.main()


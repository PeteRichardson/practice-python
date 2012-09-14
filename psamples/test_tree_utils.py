#!/usr/bin/env python

import unittest
from tree_utils import Node, is_balanced


class Test_Node(unittest.TestCase):

    def test_single_node(self):
        nodeA = Node(43)
        self.assertTrue(is_balanced(nodeA))
        self.assertEqual(nodeA.d2(), 1)
        self.assertEqual(nodeA.d3(), 1)

    def test_single_child(self):
        nodeA = Node(43)
        nodeB = Node(57)
        nodeA.left = nodeB
        self.assertTrue(is_balanced(nodeA))
        self.assertEqual(nodeA.d2(), 2)
        self.assertEqual(nodeA.d3(), 2)

    def test_three_in_a_row(self):
        nodeA = Node(43)
        nodeB = Node(57)
        nodeC = Node(128)
        nodeA.left = nodeB
        nodeB.right = nodeC
        self.assertFalse(is_balanced(nodeA))
        self.assertFalse(nodeA.is_balanced())
        self.assertEqual(nodeA.d2(), 3)
        self.assertEqual(nodeA.d3(), 3)

if __name__ == "__main__":
    unittest.main()


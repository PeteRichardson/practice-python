#!/usr/bin/env python

import unittest
from ..tree_utils import Node


class Test_Node(unittest.TestCase):

    def test_single_node(self):
        nodeA = Node(43)
        self.assertTrue(nodeA.is_balanced())
        self.assertEqual(nodeA.depth(), 1)

    def test_single_child(self):
        nodeA = Node(43)
        nodeB = Node(57)
        nodeA.left = nodeB
        self.assertTrue(nodeA.is_balanced())
        self.assertEqual(nodeA.depth(), 2)

    def test_three_in_a_row(self):
        nodeA = Node(43)
        nodeB = Node(57)
        nodeC = Node(128)
        nodeA.left = nodeB
        nodeB.right = nodeC
        self.assertFalse(nodeA.is_balanced())
        self.assertEqual(nodeA.depth(), 3)

if __name__ == "__main__":
    unittest.main()


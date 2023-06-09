"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class TestNode(unittest.TestCase):

    def test_init(self):
        node1 = Node(5, None)
        node2 = Node('a', node1)
        self.assertIsInstance(node1, Node)
        self.assertIsNone(node1.next_node)
        self.assertIsInstance(node2.next_node, Node)
        self.assertEqual(node1.data, 5)
        self.assertEqual(node2.data, 'a')


class TestStack(unittest.TestCase):

    def test_init(self):
        pass

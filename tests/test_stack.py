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
        stack = Stack()
        self.assertIsNone(stack.top)
        self.assertRaises(Exception, stack.pop)

        stack.push('data1')
        stack.push('data2')
        stack.push('data3')

        self.assertEqual(stack.top.data, 'data3')
        self.assertEqual(stack.top.next_node.data, 'data2')
        self.assertEqual(stack.top.next_node.next_node.data, 'data1')
        self.assertIsNone(stack.top.next_node.next_node.next_node)
        with self.assertRaises(AttributeError):
            stack.top.next_node.next_node.next_node.data
        self.assertEqual(stack.pop(), 'data3')
        self.assertEqual(stack.top.data, 'data2')

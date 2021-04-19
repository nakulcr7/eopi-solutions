#!/usr/bin/env python3
import unittest
from eopi_solutions.stacks_and_queues import Stack, Queue, StackWithMax


class TestStackAndQueues(unittest.TestCase):
    def test_stack_size(self) -> None:
        s = Stack()
        self.assertEqual(s.size, 0)
        s.push(1)
        self.assertEqual(s.size, 1)
        s.push(2)
        self.assertEqual(s.size, 2)

    def test_stack_pop(self) -> None:
        s = Stack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

    def test_stack_pop_should_raise_error_when_empty(self) -> None:
        s = Stack()
        with self.assertRaises(IndexError):
            s.pop()
    
    def test_stack_peek(self) -> None:
        s = Stack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.peek(), 2)

    def test_stack_peak_should_raise_error_when_empty(self) -> None:
        s = Stack()
        with self.assertRaises(IndexError):
            s.peek()

    def test_queue_size(self) -> None:
        q = Queue()
        self.assertEqual(q.size, 0)
        q.enqueue(1)
        self.assertEqual(q.size, 1)
        q.enqueue(2)
        self.assertEqual(q.size, 2)

    def test_stack_pop(self) -> None:
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)

    def test_stack_pop_should_raise_error_when_empty(self) -> None:
        q = Queue()
        with self.assertRaises(IndexError):
            q.dequeue()
    
    def test_stack_peek(self) -> None:
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.peek(), 2)

    def test_stack_peak_should_raise_error_when_empty(self) -> None:
        q = Queue()
        with self.assertRaises(IndexError):
            q.peek()


    def test_stack_with_max(self) -> None:
        s = StackWithMax()
        s.push(3)
        s.push(2)
        s.push(4)
        s.push(1)
        self.assertEqual(s.max, 4)
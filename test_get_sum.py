from get_sum import get_sum
from random import random


def test_empty():
  '''empty list should return 0'''
  res = get_sum([])
  expected = 0
  assert res == expected


def test_one():
  '''list with single number should return the same'''
  res = get_sum([3])
  expected = 3
  assert res == expected


def test_one_random():
  '''list with single number should return the same'''
  num = int(100 * random())
  res = get_sum([num])
  expected = num
  assert res == expected

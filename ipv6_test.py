#!/usr/bin/env python

from ipv6 import *
import unittest

class BadAddress(unittest.TestCase):
  def test_bad_characters(self):
    badInputs = ('123.456.789', '2001:/', 'ghi')
    for s in badInputs:
      self.assertFalse(IPv6Prefix.check_characters(s))

  def test_invalid_abbreviation(self):
    badInputs = ('2001::0::0', '::1::1::', '1::::2')
    for s in badInputs:
      self.assertRaises(AbbreviationError,
          IPv6Prefix.split_abbreviation, s)

  def test_invalid_prefix_length(self):
    badInputs = ('2001::0/140', '2001::0/-30')
    for s in badInputs:
      self.assertRaises(PrefixLengthError, IPv6Prefix, s)

class AddressManipulation(unittest.TestCase):
  valid_expansions = (
      ('2001::0', '2001:0:0:0:0:0:0:0'),
      ('2001::', '2001:0:0:0:0:0:0:0'),
      ('2001:0:0:0:0:0:0:0', '2001:0:0:0:0:0:0:0'),
      ('2001:4860:4860::8844', '2001:4860:4860:0:0:0:0:8844'),
      )

  invalid_expansions = (
      '2001::1::',
      '2001::::',
      '2001:1:2:3:4:6:7:8',
      )
  def test_address_expansion(self):
    for brief,full in self.valid_expansions:
      self.assertEqual(IPv6Prefix.expand_ipv6_address(brief), full)


if __name__ == "__main__":
  unittest.main()

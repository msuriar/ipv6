#!/usr/bin/env python

from ipv6 import *
import unittest

class BadAddress(unittest.TestCase):
  def testBadCharacters(self):
    badInputs = ('123.456.789', '2001:/', 'ghi')
    for s in badInputs:
      self.assertFalse(IPv6Prefix.check_characters(s))

  def testInvalidAbbreviation(self):
    badInputs = ('2001::0::0', '::1::1::', '1::::2')
    for s in badInputs:
      self.assertRaises(AbbreviationError,
          IPv6Prefix.check_valid_abbreviation, s)

  def testInvalidPrefixLength(self):
    badInputs = ('2001::0/140', '2001::0/-30')
    for s in badInputs:
      self.assertRaises(PrefixLengthError, IPv6Prefix, s)



if __name__ == "__main__":
  unittest.main()

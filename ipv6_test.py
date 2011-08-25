#!/usr/bin/env python

import ipv6
import unittest

class BadAddress(unittest.TestCase):
  def testBadCharacters(self):
    badInputs = ('123.456.789', '2001:/', 'ghi')
    for s in badInputs:
      self.assertFalse(ipv6.checkCharacters(s))

  def testInvalidAbbreviation(self):
    badInputs = ('2001::0::0', '::1::1::', '1::::2')
    for s in badInputs:
      self.assertRaises(ipv6.InvalidAbbreviationError, ipv6.checkValidAbbreviation, s)


if __name__ == "__main__":
  unittest.main()

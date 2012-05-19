#!/usr/bin/env python
"""IPv6 utility module.

Toy utility I wrote to get my head around TDD with python. If you actually want
to do serious heavy lifting with IP addresses, use the ipaddr module here:
  http://code.google.com/p/ipaddr-py/
"""

import doctest
import re

class Error(Exception):
  """Base error class."""

class AbbreviationError(Error):
  """Invalid abbreviated IPv6 address."""

class CharacterError(Error):
  """Invalid character found in address."""

class PrefixLengthError(Error):
  """Invalid prefix length."""

class IPv6Prefix(object):
  """IPv6 prefix object. Stores an IPv6 prefix."""

  TOTAL_ADDRESS_CHUNKS = 8
  TOTAL_COLONS = TOTAL_ADDRESS_CHUNKS - 1

  def __init__(self, prefix):
    if '/' in prefix:
      self.address_str, self.prefix_length_str = prefix.split('/')
    else:
      self.address_str = prefix
      self.prefix_length_str = '128'

    self.__validate()

  def __validate(self):
    """Call individual validation methods."""
    self.__validate_address()
    self.__validate_prefix_length()

  def __validate_address(self):
    """Validate IPv6 address."""
    if not self.check_characters(self.address_str):
      raise CharacterError('Invalid character found in address.')

  def __validate_prefix_length(self):
    """Validate IPv6 prefix length."""
    if (0 <= int(self.prefix_length_str) <= 128):
      self.prefix_length = int(self.prefix_length_str)
    else:
      raise PrefixLengthError("Prefix length %s is not valid." %
                              self.prefix_length_str)


  @classmethod
  def expand_ipv6_address(cls, address):
    """Take an abbreviated IPv6 address and expand the ::"""
    separated_address = cls.check_valid_abbreviation(address)
    if separated_address:
      current_colons = sum([cls.count_colons(i) for i in separated_address])
      additional_colons = cls.TOTAL_COLONS - current_colons
      padding = r':0' * (additional_colons-1) + ':'
      return padding.join(separated_address)
    else: return 0

  @classmethod
  def check_valid_abbreviation(cls, address):
    separated_address = address.split('::')
    if (len(separated_address) == 2):
      return separated_address
    else:
      raise AbbreviationError('More than one :: in address.')

  @classmethod
  def pad_ipv6_address(cls, address):
    pass

  @classmethod
  def count_colons(cls, address):
    return address.count(':')

  @classmethod
  def check_characters(cls, address):
    RE_VALID_CHARS = re.compile(r'[^A-Fa-f0-9:]')
    search = RE_VALID_CHARS.search
    return not bool(search(address))

#!/usr/bin/env python

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
    self.__validate_address()
    self.__validate_prefix_length()

  def __validate_address(self):
    if not self.check_characters(address):
      raise CharacterError('Invalid character found in address.')

  def __validate_prefix_length(self):
    if (0 <= int(self.prefix_length_str) <= 128):
      self.prefixLength = int(self.prefix_length_str)
    else:
      raise PrefixLengthError("Prefix length %s is not valid." %
                              self.prefix_length_str)


  @classmethod
  def expand_ipv6_address(cls, address):
    pass

  @classmethod
  def calculate_pad_nibbles(cls, address):
    separated_address = cls.check_valid_abbreviation(address)
    if separated_address:
      current_colons = sum(map(cls.count_colons, separated_address))
      additional_colons = cls.TOTAL_COLONS - current_colons
      padding = r':0' * additional_colons + ':'
      return padding.join(separated_address)
    else: return 0

  @classmethod
  def check_valid_abbreviation(cls, address):
    separated_address = address.split('::')
    if (len(separated_address) == 1) and separated_address[0] == address:
      return False
    elif (len(separated_address) == 2):
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

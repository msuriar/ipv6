#!/usr/bin/env python

import doctest
import re

TOTAL_ADDRESS_CHUNKS = 8
TOTAL_COLONS = TOTAL_ADDRESS_CHUNKS - 1

class Error(Exception):
  """Base error class."""

class InvalidCharacterError(Error):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)

class InvalidAbbreviationError(Error):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)

def expandIPv6Address(address):
  if not checkCharacters(address):
    raise InvalidCharacterError('Invalid character found in address.')

def calculatePadNibbles(address):
  separated_address = checkValidAbbreviation(address)
  if separated_address:
    current_colons = sum(map(countColons, separated_address))
    additional_colons = TOTAL_COLONS - current_colons
    padding = r':0' * additional_colons + ':'
    return padding.join(separated_address)
  else: return 0

def checkValidAbbreviation(address):
  separated_address = address.split('::')
  if (len(separated_address) == 1) and separated_address[0] == address:
    return False
  elif (len(separated_address) == 2):
    return separated_address
  else:
    raise InvalidAbbreviationError('More than one :: in address.')

def padIPv6Address(address):
  pass

def countColons(address):
  return address.count(':')

def checkCharacters(address):
  validRE = re.compile(r'[^A-Fa-f0-9:]')
  search = validRE.search
  return not bool(search(address))

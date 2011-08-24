#!/usr/bin/env python

import doctest
import re


class InvalidCharacterError(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)

class InvalidAbbreviationError(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)

def expandIPv6Address(address):
  if not checkCharacters(address):
    raise InvalidCharacterError('Invalid character found in address.')

def calculatePadNibbles(address):
  if checkValidAbbreviation:
    pass
  else: return 0

def checkValidAbbreviation(address):
  separated_address = address.split('::')
  if (len(separated_address) == 1) and separated_address[0] == address:
    return False
  elif (len(separated_address) == 2):
    return True
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

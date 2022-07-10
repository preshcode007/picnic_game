#!/usr/bin/env python3
"""tests for picnic.py"""

import os
from subprocess import getoutput

prg = './picnic.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput(f'python3 {prg} {flag}')
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_one():
    """one item"""

    out = getoutput(f'python3 {prg} chips')
    assert out.strip() == 'You are bringing chips.'


# --------------------------------------------------
def test_two():
    """two items"""

    out = getoutput(f'python3 {prg} soda "french fries"')
    assert out.strip() == 'You are bringing soda and french fries.'


# --------------------------------------------------
def test_more_than_two():
    """more than two items"""

    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f'python3 {prg} {arg}')
    expected = ('You are bringing potato chips, coleslaw, '
                'cupcakes, and French silk pie.')
    assert out.strip() == expected


# --------------------------------------------------
def test_two_sorted():
    """two items sorted output"""

    out = getoutput(f'python3 {prg} -s soda candy')
    assert out.strip() == 'You are bringing candy and soda.'


# --------------------------------------------------
def test_more_than_two_sorted():
    """more than two items sorted output"""

    arg = 'bananas apples dates cherries'
    out = getoutput(f'python3 {prg} {arg} --sorting')
    expected = ('You are bringing apples, bananas, cherries, and dates.')
    assert out.strip() == expected


# -------------------------------------------------------------------------

def test_oxford_comma():
    """option for ignoring the Oxford Comma. An Oxford Comma is ...
       a comma used after the penultimate item in a list of three ...
       or more items, before ‘and’ or ‘or’ """

    arg = " cake juice orange wine"
    out = getoutput(f'python3 {prg} {arg} --comma')
    expected = ("You are bringing cake, juice, orange and wine.")

    assert out.strip() == expected

# -----------------------------------------------------------------------

def test_character_seperator ():
    arg = " apple mangoes guava"
    out = getoutput(f' python3 {prg} {arg} --char')
    expect = "You are bringing apple:mangoes:guava."
    assert out.strip() == expect
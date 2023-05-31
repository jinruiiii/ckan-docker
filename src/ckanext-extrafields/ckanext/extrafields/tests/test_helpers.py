"""Tests for helpers.py."""

import ckanext.extrafields.helpers as helpers


def test_extrafields_hello():
    assert helpers.extrafields_hello() == "Hello, extrafields!"

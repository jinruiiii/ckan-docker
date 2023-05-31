"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.extrafields.logic import validators


def test_extrafields_reauired_with_valid_value():
    assert validators.extrafields_required("value") == "value"


def test_extrafields_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.extrafields_required(None)

"""Tests for rapid-debounce-py."""

import pytest
from rapid_debounce_py import py


class TestPy:
    """Test suite for py."""

    def test_basic(self):
        """Test basic usage."""
        result = py("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            py("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = py(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities

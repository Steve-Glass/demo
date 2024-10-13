import pytest
from square_calculator import calculate_square

def test_calculate_square():
    # Test with positive numbers
    assert calculate_square(2) == 4
    assert calculate_square(3) == 9

    # Test with negative numbers
    assert calculate_square(-2) == 4
    assert calculate_square(-3) == 9

    # Test with zero
    assert calculate_square(0) == 0

    # Test with floating point numbers
    assert calculate_square(1.5) == 2.25
    assert calculate_square(-1.5) == 2.25

    # Test with edge cases
    assert calculate_square(float('inf')) == float('inf')
    assert calculate_square(float('-inf')) == float('inf')

if __name__ == "__main__":
    pytest.main()

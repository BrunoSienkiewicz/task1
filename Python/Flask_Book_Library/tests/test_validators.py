import pytest
from project.validators import validate_text

@pytest.mark.parametrize("v", ["Dune", "O'Brien", "Łódź", "Dr. Who?"])
def test_valid(v):
    assert validate_text(v, "name") == v

@pytest.mark.parametrize("v", ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>", '"><svg/onload=1>', "", "a" * 65])
def test_invalid(v):
    with pytest.raises(ValueError):
        validate_text(v, "name")
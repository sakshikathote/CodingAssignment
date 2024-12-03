
---

### File: `package_sorter.py`

```python
def sort(width, height, length, mass):
    """
    Determines the stack for a package based on dimensions and mass.
    
    Args:
        width (float): Width of the package in cm.
        height (float): Height of the package in cm.
        length (float): Length of the package in cm.
        mass (float): Mass of the package in kg.
    
    Returns:
        str: The name of the stack ('STANDARD', 'SPECIAL', 'REJECTED').
    """
    # Calculate volume
    volume = width * height * length

    # Determine if the package is bulky
    is_bulky = volume >= 1_000_000 or any(dim >= 150 for dim in [width, height, length])

    # Determine if the package is heavy
    is_heavy = mass >= 20

    # Determine the stack
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

if __name__ == "__main__":
    # Example usage
    print(sort(100, 100, 100, 5))   # STANDARD
    print(sort(200, 100, 50, 10))   # SPECIAL
    print(sort(200, 200, 50, 25))   # REJECTED

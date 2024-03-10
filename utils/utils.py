import numpy as np

def apply_precision(value, precision=2):
    """Apply the specified precision to a numeric value, a NumPy array, or to each element of a list or nested list."""
    if isinstance(value, np.ndarray):
        return np.round(value, precision)
    elif isinstance(value, list):
        # If it's a list, convert to a NumPy array, apply precision, and convert back to a list
        return np.round(np.array(value), precision).tolist()
    elif isinstance(value, (float, int)):
        return round(value, precision)
    else:
        raise TypeError("Value must be a numeric type, a list of numeric types, or a NumPy array.")

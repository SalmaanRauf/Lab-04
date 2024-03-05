# mathematics/numbers/series.py

def calculate_sum(**kwargs):
    return sum(kwargs.values())

def average(**kwargs):
    return calculate_sum(**kwargs) / len(kwargs)

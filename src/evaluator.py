import re

def extract_number(text):
    match = re.findall(r"\d+\.?\d*", text)
    return float(match[-1]) if match else None

def evaluate(pred, actual):
    return abs(pred - actual)
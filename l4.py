s = [{"name": "priya", "marks": 95},{"name": "geetha", "marks": 82},{"name": "gokul", "marks": 76},{"name": "jana", "marks": 88}
]
g = list(map(lambda x: {**x, "grade": "A" if x["marks"] >= 90 else "B" if x["marks"] >= 80 else "C"}, s))

print(g)

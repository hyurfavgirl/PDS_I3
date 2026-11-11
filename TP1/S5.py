def letter_grade(score) :
    if score > 100 and score < 0:
        return "Invalid"
    elif score >= 97:
        return "A+"
    elif score >= 90:
        return"A"
    elif score >= 80:
        return"B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else :
        return "F"

scores = [99, 90, 85.5, 72, 60, 59.9, -5, 101]

for score in scores:
    print(score, "-->", letter_grade(score))
  
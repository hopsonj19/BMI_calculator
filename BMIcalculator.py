import pytest
def getData():
    height = input("What is your height in the form -> Feet-Inches ? ")
    weight = int(input("What is your weight in pounds? "))
    calculateBMI(height, weight)

def calculateBMI(height, weight):
    heights = str.split(height, "-")
    height = int(heights[0]) * 12 + int(heights[1])
    bmi = (weight*.45)/(height*0.025)**2
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal weight"
    elif 25 <= bmi <= 29.9:
        category = "Overweight"
    elif 30 <= bmi:
        category = "Obese"
    print(height,"inches", weight,"pounds", bmi, category)
    return category


def test_under():
    assert calculateBMI("5-0", 10) == "Underweight"
    assert calculateBMI("5-0", 92) == "Underweight"

def test_normal():
    assert calculateBMI("5-0", 93) == "Normal weight"
    assert calculateBMI("5-0", 124) == "Normal weight"

def test_over():
    assert calculateBMI("5-0", 125) == "Overweight"
    assert calculateBMI("5-0", 149) == "Overweight"

def test_obese():
    assert calculateBMI("5-0", 150) == "Obese"
    assert calculateBMI("5-0", 300) == "Obese"

 
import logging
from datetime import datetime



from abc import ABC, abstractmethod


class Assessment(ABC):
    def __init__(self, score: float, weight: float):
        self.score = score
        self.weight = weight

    @abstractmethod
    def get_weighted_score(self) -> float:
        pass


class SimpleAssessment(Assessment):
    def get_weighted_score(self) -> float:
        return (self.score * self.weight) / 100


class Student:
    def __init__(self, name: str):
        self.name = name
        self.assessments = []

    def add_assessment(self, assessment: Assessment):
        self.assessments.append(assessment)

    def calculate_weighted_average(self) -> float:
        return sum(assessment.get_weighted_score() for assessment in self.assessments)

    def qualifies_for_exam(self) -> bool:
        return self.calculate_weighted_average() >= 50


def main():
    try:
        name = input("Enter student name: ")
        scores = {
            "Test 1": float(input("Enter Test 1 mark (out of 100): ")),
            "Test 2": float(input("Enter Test 2 mark (out of 100): ")),
            "Assignment 1": float(input("Enter Assignment 1 mark (out of 100): ")),
            "Project": float(input("Enter Project mark (out of 100): "))
        }

        weights = {
            "Test 1": 30,
            "Test 2": 50,
            "Assignment 1": 10,
            "Project": 10
        }

        student = Student(name)

        for key in scores:
            student.add_assessment(SimpleAssessment(scores[key], weights[key]))

        average = student.calculate_weighted_average()
        print(f"\n{name}'s weighted average: {average:.2f}")
        if student.qualifies_for_exam():
            print("Result: QUALIFIES to write the exam.")
        else:
            print("Result: DOES NOT QUALIFY to write the exam.")
    except ValueError:
        print("Invalid input. Please enter numeric marks.")


if __name__ == "__main__":
    main()



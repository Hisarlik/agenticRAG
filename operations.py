from typing import List


class Person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"Hi {self.name}"


class Alien:
    def __init__(self, name):
        self.name = name

    def yell(self):
        return f"Hi {self.name}"


def say_hey_all(people: List[Person]) -> None:
    for person in people:
        person.speak()


people = [Person("Peter"), Person("Brian"), Person("Stewie")]
aliens = [Alien("Alf"), Alien("ET"), Alien("Thanos")]

say_hey_all(people)  # Todo ok

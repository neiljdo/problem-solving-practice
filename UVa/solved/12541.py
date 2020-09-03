import sys
import math


class Person:
    def __init__(self, name=None, day=None, month=None, year=None):
        self.name = name
        self.day = day
        self.month = month
        self.year = year

    def __lt__(self, other):
        if self.year == other.year:
            if self.month == other.month:
                return self.day < other.day
            else:
                return self.month < other.month
        else:
            return self.year < other.year


def main():
    n = int(sys.stdin.readline().strip())
    people = []
    for _ in range(n):
        name, day, month, year = sys.stdin.readline().strip().split()
        people.append(Person(
            name=name,
            day=int(day),
            month=int(month),
            year=int(year)
        ))
    people.sort(reverse=True)

    print(people[0].name)
    print(people[-1].name)


if __name__ == "__main__":
    main()

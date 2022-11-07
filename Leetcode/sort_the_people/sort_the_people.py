from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        persons = {}
        sorted_people = []

        for i in range(0, len(names)):
            persons[heights[i]] = names[i]
        heights.sort(reverse=True)

        for i in range(0, len(heights)):
            sorted_people.append(persons[heights[i]])

        return sorted_people


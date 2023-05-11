"""

O método add_person possui complexidade O(1) já que realiza uma
inserção em um hashmap

O método get_score possui complexidade O(1) já que realiza uma
busca em um hashmap

"""


class Hierarchy:
    def __init__(self, k):
        self.subordinates = {}
        self.imediate_boss = {}
        self.scores = {}
        self.k = k

    def update_bosses_scores(self, boss):
        self.scores[boss] += 1
        if boss in self.imediate_boss:
            self.update_bosses_scores(self.imediate_boss[boss])

    def add_person(self, boss, person):
        if not boss:
            self.subordinates[person] = []
            self.scores[person] = 1
            return

        if len(self.subordinates[boss]) < self.k:
            self.imediate_boss[person] = boss
            self.subordinates[boss].append(person)
            self.subordinates[person] = []
            self.scores[person] = 1
            self.update_bosses_scores(boss)
        else:
            self.add_person(self.subordinates[boss][0], person)

    def get_score(self, person):
        return self.scores[person]


if __name__ == "__main__":
    hierarchy = Hierarchy(2)
    hierarchy.add_person(None, 1)
    hierarchy.add_person(1, 2)
    hierarchy.add_person(1, 3)
    hierarchy.add_person(2, 4)
    hierarchy.add_person(4, 5)
    hierarchy.add_person(4, 6)
    hierarchy.add_person(5, 7)

    print(f"Subordinates: {hierarchy.subordinates}")
    print(f"Scores: {hierarchy.scores}")

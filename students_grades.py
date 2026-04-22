from itertools import count


class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.scores[index]
        if score >= 90:
            grade = "A"
        elif score < 90 and score >= 80:
            grade = "B"
        elif score < 80 and score >= 70:
            grade = "C"
        elif score < 70 and score >= 60:
            grade = "D"
        elif score < 60 and score >= 50:
            grade = "E"
        else:
            grade = "F"
        return grade

    def find(self, points):
        points_index= []
        for i in range(len(self.scores)):
            if self.scores[i] == points:
                points_index.append(i)
        return points_index

    def get_sorted(self):
        scores = list(self.scores)
        n = len(scores)
        for i in range(n):
            for j in range(0, n - i - 1):
                if scores[j] > scores[j + 1]:
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]
        return scores




if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(results.count())  # 9
    print(results.get_by_index(2))  # 91
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]
    print(results.get_grade(index=1))
    print(results.find(100))
    print(results.get_sorted())
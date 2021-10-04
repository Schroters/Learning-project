# Making the Grade
# https://exercism.org/tracks/python/exercises/making-the-grade

def round_scores(student_scores):
    for i in range(len(student_scores)):
        student_scores[i] = round(student_scores[i])
    return student_scores


def count_failed_students(student_scores):
    fail_cnt = 0
    for i in student_scores:
        if i <= 40:
            fail_cnt += 1
    return fail_cnt


def above_threshold(student_scores, threshold):
    result = []
    for i in student_scores:
        if i >= threshold:
            result.append(i)
    return result


def letter_grades(highest):
    difference, result = round((highest - 41) / 4), [41]
    for _ in range(3):
        result.append(result[-1] + difference)
    return result


def student_ranking(student_scores, student_names):
    result = []
    for i in range(len(student_scores)):
        result.append(f"{i+1}. {student_names[i]}: {student_scores[i]}")
    return result


def perfect_score(student_info):
    for name, score in student_info:
        if score == 100:
            return [name, score]
    return "No perfect score."


print(round_scores([90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]))     # [40, 39, 95, 80, 25, 31, 70, 55, 40, 90]
print(round_scores([50, 36.03, 76.92, 40.7, 43, 78.29, 63.58, 91, 28.6, 88.0]))     # [88, 29, 91, 64, 78, 43, 41, 77, 36, 50]
print(round_scores([]))
print(round_scores([0.5]))      # 0
print(round_scores([1.5]))      # 2

print("-------------------------------------------------------------------")
print(count_failed_students([90,40,55,70,30,25,80,95,38,40]))
print(count_failed_students([89, 85, 42, 57, 90, 100, 95, 48, 70, 96]))

print("-------------------------------------------------------------------")
print(above_threshold(student_scores=[90,40,55,70,30,68,70,75,83,96], threshold=75))    # [90,75,83,96]

print("-------------------------------------------------------------------")
print(letter_grades(highest=100))   # [41, 56, 71, 86]
print(letter_grades(highest=88))    # [41, 53, 65, 77])
print(letter_grades(highest=97))    # [41, 55, 69, 83]
print(letter_grades(highest=85))    # [41, 52, 63, 74]
print(letter_grades(highest=92))    # [41, 54, 67, 80]
print(letter_grades(highest=81))    # [41, 51, 61, 71]

print("-------------------------------------------------------------------")
print(student_ranking([100, 99, 90, 84, 66, 53, 47], ['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred']))
# ['1. Joci: 100', '2. Sara: 99', '3. Kora: 90', '4. Jan: 84', '5. John: 66', '6. Bern: 53', '7. Fred: 47']

print("-------------------------------------------------------------------")
print(perfect_score(student_info=[["Charles", 90], ["Tony", 80], ["Alex", 100]]))   # ["Alex", 100]
print(perfect_score(student_info=[["Charles", 90], ["Tony", 80]]))      # "No perfect score."
print(perfect_score([['Rui', 60], ['Joci', 58], ['Sara', 91], ['Kora', 93], ['Alex', 42]]))     #  "No perfect score."

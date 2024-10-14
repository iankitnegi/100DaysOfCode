student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

total_exam_score = sum(student_scores)
max_score = max(student_scores)
print(f"Total: {total_exam_score}, Max: {max_score}")

sum_ = 0
for i in student_scores:
    sum_ += i
print("Total:", sum_)

max_ = 0
for j in student_scores:
    if max_<j:
        max_=j
print("Max:", max_)



grade_book = {
    "Alice":88,
    "Bob":74,
    "Charlie":95,
    "Diana": 82,
    "Evan":67
}
total_score = 0
for score in grade_book.values():
    total_score += score
class_average = total_score/len(grade_book)
top_student = max(grade_book, key=grade_book.get)
bottom_student = min(grade_book, key=grade_book.get)
print(f"Class Average:  {class_average}")
print(f"Top Scorer: {top_student}")
print(f"Bottom Scorer: {bottom_student}")
search = input("Enter a student's name")
student_score = grade_book.get(search)
if student_score is not None:
    print(f"{search}'s score is {student_score}.")
else:
    print(f"Student '{search}' was not found")
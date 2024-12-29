def calculate_grade(mark):
  """Calculates the grade for a given student mark.

  Args:
    mark: The student's mark as an integer or float.

  Returns:
    The corresponding grade as a string.
  """

  if mark >= 90:
    return "A"
  elif mark >= 80:
    return "B"
  elif mark >= 70:
    return "C"
  elif mark >= 60:
    return "D"
  else:
    return "F"

if __name__ == "__main__":
  try:
    mark = float(input("Enter the student's mark (0-100): "))
    if 0 <= mark <= 100:
      grade = calculate_grade(mark)
      print("Grade:", grade)
    else:
      print("Invalid mark. Please enter a value between 0 and 100.")
  except ValueError:
    print("Invalid input. Please enter a numeric value.")
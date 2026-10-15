import subprocess
import sys
from pathlib import Path

from text_similarity import calculate_similarity


# Step 1: Teacher's answer
teacher_path = Path("teacher.txt")
teacher_answer = teacher_path.read_text(encoding="utf-8")




# Step 2: Run OCR.py
print("Running OCR...")

subprocess.run(
    [sys.executable, "OCR.py"],
    check=True
)


# Step 3: Read student's answer from OCR output
file_path = Path("sample_data/extracted_text.txt")

if not file_path.exists():
    raise FileNotFoundError("OCR output file not found!")

student_answer = file_path.read_text(encoding="utf-8")


# Step 4: Calculate similarity
score = calculate_similarity(
    teacher_answer,
    student_answer
)


# Step 5: Display result
print("\n========== DHARMASCORE RESULT ==========")

print(f"Similarity Score: {score:.2f}%")

threshold = 50

if score >= threshold:
    print("Result: PASS")
else:
    print("Result: FAIL")

print("========================================")
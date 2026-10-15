import cv2
import pytesseract
from pathlib import Path


# ==========================================
# STEP 1: IMAGE PATH
# ==========================================

image_path = Path("sample_data/image.png")


# ==========================================
# STEP 2: LOAD IMAGE
# ==========================================

image = cv2.imread(str(image_path))

if image is None:
    raise FileNotFoundError(
        f"Image not found: {image_path}\n"
        "Please check the image path and filename."
    )

print("Image loaded successfully!")
print(f"Image dimensions: {image.shape[1]} x {image.shape[0]}")


# ==========================================
# STEP 3: GRAYSCALE CONVERSION
# ==========================================

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("Grayscale conversion completed!")


# ==========================================
# STEP 4: NOISE REDUCTION
# ==========================================

denoised_image = cv2.medianBlur(gray_image, 3)

print("Noise reduction completed!")


# ==========================================
# STEP 5: THRESHOLDING
# ==========================================

_, threshold_image = cv2.threshold(
    denoised_image,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

print("Thresholding completed!")


# ==========================================
# STEP 6: DISPLAY IMAGE COMPARISON
# ==========================================

# cv2.imshow("Original Image", image)
# cv2.imshow("Grayscale Image", gray_image)
# cv2.imshow("Threshold Image", threshold_image)

# print("\nPress any key on the image window to continue...")

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ==========================================
# STEP 7: OCR ON ORIGINAL IMAGE
# ==========================================

original_text = pytesseract.image_to_string(
    image,
    config="--psm 6"
)


# ==========================================
# STEP 8: OCR ON GRAYSCALE IMAGE
# ==========================================

grayscale_text = pytesseract.image_to_string(
    gray_image,
    config="--psm 6"
)


# ==========================================
# STEP 9: OCR ON THRESHOLD IMAGE
# ==========================================

threshold_text = pytesseract.image_to_string(
    threshold_image,
    config="--psm 6"
)


# ==========================================
# STEP 10: DISPLAY OCR RESULTS
# ==========================================

print("\n" + "=" * 50)
print("           ORIGINAL IMAGE OCR")
print("=" * 50)
print(original_text)


print("\n" + "=" * 50)
print("           GRAYSCALE IMAGE OCR")
print("=" * 50)
print(grayscale_text)


print("\n" + "=" * 50)
print("           THRESHOLD IMAGE OCR")
print("=" * 50)
print(threshold_text)


# ==========================================
# STEP 11: SAVE SELECTED OCR OUTPUT
# ==========================================

# For now, save the threshold image OCR result.
# We will select the best preprocessing method
# after comparing the three OCR outputs.

output_path = Path("sample_data/extracted_text.txt")

output_path.parent.mkdir(parents=True, exist_ok=True)

output_path.write_text(threshold_text, encoding="utf-8")

print("\n" + "=" * 50)
print("OCR PROCESS COMPLETED!")
print(f"Extracted text saved to: {output_path}")
print("=" * 50)
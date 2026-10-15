import cv2
import pytesseract

# Step 1: Load the image
image_path = "/Users/laleshkumar/Documents/DharmaScore/sample_data/sample-scanned-page.jpg"
image = cv2.imread(image_path)

# Step 2: Check whether the image loaded successfully
if image is None:
    print("Error: Image not found!")
else:
    # Step 3: Extract text using Tesseract OCR
    extracted_text = pytesseract.image_to_string(image)

    # Step 4: Display the extracted text
    print("\n--- Extracted Text ---\n")
    print(extracted_text)
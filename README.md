<div align="center">

# DharmaScore
### OCR and NLP-Based Answer Evaluation Model

**Extract text from answer-sheet images. Compare it with teacher-provided reference answers.**

A Python project exploring OCR, TF-IDF, and Cosine Similarity for preliminary answer comparison.

</div>

---

## 📌 Overview

**DharmaScore** is a Python-based project that explores a basic workflow for evaluating student answers. It uses **OpenCV** to preprocess answer-sheet images, **Tesseract OCR** to extract text, and **TF-IDF with Cosine Similarity** to compare the extracted text against a teacher-provided reference answer.

The current implementation applies an **experimental 50% similarity threshold** to produce a preliminary `PASS` or `FAIL` label.

> **Important:** A similarity score is not the same as academic correctness. The threshold is experimental and has not been validated as a grading standard. DharmaScore is a learning/MVP project, not a replacement for human assessment.

## ✨ Current Features

- 🖼️ Load answer-sheet images with OpenCV
- ⚙️ Preprocess images using:
  - Grayscale conversion
  - Median blur for noise reduction
  - Otsu's thresholding
- 🔎 Extract text with Tesseract OCR through Pytesseract
- 📄 Save extracted text to a text file
- 🧮 Convert student and reference answers into TF-IDF vectors
- 📐 Calculate text similarity using Cosine Similarity
- ✅ Apply an experimental 50% threshold for preliminary `PASS` / `FAIL` classification

## 🧰 Tech Stack

| Technology | Role |
|---|---|
| Python | Core implementation |
| OpenCV | Image loading and preprocessing |
| Tesseract OCR | Text recognition engine |
| Pytesseract | Python interface to Tesseract |
| NumPy | Numerical computing support |
| Scikit-learn | TF-IDF vectorization and similarity calculation |

## 🔄 Workflow

```text
Student Answer-Sheet Image
            │
            ▼
 Image Preprocessing (OpenCV)
 Grayscale → Median Blur → Otsu Thresholding
            │
            ▼
      Tesseract OCR
      (via Pytesseract)
            │
            ▼
   Extracted Student Text
            │
            ├──────────────────────┐
            │                      │
            ▼                      ▼
     Student Answer        Teacher Reference Answer
            │                      │
            └──────────┬───────────┘
                       ▼
               TF-IDF Vectorization
                       │
                       ▼
                Cosine Similarity
                       │
                       ▼
          Experimental 50% Threshold
                 ┌─────┴─────┐
                 ▼           ▼
                PASS         FAIL
```

## 📁 Project Structure

The structure below is a suggested representation. Adjust filenames to match the files currently present in your repository.

```text
DharmaScore/
├── OCR.py
├── text_similarity.py
├── main.py
├── teacher.txt
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Prerequisites

- Python installed on your system
- Tesseract OCR installed separately
- `pip` available in your Python environment

> Pytesseract is a Python wrapper; installing the Python package alone does not install the Tesseract OCR engine.

## 🚀 Getting Started

### 1. Clone the repository

Replace `<your-username>` with your GitHub username and use the actual repository name if it differs.

```bash
git clone https://github.com/<your-username>/DharmaScore.git
cd DharmaScore
```

### 2. Create and activate a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Tesseract OCR

Install the Tesseract OCR engine for your operating system and verify that it is available:

```bash
tesseract --version
```

If Tesseract is installed but its executable is not on your system `PATH`, configure the executable path in your Python environment or project configuration as appropriate.

### 5. Configure project inputs

- Provide a student answer-sheet image at the path expected by your code.
- Put the teacher's reference answer in `teacher.txt` if that is how your current implementation reads reference text.
- Check the file paths in your Python scripts before running the project.

### 6. Run the project

If `main.py` is the entry point in your current version, run:

```bash
python main.py
```

If your implementation uses a different entry point or requires command-line arguments, use the command defined in your code.

## 🧪 How It Works

### 1. Image preprocessing
OpenCV loads the image and applies grayscale conversion, median blur, and Otsu's thresholding before OCR.

### 2. OCR text extraction
Tesseract attempts to recognise text in the preprocessed image. The extracted text can be saved for inspection and later comparison.

### 3. TF-IDF representation
TF-IDF converts the student answer and reference answer into numerical vectors based on term frequency and inverse document frequency.

### 4. Cosine Similarity
Cosine Similarity compares the angle between the TF-IDF vectors. A higher score indicates greater similarity in their weighted term representations; it does **not** prove that an answer is correct.

### 5. Preliminary classification
The current experimental rule is:

| Similarity score | Output |
|---|---|
| Greater than 50% | `PASS` |
| Equal to or less than 50% | `FAIL` |

This rule is a configurable project choice, not a validated grading threshold.

## 📊 Limitations

- OCR output can contain errors, especially for handwritten, low-resolution, or poorly lit answer sheets.
- TF-IDF and Cosine Similarity mainly capture lexical overlap and may not fully recognise equivalent meaning expressed using different words.
- Similarity scores do not independently measure factual correctness or conceptual understanding.
- The 50% threshold has not been validated on a labelled evaluation dataset.
- Performance metrics and accuracy claims should only be added after systematic testing.

## 🛠️ Future Improvements

Potential improvements include:

- Testing on a diverse set of answer-sheet images
- Comparing OCR output before and after preprocessing
- Evaluating alternative OCR configurations for handwritten text
- Validating the classification threshold using labelled examples
- Exploring semantic similarity methods
- Adding a user interface or API after the core model is evaluated

These are **future possibilities**, not claims about features already implemented.

## 📚 Key Concepts

- **OCR:** Converts text in images into machine-readable text.
- **TF-IDF:** Represents text numerically by weighting terms according to their frequency and distribution.
- **Cosine Similarity:** Measures similarity between numerical vectors.
- **Image preprocessing:** Applies transformations intended to make an image more suitable for OCR.

## 👤 Author

**Project:** DharmaScore — OCR and NLP-Based Answer Evaluation Model  
**Developed using:** Python and open-source computer vision / text-processing tools

Add your name, university, course, or contact details here if you want them displayed publicly.

## 📄 License

No license has been specified in this README.

---

<div align="center">

**DharmaScore — a learning project exploring OCR and text similarity for preliminary answer comparison.**

</div>

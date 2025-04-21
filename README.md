
## ✅ Current Progress

### ✔️ Dataset

- ✅ Successfully downloaded the **RVL-CDIP** dataset (sample version for testing)
- ✅ Displayed a few samples and explored image structure

### ✔️ OCR Preprocessing

- Built a reusable **pipeline** that tests 5 preprocessing techniques:
  - Grayscale
  - Adaptive Thresholding
  - Inverted Grayscale
  - Green Color Masking
  - White Color Masking

- ✅ Evaluated each method using Tesseract OCR on a sample image
- ✅ Compared the OCR results to understand which preprocessing helps detect white/colored text better

### ✔️ Modularization

- ✅ Created a `src/preprocessing/preprocess.py` file
  - Contains utility functions:
    - `load_image()`
    - `preprocess_*()` methods
    - `ocr_pipeline()` to apply all preprocessing + OCR

---

## 🧪 Next Steps

- [ ] Improve text detection by combining multiple preprocessed results (voting/ensemble)
- [ ] Build layout analysis (bounding boxes, regions of interest)
- [ ] Fine-tune OCR accuracy with synthetic examples
- [ ] Evaluate performance on real RVL-CDIP samples
- [ ] Push project to GitHub 🚀

---

## 🛠️ Tools & Libraries

- Python 🐍
- OpenCV (`cv2`)
- Pillow (`PIL`)
- `pytesseract` (Tesseract OCR)
- `matplotlib`, `numpy`
- Jupyter & VS Code

---

## ✍️ Author

**Mariam Khedhiri**  
Data Enthusiast | Machine Learning Explorer | OCR Tinkerer  
🔗 [GitHub Profile](https://github.com/mariam-khediri) 

---

## 📌 Notes

This project is purely educational and built to simulate a real-world OCR pipeline (inspired by PixOCR). It will be continuously updated as more features are implemented.


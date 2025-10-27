# 🖼 Image Grayscale Converter (Python + OpenCV)

This project is a simple Python program that converts any image to grayscale while maintaining its original size. The user can choose whether to display the processed image or save it locally.

## 🚀 Features

✅ Converts a colored image to grayscale
✅ Keeps the original image dimensions (no resizing)
✅ Display output image in a window
✅ Option to save the processed image
✅ Simple and user-friendly input prompts

## 🛠️ Technologies Used
Tool	Purpose
Python	Programming language
OpenCV (cv2)	Image processing

## 📌 Code Overview
The program:
* Loads the image from user input path
* Converts the image from BGR to Grayscale
* Maintains original width and height
* Shows or saves the converted image based on user choice

## 📸 Example Output (Workflow)
* Input image location
* Program converts image to grayscale
* User selects:
** Display ✅
** Save ✅
* If save → asks for filename and stores the processed image locally

## ⚡ Future Enhancements (Optional)

* Add auto-image preview before saving
* Bulk image grayscale conversion
* GUI support using Tkinter or Streamlit
* Add image filters (blur, edge detection, etc.)

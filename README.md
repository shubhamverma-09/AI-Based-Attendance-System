## 🎓 AI-Based Attendance System using Face Recognition

An **AI-powered Smart Attendance System** that automatically marks student attendance using **face recognition**.
The system leverages **Machine Learning (InsightFace – FaceAnalysis)** with a **Django backend** and a **Raspberry Pi** for real-time image capture in classrooms.

---

## 🚀 Project Overview

Traditional attendance systems are time-consuming and prone to proxy attendance.
This project solves that problem by using **computer vision and deep learning** to recognize students’ faces and mark attendance automatically.

### How it works:

1. **Raspberry Pi** captures an image of the classroom.
2. The image is sent securely to the **Django backend API**.
3. **InsightFace (FaceAnalysis)** detects and recognizes student faces.
4. Recognized students are matched with registered embeddings.
5. Attendance is automatically marked in the database.

---

## 🧠 Technologies Used

### Backend

* **Django**
* **Django REST Framework**
* **Python**

### Machine Learning

* **InsightFace**
* **FaceAnalysis (Deep Face Embeddings)**
* **Cosine Similarity for Face Matching**

### Hardware

* **Raspberry Pi**
* **Raspberry Pi Camera / USB Camera**

### Database

* **MySQL**

---

## 📷 System Architecture

```
Raspberry Pi (Camera)
        |
        |  (Captured Image)
        ▼
Django REST API
        |
        |  (Face Detection & Recognition)
        ▼
InsightFace (FaceAnalysis)
        |
        |  (Matched Student IDs)
        ▼
Attendance Database
```

---

## ✨ Key Features

* ✅ Automatic attendance marking
* ✅ No proxy attendance
* ✅ Fast and accurate face recognition
* ✅ Scalable for large classrooms
* ✅ Centralized backend system
* ✅ Works in real classroom environments
* ✅ Minimal human intervention

---

## 🧩 Core Components

### 1. Student Registration

* Capture multiple face images per student
* Generate and store face embeddings
* Associate embeddings with student profiles

### 2. Face Recognition Engine

* Detect faces using **InsightFace**
* Extract embeddings using **FaceAnalysis**
* Compare embeddings using **cosine similarity**

### 3. Attendance Management

* Mark present/absent automatically
* Store date-wise attendance
* Avoid duplicate entries

---

## 📊 Accuracy & Performance

* High recognition accuracy using **deep face embeddings**
* Optimized for classroom-scale images
* Handles multiple faces in a single frame

---

## 🔒 Security & Privacy

* No raw images stored permanently
* Only encrypted face embeddings are stored
* Secure API endpoints
* Data access restricted to authorized users

---

## 🧪 Future Enhancements

* 🔹 Live video stream attendance
* 🔹 Mask detection support
* 🔹 Mobile app integration
* 🔹 Admin dashboard with analytics
* 🔹 Cloud deployment support
* 🔹 Multi-class & multi-camera support

---

## 👨‍💻 Contributors

* **Project Lead:** Piyush Ladhar
* **Team Members:** Rohit Panchariya, Shubham Verma, Yogesh Swami, Rudrakash Tiwari

---

## My Contributions

- Developed the complete Computer Vision pipeline
- Implemented face detection using OpenCV
- Built the face recognition module
- Performed image preprocessing and feature extraction
- Integrated real-time attendance marking
- Tested and optimized the detection pipeline

---

## 📜 License

This project is for **educational and research purposes**.
Feel free to modify and improve it for learning and experimentation.

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 🧠 Learn and build something amazing!

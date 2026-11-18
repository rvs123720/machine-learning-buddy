# 🤖 Machine Learning Buddy

An AI-powered educational application that helps beginners learn Machine Learning concepts through interactive explanations, real-life examples, quizzes, and answer evaluation.

## 📌 Overview

Machine Learning Buddy is a web application developed using Python and Streamlit, integrated with Google's Gemini AI.

It provides an interactive learning environment where users can explore Machine Learning topics, understand their real-world applications, practice through quizzes, and evaluate their knowledge.

## ✨ Features

### 1. Explain Concept
- Explains Machine Learning concepts in simple, beginner-friendly language.
- Provides definitions, importance, explanations, and key points.

### 2. Real-Life Example
- Generates real-world examples of Machine Learning concepts.
- Explains how these concepts are applied in everyday situations.

### 3. Generate Quiz
- Generates 5 multiple-choice questions on a selected topic.
- Provides four options for each question.
- Includes correct answers and explanations.

### 4. Ask Anything
- Allows users to ask questions about Machine Learning.
- Generates AI-powered responses using Gemini.

### 5. Evaluate My Answer
- Accepts answers submitted by students.
- Identifies correct and incorrect points.
- Provides suggestions for improvement.
- Assigns a score out of 10.

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Frontend:** Streamlit
- **AI Integration:** Google Gemini AI
- **SDK:** Google Generative AI Python SDK

## 📁 Project Structure

```text
Machine-Learning-Buddy/
│
├── app.py
├── requirements.txt
├── README.md
└── .streamlit/
    └── secrets.toml
```

## ⚙️ Installation and Setup

### Prerequisites
- Python 3.8+
- pip
- Google Gemini API Key

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd Machine-Learning-Buddy
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Create a `.streamlit` folder in the project directory.

Inside it, create a `secrets.toml` file:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Replace the placeholder with your actual Gemini API key.

**Important:** Never upload your API key or `secrets.toml` file to GitHub.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your default browser.

## 🔌 API Integration

The application integrates Google's Gemini AI using the `google-generativeai` Python SDK.

- Configures the API key through Streamlit secrets.
- Uses the `gemini-flash-latest` model.
- Generates responses based on the user's selected activity and input.

## 📦 Requirements

The project dependencies are listed in `requirements.txt`:

```text
streamlit
google-generativeai
```

## 🎯 Project Objective

To make Machine Learning education more accessible and engaging for beginners through AI-powered explanations, interactive practice, and personalized feedback.

## 👩‍💻 Author

**RV Srujana**

Computer Science and Engineering  
Vasavi College of Engineering

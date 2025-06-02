# 🌍 Geography Quiz App with Streamlit  [👉 GO TO WEBSITE](https://abhikgeo.streamlit.app/)

Welcome to the **Geography Quiz App**, an interactive and educational web application built with **Streamlit** and **Pandas**. This app helps users test and improve their knowledge of world capitals and continents in a fun and gamified way!

---

## 🎯 Features

- **Capital City Quiz (Tab 1):**
  - Choose from six continents: Asia, Europe, North America, South America, Australia, and Africa.
  - Five difficulty levels (based on question sets) per continent.
  - Multiple-choice questions for each capital city.
  - Real-time scoring, feedback, and correct answers shown for incorrect responses.
  - Visuals for each continent enhance the learning experience.

- **Country-Continent Quiz (Tab 2):**
  - Identify the correct continent for a randomly selected country.
  - 10 levels, each with a new set of 10 questions (randomized at the start of each session).
  - Immediate feedback with correct answers for wrong responses.
  - Score summary and motivational animations based on performance.

- **User-Friendly Interface:**
  - Powered by Streamlit’s form functionality and layout options.
  - Clean, responsive design with dynamic content switching via tabs and radio buttons.

---

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Pandas**
- **CSV file** (for storing quiz questions and answers)
- **Images** (used to represent continents visually)

---

## 📁 Project Structure

```

.
├── app.py                     # Main Streamlit application script
├── capitals\_city.csv          # CSV file with questions, options, and answers
├── images/
│   ├── asia.png
│   ├── europe.png
│   ├── north\_america.png
│   ├── south\_america.png
│   ├── australia.png
│   ├── africa.png
│   └── world\_map\_3360.jpg
├── README.md                  # Project documentation
├── requirements.txt           # Required library with versions for streamlit hosting



````

---

## 🧠 Data Format (`capitals_city.csv`)

Ensure your CSV file contains the following columns:

- `question`: The quiz question
- `option1`, `option2`, `option3`, `option4`: Multiple choice options
- `answer`: The correct option
- `continent`: The corresponding continent
- `country`: Country name (used in Tab 2)

---

## 👨‍💻 Author

**Partho Sarothi Das**
*Aspiring Data Scientist | Passionate about ML & Visualization*
📧 [partho52@gmail.com](mailto:partho52@gmail.com)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

### 🌟 If you find this useful, give it a ⭐ and share it with others!

```

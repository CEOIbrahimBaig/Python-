# Gym Progress & Fitness Analytics Tracker

An analytics project built to track, analyze, and visualize a 12-week (84 days) fitness journey. This project utilizes foundational data science tools in Python to process daily body metrics, nutritional intake, and strength progression.

## 📊 Features & Project Scope

### 1. Data Generation & Structuring (NumPy & Pandas)
* **Timeline Simulation:** Generates sequential daily data spanning 12 continuous weeks.
* **Synthetic Metrics:** Uses **NumPy** arrays to model realistic body weight fluctuations, daily caloric targets, protein intake, and lifting maxes (Bench Press and Squat).
* **Data Integration:** Compiles multi-dimensional numerical inputs into a structured **Pandas** DataFrame.

### 2. Fitness Analytics (Pandas Data Manipulation)
* **Trend Smoothing:** Calculates a 7-day rolling average of body weight to filter out daily water retention noise.
* **Nutritional Insights:** Extracts descriptive statistics (minimum, maximum, and average values) for daily macro consumption.
* **Milestone Tracking:** Filters and queries the dataset to identify specific calendar dates when personal lifting records (PRs) were achieved.

### 3. Visual Analytics Dashboard (Matplotlib Layouts)
The project generates a clean, multi-panel visualization interface using `plt.subplots()` to display four core areas of fitness analysis:

* **Weight Trend Analysis:** A dual-layered line plot displaying daily weight fluctuations against the 7-day rolling average progression trend line.
* **Diet vs. Strength Correlation:** A scatter plot mapping daily calorie intake directly against Bench Press maxes to observe strength correlation.
* **Caloric Distribution:** A customized histogram illustrating the consistency of nutritional intake against target goals.
* **Strength Progression:** A multi-line graph detailing the 12-week trajectory of Squat and Bench Press limits complete with legends, labels, and formatted axes.

---

## 🛠️ Tech Stack & Concepts Applied

* **NumPy:** Array initialization, random distribution generation, and data alignment.
* **Pandas:** DataFrame creation, data cleaning, rolling windows (`.rolling()`), and conditional querying.
* **Matplotlib:** Subplot axis management (`fig, axs`), custom line styling, marker selection, histograms, scatter plots, and legend formatting.

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
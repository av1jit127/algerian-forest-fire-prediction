# Algerian Forest Fires — FWI Prediction & Analysis

An end-to-end Machine Learning regression project that predicts the **Fire Weather Index (FWI)** using meteorological observations and fire index components from the Algerian Forest Fires dataset. The repository covers complete data preprocessing, exploratory data analysis, multicollinearity mitigation, regularization model benchmarks, and deployment artifacts.

---

## 📌 Project Overview

* **Dataset:** Algerian Forest Fires Dataset (Bejaia and Sidi-Bel Abbes regions).
* **Target Feature:** `FWI` (Fire Weather Index).
* **Core Problem:** Regression task predicting fire weather severity based on weather data and fuel moisture codes.
* **Best Performing Models:** Linear Regression ($R^2 \approx 0.985$, $\text{MAE} \approx 0.547$) and RidgeCV ($R^2 \approx 0.984$, $\text{MAE} \approx 0.564$).

---

## 🛠️ Data Pipeline & Workflow

1. **Data Cleaning & Wrangling:**
   * Handled dual-region structure by segmenting Bejaia (Region 0) and Sidi-Bel Abbes (Region 1).
   * Cleaned redundant header rows and formatted column whitespace.
   * Converted numerical string objects to standard integer and floating-point types.
   * Encoded categorical `Classes` into binary format (`0: not fire`, `1: fire`).

2. **Feature Selection & Engineering:**
   * Dropped non-predictive temporal variables (`day`, `month`, `year`)[cite: 1].
   * Analyzed Pearson correlation matrices to prevent multicollinearity[cite: 1].
   * Filtered out highly collinear features using a Pearson threshold of $\vert{}r\vert{} > 0.85$ (dropping `BUI` and `DC`)[cite: 1].

3. **Standardization:**
   * Train-test split (75/25 ratio, `random_state=42`)[cite: 1].
   * Fitted `StandardScaler` strictly on the training set and transformed test data to prevent data leakage[cite: 1].

4. **Model Training & Benchmarking:**
   * Evaluated multiple regression algorithms including **Linear Regression**, **Lasso**, **LassoCV**, **Ridge**, **RidgeCV**, **ElasticNet**, and **ElasticNetCV**[cite: 1].

---

## 📊 Model Evaluation Results

| Model | MAE | $R^2$ Score |
|---|---|---|
| **Linear Regression** | **0.5468**[cite: 1] | **0.9848**[cite: 1] |
| **Ridge Regression** | 0.5642[cite: 1] | 0.9843[cite: 1] |
| **RidgeCV (5-Fold)** | 0.5642[cite: 1] | 0.9843[cite: 1] |
| **LassoCV (5-Fold)** | 0.6199[cite: 1] | 0.9821[cite: 1] |
| **ElasticNetCV (5-Fold)** | 0.6576[cite: 1] | 0.9814[cite: 1] |
| **Lasso Regression** | 1.1332[cite: 1] | 0.9492[cite: 1] |
| **ElasticNet Regression** | 1.8822[cite: 1] | 0.8753[cite: 1] |

---

## 📁 Repository Structure

```text
├── algerianFireDataSet.ipynb               # Full EDA, cleaning, and model training notebook
├── app.py                                  # Streamlit web application
├── scaler.pkl                              # Pre-trained StandardScaler object
├── ridgecv.pkl                             # Trained RidgeCV model artifact
├── requirements.txt                        # Project dependencies
└── README.md                               # Project documentation

# 🌲 Algerian Forest Fire Prediction

An interactive web application built with **Streamlit** and **Machine Learning** to predict forest fire occurrences and risk indices based on meteorological and environmental parameters from Algerian forest regions (Bejaia and Sidi Bel-abbes).

🔗 **Live Demo:** [algerian-forest-fire-predictionn.streamlit.app](https://algerian-forest-fire-predictionn.streamlit.app/)

---

## 📌 Project Overview

Forest fires pose significant threats to ecological balance, property, and human lives. This project leverages historical meteorological data from the **UCI Algerian Forest Fires Dataset** to predict fire risk.

The application allows users to input real-time weather readings (temperature, humidity, wind, rainfall) alongside Fire Weather Index (FWI) components to evaluate fire probability and risk severity.

---

## ✨ Features

- **Interactive UI:** Intuitive parameter input via sliders and numerical input fields.
- **Instant Predictions:** Real-time ML model inference for fire occurrence / Fire Weather Index (FWI).
- **Metric Insights:** Clear visualization of input conditions against critical fire threshold levels.
- **Fully Deployed:** Cloud-hosted and accessible via Streamlit Community Cloud.

---

## 📊 Dataset & Features

The model uses meteorological records and components of the Canadian Forest Fire Weather Index (FWI) System:

| Feature | Description | Unit / Range |
|---|---|---|
| **Temperature** | Noon maximum temperature | °C (22 – 42) |
| **RH** | Relative Humidity | % (21 – 90) |
| **Ws** | Wind Speed | km/h (6 – 29) |
| **Rain** | Total daily rainfall | mm (0 – 16.8) |
| **FFMC** | Fine Fuel Moisture Code | 28.6 – 92.5 |
| **DMC** | Duff Moisture Code | 1.1 – 65.9 |
| **DC** | Drought Code | 7 – 220.4 |
| **ISI** | Initial Spread Index | 0 – 18.5 |
| **BUI** | Buildup Index | 1.1 – 68 |
| **FWI** | Fire Weather Index (Target) | 0 – 31.1 |

---

## 🛠️ Tech Stack

- **Frontend & App Framework:** [Streamlit](https://streamlit.io/)
- **Machine Learning & Preprocessing:** `scikit-learn`, `numpy`, `pandas`
- **Data Visualization:** `seaborn`, `matplotlib`
- **Model Serialization:** `pickle` / `joblib`
- **Deployment:** Streamlit Cloud

---

## 🚀 Getting Started Locally

Follow these steps to run the application on your local machine:

### 1. Clone the repository
```bash
git clone [https://github.com/](https://github.com/)<your-username>/<your-repo-name>.git
cd <your-repo-name>

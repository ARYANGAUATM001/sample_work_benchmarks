# Cascaded Tanks Benchmark – System Identification

This project presents a small work sample for nonlinear system identification using the **Cascaded Tanks benchmark**.

## 📌 Objective

The goal is to model the system dynamics and compare:

* A **linear baseline model (ARX)**
* A **nonlinear model (NARX Neural Network)**

Both models are trained on the provided dataset and evaluated in **simulation mode**, following the benchmark guidelines.

---

## ⚙️ Methodology

### 1. Data

* Dataset: Cascaded Tanks benchmark
* Train/test split provided by the benchmark
* Evaluation uses only the allowed initialization window

### 2. Models

#### 🔹 ARX (Linear Model)

* Uses past inputs and outputs
* Implemented using linear regression
* Serves as a baseline

#### 🔹 NARX Neural Network

* Uses lagged inputs and outputs
* Implemented using a multi-layer perceptron (MLP)
* Captures nonlinear system dynamics

---

## 📊 Results

| Model               | RMSE  |
| ------------------- | ----- |
| ARX (Linear)        | ~4.55 |
| NARX Neural Network | ~5.08 |

> The nonlinear model required stabilization during simulation and showed slightly lower performance compared to the linear baseline in this setup.

---

## 📈 Model Comparison

The following plot shows the true system output along with predictions from both models:

![Model Comparison](results/model_comparison.png)

---

## 🧠 Observations

* The ARX model provides a stable and reasonable approximation of the system.
* The NARX model captures some nonlinear behavior but required stabilization during simulation.
* Training nonlinear dynamic models is more sensitive to errors due to feedback in simulation.

---

## 🚀 How to Run

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the main script:

   ```bash
   python main.py
   ```

3. Output:

   * RMSE values printed in console
   * Plot saved in `results/` folder

---

## 📁 Project Structure

```
.
├── main.py
├── utils.py
├── models/
│   ├── arx_Model.py
│   └── narx_nn_model.py
├── results/
│   └── model_comparison.png
├── requirements.txt
└── .gitignore
```

---

## ✅ Summary

This project demonstrates:

* Implementation of linear and nonlinear system identification models
* Proper evaluation using simulation-based prediction
* Comparison using both quantitative (RMSE) and qualitative (plots) analysis

---

## 👤 Author

Aryan Gautam

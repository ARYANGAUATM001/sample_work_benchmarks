# Cascaded Tanks Benchmark – System Identification

This project presents a work sample for **nonlinear system identification** using the **Cascaded Tanks benchmark dataset**.

---

## 📌 Objective

The goal is to model the system dynamics and compare:

- A **linear baseline model (ARX)**
- A **nonlinear model (NARX Neural Network)**

Both models are trained on the provided dataset and evaluated in **simulation mode**, following the official benchmark guidelines.

---

## ⚙️ Methodology

### 1. Data

- Dataset: Cascaded Tanks benchmark  
- Predefined train/test split  
- Evaluation uses only the **initialization window (`y[:n]`)**, with the rest predicted autoregressively  

### 2. Models

#### 🔹 ARX (Linear Model)

- Uses past inputs and outputs  
- Implemented using linear regression  
- Serves as a simple and stable baseline  

#### 🔹 NARX Neural Network

- Uses lagged inputs and outputs  
- Implemented using a multi-layer perceptron (MLP)  
- Designed to capture nonlinear system behavior  

---

## 📊 Results

| Model               | RMSE  |
|--------------------|------|
| ARX (Linear)       | ~4.55 |
| NARX Neural Network| ~5.08 |

> The nonlinear model required stabilization during simulation and showed slightly lower performance compared to the linear baseline.

---

## 📈 Model Comparison

The plot below compares the true system output with predictions from both models:

![Model Comparison](results/model_comparison.png)

---

## 🧠 Observations

- The **ARX model** provides stable and consistent predictions.  
- The **NARX model** captures some nonlinear patterns but is sensitive during simulation.  
- Autoregressive prediction introduces **error accumulation**, making nonlinear models harder to stabilize.  

---

Summary :

This project demonstrates:

Implementation of linear and nonlinear system identification models
Proper simulation-based evaluation following benchmark rules
Clear comparison using both quantitative (RMSE) and qualitative (plots) analysis

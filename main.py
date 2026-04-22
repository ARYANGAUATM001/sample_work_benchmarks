import nonlinear_benchmarks

from models.arx_Model import train_arx
from models.narx_nn_model import train_narx_nn
from utils import simulate

from nonlinear_benchmarks.error_metrics import RMSE

# ===============================
# Load data (KEEP EXACT)
# ===============================
train, test = nonlinear_benchmarks.Cascaded_Tanks()
n = test.state_initialization_window_length

# ===============================
# Train models
# ===============================
model_arx = train_arx(train)
model_narx = train_narx_nn(train)

# ===============================
# Apply models (IMPORTANT RULE)
# ===============================
y_arx = simulate(model_arx, test.u, test.y[:n])
y_narx = simulate(model_narx, test.u, test.y[:n])

# ===============================
# Evaluate
# ===============================
y_arx = y_arx[:len(test.y)]
y_narx = y_narx[:len(test.y)]

rmse_arx = RMSE(test.y[n:], y_arx[n:])
rmse_narx = RMSE(test.y[n:], y_narx[n:])

# ===============================
# Print results
# ===============================
print(f"ARX (Linear) RMSE: {rmse_arx:.3f}")
print(f"NARX Neural Net RMSE: {rmse_narx:.3f}")

if rmse_narx < rmse_arx:
    print("Best model: NARX NN (captures nonlinear dynamics)")
else:
    print("Best model: ARX (simpler but less expressive)")




import os
import matplotlib.pyplot as plt

# create folder if not exists
os.makedirs("results", exist_ok=True)

plt.figure(figsize=(10, 4))

plt.plot(test.y, label="True Output", linewidth=2)
plt.plot(y_arx, label="ARX Prediction")
plt.plot(y_narx, label="NARX Prediction")

plt.legend()
plt.title("Model Comparison - Cascaded Tanks")

plt.tight_layout()

# ✅ save inside project/results/
plt.savefig("results/model_comparison.png", dpi=300)


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

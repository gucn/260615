# Unbalanced dataset generator
# Generates a mock .csv of patient data
# Lower values are considered healthier

import numpy as np
import pandas as pd
np.random.seed(137) # predetermined seed for reproducibility

n_healthy=15
n_sick=5
data=[]

# Healthy patient data generator
for i in range(n_healthy):
	patient = f"Patient{i+1}"
	val1 = np.random.randint(10, 60)
	val2 = np.random.randint(200, 600)
	data.append([patient, val1, val2, "Healthy"])


# Diseased patient data generator
for i in range(n_sick):
	patient = f"Patient{n_healthy+i+1}"
	val1 = np.random.randint(50, 100)
	val2 = np.random.randint(400, 1000)
	data.append([patient, val1, val2, "Diseased"])

# Create dataframe and print to csv
df = pd.DataFrame(data, columns=["Patient","Val1","Val2","Status"])
df.to_csv("init_data.csv", index=False)
print("Initial data has been created")
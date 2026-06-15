# Balanced dataset generator
# 1. Takes the output of generate.py as input
# 2. Reports the minority
# 3. Generates data points using the following formula
# newPoint = oldPoint1 + x(OldPoint2 - OldPoint1)
# where x is a randomly assigned weight value between 0 and 1
# 4. Appends the generated data points to the initial dataset
# and outputs a new csv

import numpy as np
import pandas as pd
np.random.seed(137) # predetermined seed for reproducibility

# group the input by Status value and print the qty of each
df = pd.read_csv("init_data.csv")
groups = df.groupby("Status")
status_count = groups.size()
print("Status distribution:")
print(status_count.to_string())

# print the majority and minority Status by name
print ("Majority status:", status_count.idxmax())
print ("Minority status:", status_count.idxmin())

# determine and print how many samples are needed
# to equal majority to minority
points_needed = status_count.max() - status_count.min()
print (points_needed, "samples are needed.")

# create dataframe in which Status = minority status
minority_status = status_count.idxmin()
minority_df = df[df["Status"] == minority_status]

# create a new list to store the newly generated points in
# generate the new points according to the formula previously mentioned
# generated data points are rounded to integers for aesthetic reasons

synth_samples = []

for i in range(points_needed):
	# randomly pick 2 minority rows
	samples = minority_df.sample(2)
	a = samples.iloc[0]
	b = samples.iloc[1]
	x = np.random.rand() # randomly pick weight
	# generate the new new data point
	new_Val1 = int(round(a["Val1"] + x * (b["Val1"] - a["Val1"])))
	new_Val2 = int(round(a["Val2"] + x * (b["Val2"] - a["Val2"])))

	synth_samples.append([
		f"Synth{i+1}", new_Val1, new_Val2, minority_status
		])

# convert the list to a dataframe and
# append to the initial dataset

synth_df = pd.DataFrame(
	synth_samples, columns=["Patient", "Val1", "Val2", "Status"])
balanced_df = pd.concat([df, synth_df], ignore_index=True)
balanced_df.to_csv("balanced_data.csv", index=False)
print("Balanced dataset has been created")

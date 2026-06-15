OVERVIEW

This project generates a small synthetic dataset with an intentional class imbalance and balances it using a simple interpolation method inspired by SMOTE.

It includes two scripts:
1. generate.py (Generates the unbalanced dataset)
2. balance.py (Generates synthetic samples to balance the dataset)

PROJECT STRUCTURE

.
|__ generate.py			# creates unbalanced dataset
|__ balance.py			# uses interpolation to create balanced dataset
|__ init_data.csv		# output ot generate.py
|__ balanced_data.csv	# output of balance.py
L__ readme.txt

DATASET DESCRIPTION

Patient: patient number/identifier
Val1: an integer between 10-100
Val2: an integer between 200-1000
Status: class label (Healthy or Diseased)

Note: Status is not a derived value and imagined to be assigned by a doctor.

HOW IT WORKS

1. Generate imbalanced dataset using generate.py

	a. Randomly generate mock patient records
	b. Assigns
		- Higher count to Diseased patients
		- Lower count to Healthy patients
	c. Saves output as init_data.csv

2. Analyse imbalance using balance.py

	a. Load init_data.csv
	b. Group data by Status
	c. Print
		- Class distribution
		- Majority
		- Minority
		- Number of synthetic samples needed

3. Generate synthetic samples to balance the dataset (inspired by SMOTE)

	New samples are created using linear interpolation but simple averaging is avoided by using a random weight called x. Unlike SMOTE, the samples to be interpolated upon are chosen randomly within the minority group and are not necessarily closest neighbours.

	The formula for the interpolation is: new_point = a + x(b-a)
	where a, b = randomly selected minority samples
	x = random weight between 0 and 1

	The resulting point is rounded to an integer for visual consistency.

4. Output

	The synthetic samples are appended to the original data and exported as balanced_data.csv

HOW TO RUN

python generate.py
python balance.py

NOTES

- The random seed is fixed for reproducibility

POSSIBLE ADDITIONS

1. Implement nearest neighbour selection instead or random
2. Data visualisation using scatter plots
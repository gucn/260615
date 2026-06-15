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

AI DISCLOSURE AND REMARKS

1. Since Google searches now return an AI Overview, the phrase (prompt) "examples of oversampling methods" returned a summary of ROS, SMOTE, ADASYN among others.

After reading the summary, I decided to learn more about SMOTE over ROS because I thought duplication of existing data in a medical/patient context might lead to duplication of unconsidered traits and over-emphasise unforeseen correlations. Other methods sounded too complex for the scope of this task.

2. ChatGPT was used to inquire about the SMOTE algorithm. The prompt was "can you explain how the SMOTE algorithm for data balancing works step by step through pseudocode?"

ChatGPT told me SMOTE is similar to "data hallucination", which I thought was a hilarious analogy coming from an LLM.

I learned that SMOTE picks closest neighbours. I decided to pick random points within the minority group to simplify the task. I feel like this results in "weaker" generated samples for the same reason I thought ROS was a weaker algorithm: data points that are naturally far away might have an underlying correlation. Picking such samples and taking their weighted average might result in unrealistic data points.

3. ChatGPT was used to inquire about the structure of a readme file. The prompt was: "i have the following python code. it works as intended. now i'm writing the readme file but i'm not sure what i should include. can you give me a template?" [code omitted for brevity]

I largely followed ChatGPT's answer (but haven't copy-pasted) because I had never needed to write a readme file before.

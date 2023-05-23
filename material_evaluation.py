import numpy as np
import pandas as pd
import scipy as sp
import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

# Read Course Materials CSV and display values
materials_csv_data=pd.read_csv("course_materials_new.csv")
print(materials_csv_data.shape)
print(materials_csv_data)

# Read Rating Scales CSV and display values
rating_csv_data=pd.read_csv("rating_scale.csv")
print(rating_csv_data.shape)
print(rating_csv_data)

# Generate 100 Random Student Evaluations for each training course based on the scale
rng = np.random.default_rng(seed=0)
student_evaluations = rng.integers(1, high=6, size=(100,12))
print(student_evaluations)

# Convert array into dataframe for visualization
evaluations_df = pd.DataFrame(student_evaluations, columns = ['Reproducibility in Life Sciences', 'Terminal and Bash', 'Introduction to Python', 'Scientific Python: NumPy and Scipy', 'Introduction to Git and GitHub', 'Data Wrangling with Pandas', 'Classical statistics pitfalls and remedies', 'Machine Learning 1: Supervised Learning', 'Machine Learning 2: Model selection validation', 'Introduction to Data Visualization', 'Containers', 'High Performance Computing'])
print(evaluations_df)

# Histograms for student evaluations
life_science_histogram = evaluations_df.plot.hist(column=['Reproducibility in Life Sciences'])
plt.savefig('life_science_histogram.png')

terminal_bash_histogram = evaluations_df.plot.hist(column=['Terminal and Bash'])
plt.savefig('terminal_bash.png')

python_histogram = evaluations_df.plot.hist(column=['Introduction to Python'])
plt.savefig('python.png')

numpy_scipy_histogram = evaluations_df.plot.hist(column=['Scientific Python: NumPy and Scipy'])
plt.savefig('numpy_scipy.png')

github_histogram = evaluations_df.plot.hist(column=['Introduction to Git and GitHub'])
plt.savefig('github.png')

pandas_histogram = evaluations_df.plot.hist(column=['Data Wrangling with Pandas'])
plt.savefig('pandas.png')

stats_histogram = evaluations_df.plot.hist(column=['Classical statistics pitfalls and remedies'])
plt.savefig('stats.png')

m1_histogram = evaluations_df.plot.hist(column=['Machine Learning 1: Supervised Learning'])
plt.savefig('m1.png')

m2_histogram = evaluations_df.plot.hist(column=['Machine Learning 2: Model selection validation'])
plt.savefig('m2.png')

vis_histogram = evaluations_df.plot.hist(column=['Introduction to Data Visualization'])
plt.savefig('vis.png')

containers_histogram = evaluations_df.plot.hist(column=['Containers'])
plt.savefig('containers.png')

hpcomputing_histogram = evaluations_df.plot.hist(column=['High Performance Computing'])
plt.savefig('hpcomputing.png')

# Convert CSV file into a list
#material_csv = 'course_materials_new.csv'
#with open(material_csv) as f:
 #   reader = csv.reader(f)
  #  lst = list(reader)

#Convert list into numpy array
#material_array = np.array(lst)
#print(material_array)


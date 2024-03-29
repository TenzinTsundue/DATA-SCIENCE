
# Go Beyond the Numbers: Translate Data into insights
Week 1: Find and share stories using data ✅ <br>
Week 2: Explore raw data ✅<br>
Week 3: Clean your data <br>
Week 4: Data visualization and presentations <br>
Week 5: end-of-course project <br>

### Week 1: Find and share stories using data <br>

Exploratory data analysis (EDA): The process of investigating, organizing, and analyzing datasets and summarizing their main characteristics, often employing data wrangling and visualization methods <br>
* Discovering: Data professionals familiarize themselves with the data so they can start conceptualizing how to use it.
* Structuring: The process of taking raw data and organizing or transforming it to be more easily visualized, explained, or modeled
* Cleaning: The process of removing errors that may distort your data or make it less useful
* Joining: The process of augmenting or adjusting dat any adding values from other datasets
* Validating: The process of verifying that the data is consistent and high quality
* Presenting: Making your cleaned dataset or data visualizations available to others for analysis or further modeling

Data Visualization: A graph, chart, diagram, or the dashboard that is created as a representation of information  <br>

Case study | Deloitte [Coursera | Online Courses & Credentials From Top Educators. Join for Free | Coursera](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/supplement/b7ThI/case-study-deloitte) <br>

Reference guide: The EDA process[Coursera | Online Courses & Credentials From Top Educators. Join for Free | Coursera](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/supplement/MR1G3/reference-guide-the-eda-process)

*Bias*: In data structuring, refers to organizing data results in groupings, categories, or variables that are misrepresentative of the whole dataset <br>				
*Cleaning*: The process of removing errors that might distort your data or make it less useful; one of the six practices of EDA <br>
*Data visualization*: A graph, chart, diagram, or dashboard that is created as a representation of information <br>
*Discovering*: The process data professionals use to familiarize themselves with the data so they can start conceptualizing how to use it; one of the six practices of EDA	 <br>
*Exploratory data analysis (EDA)*: The process of investigating, organizing, and analyzing datasets and summarizing their main characteristics, often by employing data wrangling and visualization methods; the six main practices of EDA are: discovering, structuring, cleaning, joining, validating, and presenting <br>					
*Joining*: The process of augmenting data by adding values from other datasets; one of the six practices of EDA <br>
*PACE*: A workflow data professionals can use to remain focused on the end goal of any given dataset; stands for plan, analyze, construct, and execute <br>
*Presenting*: The process of making a cleaned dataset available to others for analysis or further modeling; one of the six practices of EDA <br>
*Structuring*: The process of taking raw data and organizing or transforming it to be more easily visualized, explained, or modeled; one of the six practices of EDA <br>
*Validating*: The process of verifying that the data is consistent and high quality; one of the six practices of EDA <br>	

### Week 2: Explore raw data <br>

First-party data is data that was gathered from inside your own organization.  <br>
Second-party data was gathered outside your organization but directly from the original source.  <br>
Third-party data, which is data gathered outside your organization and aggregated. <br>

head(), info(), describe() and shape <br>

Hypothesis: A theory or an explanation, based on evidence, that is not yet proved true. <be>

Sorting | Extracting | Filtering | Slicing | Grouping | Merging  <br>

```
df.merge()
pd.concat()
df.join()
df.select_dtypes
df[condition]
pd.sort_values()
df.iloc[]
df.loc[]
```
EDA structuring with Python [Coursera | Online Courses & Credentials From Top Educators. Join for Free | Coursera](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/ungradedLab/WMxxI/annotated-follow-along-guide-eda-structuring-with-python/lab?path=%2Fnotebooks%2FAnnotated%2520follow-along%2520guide_%2520EDA%2520structuring%2520with%2520Python.ipynb) <br>

Histograms: Symmetric | Skewed | Bimodal | Uniform <br>

Activity: [Coursera | Online Courses & Credentials From Top Educators. Join for Free | Coursera](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/ungradedLab/gr3qN/activity-structure-your-data/lab?path=%2Fnotebooks%2FActivity_Structure%2520your%2520data.ipynb) <br>

Exemplar: [Coursera | Online Courses & Credentials From Top Educators. Join for Free | Coursera](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/ungradedLab/A0hlQ/exemplar-structure-your-data/lab?path=%2Fnotebooks%2FExemplar_Structure%2520your%2520data.ipynb) <br>

*Box plot:*A data visualization that depicts the locality, spread, and skew of groups of values within quartiles <br>
*CSV file*: A simple text file that can be easy to import or store in other softwares, platforms, and databases <br>
*Database (DB) file*: A file type used to store data, often in tables, indexes, or fields <br>
*Data source:* The location where data originates <br>
*Extracting:* The process of retrieving data out of data sources for further data processing or storage <br>
*Filtering:* The process of selecting a smaller part of a dataset based on specified values and using it for viewing or analysis <br>
*First-party data:* Data that was gathered from inside your own organization <br>
*Grouping*: The process of aggregating individual observations of a variable into groups <br>
*Hypothesis:* A theory or an explanation, based on evidence, that is not yet proven true <br>
*Info():* Gives the total number of entries, along with the data types—called Dtypes in pandas—of the individual entries <br>
*Int64:* A standard integer data type, representing numbers somewhere between negative nine quintillion and positive nine quintillion <br>
*JSON file:*A data storage file that is saved in a JavaScript format <br>
*Merging:* A method to combine two (or more) different data frames along a specified starting column(s) <br>
*Second-party data:* Data that was gathered outside your organization but directly from the original source <br>
*Slicing:*A method for breaking information down into smaller parts to facilitate efficient examination and analysis from different viewpoints <br>
*Sorting:*The process of arranging data into a meaningful order for analysis <br>
*String:* A sequence of characters and punctuation that contains textual information <br>
*Third-party data:*Data gathered outside your organization and aggregated <br>

### Week 3: Clean your data  <br>

The 6 Practices of EDA
1. Discovering
2. Structuring
3. Cleaning
4. Joining
5. Validating
6. Presenting

Missing data (or null values): A value that is not stored for a variable in a set of data. <br>

A zero (0) could be considered a missing value, but in other datasets could be legitimate data point. <br>

What to do with missing data <br>
* Request the missing values to b filled in by the owner of the data
* Delete the missing columns(s), row(s), or value(s)
* Create a NaN category
* Derive new representative values(s)

Derive new representative value(s) strategy
* Forward filling
* Backward filling (backfilling)
* Deriving mean values
* Deriving median values
* 
Working with missing data [Coursera | Online Courses & Credentials From Top Educators. Join for Free | Coursera](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/ungradedLab/E5TwS/annotated-follow-along-guide-work-with-missing-data-in-a-python-notebook/lab?path=%2Fnotebooks%2FAnnotated%2520follow-along%2520guide_%2520Dealing%2520with%2520missing%2520data%2520in%2520Python.ipynb)<br>

Activity_Address missing data [Coursera | Online Courses & Credentials From Top Educators. Join for Free | Coursera](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/ungradedLab/u5Md6/activity-address-missing-data/lab?path=%2Fnotebooks%2FActivity_Address%2520missing%2520data.ipynb)<br>

Exemplar_Address missing data [Coursera | Online Courses & Credentials From Top Educators. Join for Free | Coursera](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/ungradedLab/PLNHD/exemplar-address-missing-data/lab?path=%2Fnotebooks%2FExemplar_Address%2520missing%2520data.ipynb) <br>

Account for outliers <br>

Outliers: Observations that are an abnormal distance from other values or an overall pattern in a data population.

3 Types of outliers:
* Global outliers: Values that are completely different form the overall data group and have no association with any other outliers
* Contextual outliers: Normal data points under certain conditions but become anomalies under most other conditions.
* Collective outliers: A group of abnormal points that follow similar patterns and are isolated from the rest of the population

Documentation string or Docstring: A line of text following a method or function that is used to others, using your code, what this method or function does. A doctoring represents good documentation practice in Python. <br>

```
def fun():
    """ Docstring """
```

How to handle outliers:
* Delete them: If you are sure the outliers are mistakes, typos, or errors
* Reassign them: If the dataset is small, you can choose a path of deriving new values to replace the outlier values
* Leave them: For a dataset that you plan to do EDA/analysis on and nothing else, or for a dataset you are preparing for a model hat is resistant to outliers, it is most likely that you are going to leave them in.
[Coursera | Online Courses & Credentials From Top Educators. Join for Free | Coursera](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/supplement/vmpy6/reference-guide-how-to-handle-outliers) <br>

Label encoding is a data transformation technique where each category is assigned a unique number instead of a qualitative value [series.cat.codes]<br>

Dummy variables: Variables with values of 0 or 1, which indicate the presence or absence of something [pd.get_dummies()] . This creation of dummies is called one-hot encoding<br>

* Label encoding is best for large numbers of different categorical variables and for categories that have an inherent order to them. 
* One-hot encoding is best for smaller amounts of categorical variables and for categories that have no order. 

*Heatmap*: A typeof data Visualization that depicts the magnitude of an instance or set of values based on two colours <br>

  

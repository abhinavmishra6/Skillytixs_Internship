# Exploratory Data Analysis on Titanic Dataset

## Project Overview
This project performs Exploratory Data Analysis (EDA) on the Titanic dataset from Kaggle.  
The goal is to uncover key insights about survival patterns among passengers using visual and statistical techniques.

## Steps Performed
- Data inspection using `info()`,  `describe()`,  `isnull().sum()`
- Handling missing values
- Univariate analysis (Age, Fare, SibSp, Parch, etc.)
- Bivariate analysis: Survival vs Sex, Pclass, Embarked
- Pairplot analysis on key variables
- Skewness detection and log-transformation for:
  - Fare
  - SibSp
  - Parch
  - Age
- Correlation heatmap
- Business insights and summary

## 📊 Key Insights
- Females had a significantly higher survival rate than males.
- 1st class passengers survived more often than 2nd and 3rd class.
- Higher ticket fare showed a positive association with survival.S
- Fare and SibSp were strongly right-skewed and improved after log-transformation.

## Repository Contents
| File                  | Description                          |
| --------------------- | ------------------------------------ |
| `Task2.ipynb`         | Jupyter Notebook containing full EDA |
| `Task2.pdf`           | PDF version of analysis              |
| `README.md`           | Project documentation                |
| `Titanic_Dataset.csv` | Dataset used                         |

## Tools & Libraries
- Python, Pandas, NumPy
- Matplotlib, Seaborn
- Jupyter Notebook
- MiKTeX + nbconvert (for PDF export)


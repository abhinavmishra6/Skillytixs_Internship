# **Task 1: Data Cleaning & Preprocessing**

## **Overview**

This task involved cleaning and preprocessing the **Customer Personality Analysis** dataset from Kaggle to make it ready for analysis. The dataset contained missing values, inconsistent text formats, date formatting issues, and unnecessary duplicates. All cleaning was performed using **Python (Pandas)**.

------

## **Steps Performed**

### **1. Loaded the Dataset**

- The dataset was loaded using `pd.read_csv()` with `sep="\t"` because it was tab-separated.

### **2. Handled Missing Values**

- Checked missing values using `.isnull().sum()`.
- Removed rows that were completely empty.
- Filled missing numerical values with the **mean**.
- Filled missing categorical values with the **mode**.

### **3. Removed Duplicate Rows**

- Used `drop_duplicates()` to ensure the dataset contained unique records.

### **4. Standardized Text Columns**

- Converted text columns such as **Education** and **Marital_Status** to lowercase and stripped extra spaces.

### **5. Converted Date Format**

- Converted the `Dt_Customer` column into a standard datetime format.
- Reformatted dates to **dd-mm-yyyy**.

### **6. Cleaned Column Names**

- Converted column names to lowercase.
- Replaced spaces and hyphens with underscores for consistency.

### **7. Fixed Data Types**

- Ensured numeric columns (like `income`) were converted to correct data types (`float`).

### **8. Exported Cleaned Dataset**

- Saved the cleaned dataset as
   **`cleaned_marketing_campaign.csv`**
   using `sep="\t"` (tab-separated).

------

## **Files Included**

- **task1.py** (Python script for data cleaning)
- **marketing_campaign.csv** (raw dataset)
- **cleaned_marketing_campaign.csv** (cleaned dataset)
- **README.md**
- **Output Screenshot of python Script**

------

## **Outcome**

The final cleaned dataset is now:

- Free of missing values
- Duplicates removed
- Properly formatted
- Consistent in text, dates, and column names

- Ready for further analysis or modeling



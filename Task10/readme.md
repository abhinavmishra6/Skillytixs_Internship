# Scrape and Analyze Job Listings for Data Analyst Roles (Internshala)

## **Task Overview**

This task focuses on **scraping Data Analyst / Data Analysis internships** from Internshala using `requests` and `BeautifulSoup`.
The cleaned dataset is then analyzed to extract key insights such as **top locations**, **most in-demand skills**, and **overall job availability**.

The goal of this task is to:

- Practice **real-world web scraping**
- Understand **HTML parsing** using BeautifulSoup
- Apply **data cleaning** using Pandas
- Perform **basic exploratory analysis**
- Use **visualizations** for insights
- Follow **ethical scraping practices**

---

# **Steps Performed**

## **1. Web Scraping**

- Sent HTTP GET requests to **3 Internshala pages**
- Used BeautifulSoup to parse:
  - Internship Title
  - Company Name
  - Location
  - Salary/Stipend
  - Skill Requirements
- Extracted job cards using class-based selectors
- Added `time.sleep(2)` between requests to avoid rate limiting
- Followed Internshala’s `robots.txt` and ethical scraping rules
- Removed dummy/hidden internship cards

---

## **2. Data Cleaning**

Performed cleaning inside Pandas:

- Converted raw job dictionaries into a DataFrame
- Standardized missing values (title, company, location)
- Cleaned salary strings → `salary_clean`
- Extracted skills into a list:
  - Split by ","
  - Removed whitespace
  - Removed duplicates while preserving order
- Removed exact duplicate job entries
- Final cleaned DataFrame contains:
  - `title`
  - `company`
  - `location`
  - `salary`
  - `salary_clean`
  - `skills_raw`
  - `skills_list`

---

## **3. Basic Analysis**

Performed on cleaned dataset:

### **✔ Total Jobs Scraped**

**126 internships** scraped across 3 pages.

### **✔ Top 5 Locations**

| Location        | Count |
| --------------- | ----- |
| Work from home  | 63    |
| Bangalore       | 7     |
| Delhi           | 6     |
| Mumbai          | 6     |
| Pune (Balewadi) | 6     |

### **✔ Top 10 Most In-Demand Skills**

| Skill                         | Frequency |
| ----------------------------- | --------- |
| Data Analysis                 | 75        |
| MS-Excel                      | 42        |
| Effective Communication       | 32        |
| English Proficiency (Spoken)  | 28        |
| Business Analysis             | 27        |
| Social Media Marketing        | 25        |
| Time Management               | 23        |
| Digital Marketing             | 21        |
| Market Research               | 21        |
| English Proficiency (Written) | 21        |

---

# Key Insights

- **Work From Home** dominates internship availability with 50%+ share.
- **Data Analysis**, **MS-Excel**, and **SQL/Python** appear consistently across listings.
- Strong emphasis on **communication skills**, especially for cross-functional roles.
- Many internship listings show **Data Analysis + Social Media/Marketing**, showing companies prefer **multi-skilled interns**.
- Stipends vary widely, commonly ranging from **₹5,000–20,000 / month**.

---

# Challenges Faced During Scraping

- Internshala uses **multiple CSS classes** with extra spaces required flexible class matching.
- Some job cards are **hidden/dummy** (tracking elements)  had to skip them.
- Skills often include **dozens of entries** due to “+more” expansion required deduplication and cleaning.
- Variation in salary formats (lump sum / month) made standardization necessary.
- Website HTML structure is nested → required careful inspection via browser developers tools.

---

# **Repository Contents**

| File                                  | Description                                                     |
| ------------------------------------- | --------------------------------------------------------------- |
| `Task10.ipynb`                      | Jupyter Notebook with full scraping, cleaning, analysis & plots |
| `internshala_data_analyst_jobs.csv` | Cleaned dataset                                                 |
| `readme.md`                         | readme file                                                     |

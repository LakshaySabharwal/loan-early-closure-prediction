# loan-early-closure-prediction
🎯 Project: Predicting Early Loan Closures in Financial Services Using Machine Learning

📌 Problem Statement
Early loan closures present a major challenge for stakeholders across the financial ecosystem, including Non-Banking Financial Companies (NBFCs), banks, fintechs, and consulting firms such as the Big 4. When borrowers repay loans ahead of schedule, it disrupts expected interest income streams and affects cash flow forecasting. This unpredictability can cause:

Revenue loss due to reduced interest collection.

Inefficiencies in fund allocation and reinvestment.

Misalignment in credit risk profiling and stress testing.

Challenges in strategic planning and profitability.

Understanding and predicting borrower behavior related to early loan closure is critical for optimizing loan portfolio performance, managing risk exposure, and designing customer retention strategies such as refinancing offers or prepayment penalties.

✅ Solution Overview
To tackle this issue, we built a supervised machine learning model that predicts the probability of a loan being closed early using historical data and borrower behavior patterns.

Our model uses a Random Forest Classifier — a powerful and interpretable ensemble model — to identify early loan closures based on key loan features. This enables financial institutions and consultants to proactively manage their portfolios and reduce risks associated with early repayments.

🔍 Key Features Used
Each feature was carefully selected for its potential correlation with early repayment behavior:

Loan Type (e.g., Home Loan, LAP)
Indicates purpose and nature of the loan, which affects repayment tendency.

Loan Disbursal Date & Loan Closure Date
Used to calculate loan tenure and Months on Book (MOB), helping determine how early a closure happened.

Interest Rate
High interest rates may drive borrowers to refinance or close early to reduce interest burden.

Loan-to-Value (LTV) Ratio
Reflects the equity portion. A higher LTV may suggest higher risk or refinancing behavior.

Credit Score at Origination
Higher credit score borrowers often exhibit early repayment due to better financial discipline.

Branch State (Geographical)
Captures regional trends, economic differences, and behavioral variations.

Closure Reason
Helps the model learn from past closure motives (e.g., early_closure vs. regular_closure).

🧠 Model Architecture & Workflow
Step 1: Data Preprocessing

Load dataset (CSV/Excel).

Convert loan disbursal and closure dates to datetime.

Create new features:

MOB = (closure date - disbursal date) in months

Tenure = total number of days the loan was active

Create binary label column (1 if early_closure, else 0)

Step 2: Feature Engineering

Select features like loan_type, branch_state, interest_rate, credit_score, ltv_ratio, mob_at_closure, and tenure.

Apply one-hot encoding for categorical variables.

Step 3: Train-Test Split

Split the data into 80% training and 20% test set.

Step 4: Model Building

Train a Random Forest Classifier using the training data.

Step 5: Model Evaluation

Predict on test data.

Evaluate using accuracy, precision, recall, and F1-score.

📈 Results & Insights
The model performs well with a good balance of accuracy and recall.

Important predictors: interest rate, loan tenure, and credit score.

Business teams can use these insights to design proactive strategies like prepayment penalties, retention offers, or refinancing options.

🚀 Future Enhancements
Add behavioral features like EMI bounces or overdue records.

Try advanced models like XGBoost or LightGBM.

Deploy as a Streamlit/Flask app for interactive use.

Use SHAP values to explain individual model predictions.

💻 How to Run the Code
Install required libraries:

bash
Copy
Edit
pip install pandas scikit-learn
Run the Python script:

bash
Copy
Edit
python risk_trigger.py
Make sure the dataset (loan_data.xlsx or .csv) is placed in the same directory as the script.

📂 Files in This Project
risk_trigger.py - Main Python script with model code

loan_data.xlsx - Dataset used for training and evaluation

README.md - Documentation and project details

🤝 Built By
Lakshay Sabharwal
Risk Data Analyst | AI-ML & Data Science Enthusiast
LinkedIn: https://www.linkedin.com/in/lakshaysabharwal

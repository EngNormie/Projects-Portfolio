# EMPLOYEE PERFORMANCE ANALYSIS for INX FUTURE Inc.

INX Future Inc , (referred as INX ) , is one of the leading data analytics and automation solutions providers with over 15 years of global business presence. INX has consistently rated as the top 20 best employers for the past 5 years. INX human resource policies are considered as employee friendly and widely perceived as best practices in the industry.

Over the recent years, the employee performance indexes are not healthy and this is becoming a growing concern among the top management. There has been increased escalations on service delivery and client satisfaction levels came down by 8 percentage points.

The CEO, Mr. Brain decided to initiate a data science project, which analyses the current employee data and finds the core underlying causes of these performance issues. Project findings are expected to help the company take the right course of actions, and provide clear indicators of non performing employees, so that any penalization of non-performing employees, if required, may not significantly affect other employee morals.

The original dataset for this analysis is from \[IABAC\](http://data.iabac.org/exam/p2/data/INX\_Future\_Inc\_Employee\_Performance\_CDS\_Project2\_Data\_V1.8.xls).

Expected insights are:

* Department wise performances,  
* Top 3 Important Factors affecting employee performance,  
* A trained model which can predict employee performance based on factors as inputs. This will be used to hire employees,  
* Recommendations to improve the employee performance based on insights from analysis.

## Solution Approach

The project solution approach follows a standard Machine Learning project methodology described below:

\* \*\*Data Preprocessing\*\*:  
    \- Clean and preprocess dataset. Handle missing values, outliers, and any inconsistencies.  
    \- Convert features to appropriate formats.  
    \- Extract relevant features.

\* \*\*Feature Engineering\*\*:  
    \- Creating new features that might impact employee performance. Steps taken are as below:  
        \- Convert categorical to numerical  
        \- Check outliers & Impute outliers  
        \- Feature transformation  
        \- Feature scaling

\* \*\*Exploratory Data Analysis (EDA)\*\*:  
    \- Visualizing data to understand patterns, correlations, and distributions.  
    \- Identifying any trends, or anomalies.

\* \*\*Model Building/Training/Testing\*\*:  
    \- Training predictive models to conduct employee performance analysis.  
    \- Some relevant models include:  
        \- \*\*Logistic Regression\*\*: Supervised machine learning algorithm used for binary or multi-class classification problems.  
        \- \*\*Random Forests\*\*: Handle non-linear relationships and feature importance.  
        \- \*\*Gradient Boosting\*\*: Ensemble method for accurate predictions.  
        \- \*\*Neural Networks\*\*: Deep learning models for complex patterns.

\* \*\*Evaluation and Validation\*\*:  
    \- Evaluating model performance using metrics like Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), or Mean Absolute Percentage Error (MAPE).

\* \*\*Implementation\*\*:  
    \- Once a reliable model is identified, it is integrated it into the employee performance management system.  
    \- The model is continuously monitored and updated as new data becomes available.

## Results and Conclusion

The project aimed to build a predictive model to enable INX Future Inc. to predict employee performance rating. A datset for employee performance was provided. Feature engineering was conducted in order to come up with insightful features that impact performance rating. The following seven models were evaluated:

\* Logistic Regression

\* Decision Tree

\* Random Forest

\* Support Vector Machine

\* Artificial Neural Network (ANN \- MLP)

\* K-Nearest Neighbors (KNN)

\* Naive Bayes

\*\*Artificial Neural Network (ANN \- MLP)\*\* proved to be the best model based on training and testing accuracy scores \- \*\*98.07% and 96.80%\*\* respectively.

It is concluded that the company should provide a better environment as it significantly increases employee performance rating. The company should also often increase the salary of employee, as well as offer them promotion. This helps them maintain a worklife balance leading to better performance rating.  

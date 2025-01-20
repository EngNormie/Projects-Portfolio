# INVENTORY FORECASTING FOR SPARE PARTS

Keeping Inventory of spare in various service centre to the market demand is always a challenge as most service centres spend significantly in spare parts inventory costs. In spite of this, availability of spare parts has been one of the problem areas.

Just-in-time (JIT) is an inventory management method in which you keep as little inventory on hand as possible. That means you don’t stockpile products just in case you need them — you simply reorder products to replace those you’ve already sold.

The goal of a JIT system is to receive new products just as they’re needed — any sooner and you’ll have excess inventory levels, and you’ll encounter stockouts if shipments come too late. When implemented correctly, a JIT inventory system can help retailers.

The JIT inventory method helps businesses keep enough inventory on hand to fulfill customer orders, while also keeping inventory levels as low as possible. This allows you to enjoy significant cost savings on inventory storage (since you have fewer items to store), but it has a couple of other financial benefits.

## Project Goal(s)
The main goal is to create a predictive model for inventory forecasting so that the service centre achieve JIT standards.

 * Task 1: - Create Predictive model for inventory forecasting so that a service centre achieves JIT standards.

 * Task 2: - Prepare a complete data analysis report on the given data.

 * Task 3: - Identify the factors that affect demand.

 * Task 3: - Create a report stating the performance of multiple models on this data and suggest the best model for production.

## Data Source
Dataset: Confidential

Port No 18.136.157.135
DB Name: project_service_data
Data Description

● abc.csv

The main file which contains parts inventory data, exported using SQL

The dataset includes the following features, which are crucial for analysis and forecasting:

- `invoice_date`
- `job_card_date`
- `business_partner_name`
- `vehicle_no`
- `vehicle_model`
- `current_km_reading`
- `invoice_line_text`

## Project Solution Approach
The project solution approach follows a standard Machine Learning project methodology described below:

### Data Preprocessing:

 * Clean and preprocess dataset. Handle missing values, outliers, and any inconsistencies.
 
 * Convert date columns to appropriate datetime formats.

 * Extract relevant features from the invoice_line_text (e.g., product categories, keywords).

### Feature Engineering:

#### Creating new features that might impact demand or inventory levels. For example:
 * Day of the week (weekday vs. weekend).

 * Seasonality (month, quarter).

 * Historical demand trends.

 * Promotions or special events.


### Exploratory Data Analysis (EDA):

 * Visualizing data to understand patterns, correlations, and distributions.

 * Identifying any seasonality, trends, or anomalies.


### Model Building/Training/Testing:

 * Training predictive models to estimate demand or inventory levels.

 * Some relevant models include:

  * **Linear Regression:** Predict inventory levels based on features.

  * **Random Forests:** Handle non-linear relationships and feature importance.

  * **Gradient Boosting:** Ensemble method for accurate predictions.

### Evaluation and Validation:

  * Evaluating model performance using metrics like Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), or Mean Absolute Percentage Error (MAPE).

### Implementation:

  * Once a reliable model is identified, it is integrated it into the inventory management system.

  * The model is continuously monitored and updated as new data becomes available.

## Findings
The following five models were evaluated:

 * Decision Tree Regressor,

 * Random Forest Regressor,

 * Bagging Regressor,

 * Gaussian Process Regressor,

 * Gradient Boosting Regressor,

 * CatBoost Regressor,

 * LightGBM Regressor

RandomForestRegressor proved to be the best model based on cross-validation score. The Training Score for Random Forest Regressor was **91.8%**, hence it is recommended for integration into the business's inventory management system. This would help the automotive spare parts business to achieve endeavors for JIT inventory management and curtail losses.

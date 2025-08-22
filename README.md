# Insurance-Cost-Prediction
A predictive modeling project that estimates insurance premium costs based on health and demographic factors (age, BMI, chronic diseases, surgeries, etc.). Includes data preprocessing, model training, evaluation, and an interactive Streamlit app for real-time predictions.

# Target Metric

*Regression Problem → Target variable = Premium Amount

*Evaluation Metrics:
 * R² Score → To measure how well the model explains variance.
 * RMSE (Root Mean Squared Error) → To measure prediction error.

# Steps Taken

1. Exploratory Data Analysis (EDA)

    * Checked for missing values and outliers.

    * Visualized relationships between Age vs Premium and BMI vs Premium.

    * Observed that premium increases with age → strong positive correlation.

2. Hypothesis Testing

   * Conducted hypothesis test to check correlation between Age and Premium.

   * Result: p-value < 0.05, hence Age significantly impacts Premium.

3. Feature Engineering

   * Created categorical features like BMI category.

   * Applied Label Encoding for categorical variables.

4. Model Building

   * Tried multiple regression algorithms:

   * Linear Regression

   * Random Forest Regressor

   * Random Forest performed better with higher R² and lower RMSE.

5. Model Deployment

   * Built a Streamlit web app to allow users to input values and get predicted insurance cost.

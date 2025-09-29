import pandas as pd
import pickle
import plotly.express as px
import plotly.graph_objects as go

# -------------------------------
# Load LightGBM model
# -------------------------------
with open("lgbm_model.pkl", "rb") as f:
    model_lgbm = pickle.load(f)

# -------------------------------
# Features required by the model
# -------------------------------
model_features_order = [
    'area', 'population', 'rainfall_1d', 'temperature', 'true_cases',
    'contamination_avg', 'event_cases', 'rainfall_7d_sum', 'temp_7d_avg',
    'cases_7d_sum', 'reported_cases', 'spillover_cases', 'exposure_score',
    'syndromic_score', 'spatial_score', 'vulnerability_score', 'temp_score',
    'asha_symptoms_diarrhea', 'asha_symptoms_vomiting',
    'asha_households_affected', 'asha_visits_performed',
    'clinic_visits_diarrhea', 'clinic_admissions', 'clinic_tests_conducted',
    'clinic_ors_dispensed', 'water_ph_avg', 'water_turbidity_avg',
    'water_sources_red_pct', 'water_contamination_sources', 'month',
    'week_of_year', 'day_of_week', 'rainfall_7d_sum_lag_7',
    'rainfall_7d_sum_lag_14', 'rainfall_7d_sum_roll_mean_14',
    'rainfall_7d_sum_roll_std_14', 'contamination_avg_lag_7',
    'contamination_avg_lag_14', 'contamination_avg_roll_mean_14',
    'contamination_avg_roll_std_14', 'water_turbidity_avg_lag_7',
    'water_turbidity_avg_lag_14', 'water_turbidity_avg_roll_mean_14',
    'water_turbidity_avg_roll_std_14', 'exposure_score_lag_7',
    'exposure_score_lag_14', 'exposure_score_roll_mean_14',
    'exposure_score_roll_std_14', 'true_cases_lag_7', 'true_cases_lag_14',
    'true_cases_roll_mean_14', 'true_cases_roll_std_14',
    'temperature_lag_7', 'temperature_lag_14', 'temperature_roll_mean_14',
    'temperature_roll_std_14'
]

# -------------------------------
# Load + Feature Engineering
# -------------------------------
data = pd.read_excel("Village B.xls")
data['date'] = pd.to_datetime(data['date'])

def add_features(df):
    df = df.sort_values("date").copy()

    df['month'] = df['date'].dt.month
    df['week_of_year'] = df['date'].dt.isocalendar().week.astype(int)
    df['day_of_week'] = df['date'].dt.dayofweek

    lag_vars = ['rainfall_7d_sum', 'contamination_avg',
                'water_turbidity_avg', 'exposure_score',
                'true_cases', 'temperature']

    for var in lag_vars:
        df[f'{var}_lag_7'] = df[var].shift(7)
        df[f'{var}_lag_14'] = df[var].shift(14)
        df[f'{var}_roll_mean_14'] = df[var].rolling(window=14).mean()
        df[f'{var}_roll_std_14'] = df[var].rolling(window=14).std()

    return df

data_fe = add_features(data)

# -------------------------------
# Prediction function
# -------------------------------
def predict_outbreak(date_input: str):
    date_input = pd.to_datetime(date_input)
    row = data_fe[data_fe['date'] == date_input]

    if row.empty:
        return {"error": f"No data found for {date_input.date()}"}

    df_input = row[model_features_order].copy()
    df_input['area'] = df_input['area'].astype('category')

    prediction = float(model_lgbm.predict(df_input)[0])

    # last 7 days for metrics
    last_7d = data_fe[(data_fe['date'] <= date_input) &
                      (data_fe['date'] > date_input - pd.Timedelta(days=7))]

    metrics = {
        "population": int(row['population'].values[0]),
        "water_ph": round(row['water_ph_avg'].values[0], 2),
        "turbidity": round(row['water_turbidity_avg'].values[0], 2),
        "reported_cases_7d": int(last_7d['reported_cases'].sum()),
        "true_cases_7d": int(last_7d['true_cases'].sum())
    }

    return {"prediction": prediction, "metrics": metrics}

from to_datetime import to_datetime
import pandas as pd


def get_working_time(in_time_data, out_time_data):
    out_time_df = (
        out_time_data.copy()
        .drop("EMPLOYEE_ID", axis=1)
        .applymap(lambda x: to_datetime(x))
    )
    out_time_df
    in_time_df = (
        in_time_data.copy()
        .drop("EMPLOYEE_ID", axis=1)
        .applymap(lambda x: to_datetime(x))
    )
    in_time_df
    daily_hours_df = pd.DataFrame(out_time_df - in_time_df)
    return daily_hours_df

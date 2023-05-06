import pandas as pd


def ft_rename(df, sensors, m="101"):
    sensor_fts = sensors.iloc[:, 1].dropna()
    sensor_fts[4:16] = sensor_fts[4:16] + "(°C)"
    cols = [m + "-" + str(i) for i in range(1, 34)]
    new_cols = [df.columns[0]] + cols[:20] + cols[21:26]
    df = df[new_cols]
    rename_dict = {str(num): col for num, col in zip(cols, sensor_fts.tolist())}
    df = df.rename(columns=rename_dict)
    return df


df_101 = pd.read_csv("static/dist/pd/MTP101.csv")
df_102 = pd.read_csv("static/dist/pd/MTP102.csv")
sensor_df = pd.read_csv("static/dist/pd/BeycelikPres_DataList.csv")

df_101 = ft_rename(df_101, sensor_df, m="101")
df_102 = ft_rename(df_102, sensor_df, m="102")

df_101.to_csv("static/dist/pd/MTP101.csv", index=False)
df_102.to_csv("static/dist/pd/MTP102.csv", index=False)


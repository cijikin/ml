import pandas as pd
import numpy as np


def set_display_options():
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 200)


conversion_df = pd.read_csv("data/ad_conversion.csv")
set_display_options()

conversion_df["last name"].fillna("", inplace=True)  # заполняет N/A, NaN, None etc. поля переданным значением в кав.

conversion_df.at[8, "gender"] = "F"  # меняет значение конкретной ячейки
conversion_df.at[14, "gender"] = "M"
conversion_df.at[29, "gender"] = "F"
conversion_df.at[37, "gender"] = "M"

for z in range(len(conversion_df)):
    if conversion_df.at[z, "seen count"] > 10:
        conversion_df.at[z, "seen count"] = 0

# print(conversion_df.dtypes)

conversion_df.insert(conversion_df.columns.get_loc("gender"), "full name", None)
conversion_df.insert(conversion_df.columns.get_loc("color scheme"), "birth date", None)
conversion_df.insert(conversion_df.columns.get_loc("color scheme"), "age", None)

for z in range(len(conversion_df)):
    conversion_df.at[z, "full name"] = (
                conversion_df.at[z, "first name"] + ' ' + conversion_df.at[z, "last name"]).strip()


def age_to_range(age):
    if 6 <= age < 18:
        return "6-18"
    elif 18 <= age < 35:
        return "18-35"
    elif 35 <= age < 99:
        return "35-99"
    else:
        return "unknown"


for z in range(len(conversion_df)):
    conversion_df.at[z, "birth date"] = pd.Timestamp(day=conversion_df.at[z, "day of birth"],
                                                     month=conversion_df.at[z, "month of birth"],
                                                     year=conversion_df.at[z, "year of birth"]).date()
    conversion_df.at[z, "age"] = (pd.Timestamp("01-01-2019") - pd.Timestamp(
        conversion_df.at[z, "birth date"])).days // 365


def convert_text_to_binary(text):
    if text == "y":
        return 1
    elif text == "n":
        return 0
    else:
        return None


for z in range(len(conversion_df)):
    conversion_df.at[z, "followed ad"] = convert_text_to_binary(conversion_df.at[z, "followed ad"])
    conversion_df.at[z, "made purchase"] = convert_text_to_binary(conversion_df.at[z, "made purchase"])


def rate_conversion(rating):
    rates_mapping = {np.NaN: 1, "bad": 2, "ok": 3, "good": 4, "excellent": 5}
    if rating in rates_mapping:
        return rates_mapping[rating]
    else:
        return None


def color_scheme_conversion(cs):
    cs_mapping = {"red": 1, "green": 2, "blue": 3}
    if cs in cs_mapping:
        return cs_mapping[cs]
    else:
        return None


for z in range(len(conversion_df)):
    conversion_df.at[z, "user rating"] = rate_conversion(conversion_df.at[z, "user rating"])
    conversion_df.at[z, "age"] = age_to_range(conversion_df.at[z, "age"])
    # conversion_df.at[z, "color scheme"] = color_scheme_conversion(conversion_df.at[z, "color scheme"])

conversion_df.rename(columns={'age': 'gen'}, inplace=True)

conversion_df.drop(columns=["first name", "last name"], inplace=True)
conversion_df.drop(columns=["birth date"], inplace=True)
conversion_df.drop(columns=["month of birth", "day of birth", "year of birth"], inplace=True)

conversion_df.insert(conversion_df.columns.get_loc("made purchase"), "ad effectiveness", None)

for z in range(len(conversion_df)):
    if conversion_df.at[z, "seen count"] == 0:
        conversion_df.at[z, "ad effectiveness"] = -1
    else:
        conversion_df.at[z, "ad effectiveness"] = str(round(((conversion_df.at[z, "followed ad"] + conversion_df.at[
            z, "made purchase"]) * 50 / conversion_df.at[z, "seen count"]), ndigits=2)) + "%"

conversion_df = conversion_df.astype({"followed ad": "int64", "made purchase": "int64", "user rating": "int64"})

colors_grouped = (conversion_df[["color scheme", "followed ad", "made purchase"]]).groupby("color scheme").mean()

print(colors_grouped)
print("Из таблицы видно, что реклама, в которой"
      "\nпреобладают красніе цвета, всегда остаётся"
      "\n'кликнутой' и больше привлекает внимание,"
      "\nв то время, как та,. где преобладают зелёные -"
      "\nпровоцирует людей на произведение покупки."
      "\nРеклама же с голубыми цветами в основном"
      "\nне продкутивна, и имеет меньший результат.")
print(conversion_df)
print(conversion_df.dtypes)

conversion_df.to_csv("data/prepared_ad_conversion.csv")

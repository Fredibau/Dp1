import urllib.request
all_data = "" for i in range(2023,2024): url = “https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=” + str(i)
with urllib.request.urlopen(url) as f:
    year_data = f.read().decode("utf-8")
    if i > 2013 : year_data = year_data[665:]
    if i < 2023 : year_data = year_data[:len(year_data)-7]
    
    all_data += year_data

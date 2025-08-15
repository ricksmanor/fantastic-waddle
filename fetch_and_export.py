import pandas as pd
import requests

# Live JSON API URL
url = "https://api.outscraper.cloud/requests/NWE2MjFmODgyZjgxNGU0OWFhOTk0NDE3NzQwMThkZTQsMjAyNTA4MTUxMDA3MTZzM2Y"

# Fetch the live data
response = requests.get(url)
data = response.json()

# Convert "data" key to DataFrame
df = pd.DataFrame(data["data"])

# Save to Excel
df.to_excel("data.xlsx", index=False)

print("Excel updated successfully!")

# Visualize time-series data and customize axis labels and date formats.

#INPUT
# TimeSeriesPlot.py
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

# Sample time-series data
dates = pd.date_range(start='2025-01-01', periods=10, freq='D')  # 10 days starting Jan 1, 2025
values = [100, 120, 115, 130, 125, 140, 135, 150, 145, 160]

# Create a DataFrame
df = pd.DataFrame({'Date': dates, 'Value': values})

# Plot time-series data
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Value'], marker='o', linestyle='-', color='b')

# Customize title and labels
plt.title('Time-Series Data Example', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Value', fontsize=12)

# Customize x-axis date format
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b-%Y'))  # e.g., 01-Jan-2025
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))      # show every day

plt.xticks(rotation=45)  # rotate x-axis labels for better readability
plt.grid(True)
plt.tight_layout()
plt.show()

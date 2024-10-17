import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample dataframe
data = {
    'Date': pd.to_datetime(['2023-01-01', 
                            '2023-01-05', 
                            '2023-01-10', 
                            '2023-01-11', 
                            '2023-01-13',  
                            '2023-01-15',  
                            '2023-01-16',  
                            '2023-01-20',  
                            '2023-01-21' ]),
    'Value': [10, 20, 15, 30, 35, 20, 17, 19, 32]
}
df = pd.DataFrame(data)

# Create an empty list to store the interpolated data
interpolated_data = []

# Loop through each pair of consecutive rows
for i in range(len(df) - 1):
    start_date = df['Date'].iloc[i]
    end_date = df['Date'].iloc[i + 1]
    start_value = df['Value'].iloc[i]
    end_value = df['Value'].iloc[i + 1]
    
    # Generate 100 equally spaced points between the two dates
    date_range = pd.date_range(start_date, end_date, periods=52)[1:-1]  # Exclude start and end dates
    # Interpolate values
    value_range = np.linspace(start_value, end_value, 52)[1:-1]  # Exclude start and end values
    
    # Add jitter: small random noise
    jitter = np.random.normal(0, 0.1, len(value_range))  # Mean = 0, Std = 0.5 (adjust as needed)
    value_range_jittered = value_range + jitter
    
    # Combine dates and jittered values into a dataframe
    interpolated_segment = pd.DataFrame({'Date': date_range, 'Value': value_range_jittered})
    interpolated_data.append(interpolated_segment)

# Combine all interpolated segments into a single dataframe
interpolated_df = pd.concat(interpolated_data, ignore_index=True)

# Include original dates and values
final_df = pd.concat([df, interpolated_df]).sort_values(by='Date').reset_index(drop=True)

# Plot the original and interpolated data
plt.figure(figsize=(12, 6))
plt.plot(final_df['Date'], final_df['Value'], label='Interpolated with Jitter', alpha=0.7)
plt.scatter(df['Date'], df['Value'], color='red', label='Original Data', zorder=5)
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Interpolated Data with Jitter')
plt.legend()
plt.grid(True)
plt.show()

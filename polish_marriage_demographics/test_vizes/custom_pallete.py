import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Example DataFrame
df = pd.DataFrame({
    'Year': [2020, 2020, 2020, 2020, 2020, 
             2021, 2021, 2021, 2021, 2021, 
             2022, 2022, 2022, 2022, 2022],
    'Detailed Life Stage': ['20-29', '30-39', '40-49', '50-59', '60-69',
                            '20-29', '30-39', '40-49', '50-59', '60-69',
                            '20-29', '30-39', '40-49', '50-59', '60-69'],
    'Values': [15.3, 20.4, 10.5, 18.5, 13.0,
               16.5, 21.6, 11.0, 19.0, 14.2,
               17.8, 23.0, 12.3, 20.5, 15.3]
})

# Define a custom color palette with highlights and subdued colors
custom_palette = {
    '20-29': '#FF5733',  # Highlight 1
    '30-39': '#3498DB',  # Highlight 2
    '40-49': '#A9A9A9',  # Subdued 1
    '50-59': '#A3B18A',  # Subdued 2
    '60-69': '#C39BD3'   # Subdued 3
}

# Create the Seaborn line plot with hue and custom palette
plt.figure(figsize=(10, 6))
sns.lineplot(
    data=df,
    x='Year',
    y='Values',
    hue='Detailed Life Stage',
    palette=custom_palette,
    marker='o'
)

# Set labels and title
plt.xlabel('Year')
plt.ylabel('Values')
plt.title('Line Plot with Highlighted and Subdued Colors for Age Groups')

# Show the plot
plt.show()

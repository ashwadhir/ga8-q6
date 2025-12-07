import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 1. Data Generation
# Creating realistic synthetic data for product performance insights
data = {
    'Product Category': ['Electronics', 'Home Decor', 'Clothing', 'Beauty', 'Sports'],
    'Satisfaction Score': [4.2, 3.8, 4.5, 4.1, 3.9]
}
df = pd.DataFrame(data)

# 2. Set Figure Size for Exact Dimensions
# 8 inches * 64 dpi = 512 pixels
plt.figure(figsize=(8, 8))

# 3. Professional Styling
sns.set_style("whitegrid")
sns.set_context("talk") # Increases font size for presentations

# 4. Create Barplot
# Using a professional color palette
plot = sns.barplot(
    x='Product Category', 
    y='Satisfaction Score', 
    data=df, 
    palette='viridis'
)

# 5. Add Titles and Labels
plt.title('Customer Satisfaction by Product Category', pad=20, fontsize=16)
plt.xlabel('Category', labelpad=10)
plt.ylabel('Average Score (1-5)', labelpad=10)
plt.ylim(0, 5) # Setting fixed limit for clarity

# 6. Save Chart
# We use dpi=64 to ensure 8x64 = 512 pixels. 
# We intentionally omit bbox_inches='tight' to maintain exact 512x512 dimensions.
plt.savefig('chart.png', dpi=64)

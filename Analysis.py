import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Import data
df = pd.read_csv('Airline_review.csv')

# Melt data frame for barplot visualisation
df_melt = pd.melt(df, id_vars=['Airline'], value_vars=['Postive reviews', 'Neutral reviews', 'Negative reviews'],
        var_name='Sentiment', value_name='Count')

# Print result
print(df.head(20))

# Barplot function for centiment count
def barplot():
	ax = sns.barplot(x='Airline', y='Count', hue='Sentiment', data=df_melt, palette='YlOrRd')
	ax.set_title('Sentiment Count')
	plt.savefig('Sentiment_Count.png')
	plt.show()

# Barplot function for positive/negative sentiment ratio
def ratio():
	ax = sns.barplot(x='Airline', y='Pos/Neg ratio', data=df)
	ax.set_title('Positive/Negative Sentiment Ratio')
	plt.savefig('PositiveNegative_Sentiment_Ratio.png')
	plt.show()

# Call desired function
ratio()
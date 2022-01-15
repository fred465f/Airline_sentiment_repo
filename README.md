# Airline sentiment analysis

In this project i analysed data regarded Twitter reviews of US Airlines, and used the python libraries:

 - sqlite3
 - seaborn
 - pandas
 - csv

The python library sqlite3 was used to write sqlite commands to query the database, 'database.sqlite', downloaded from kaggle, 
https://www.kaggle.com/crowdflower/twitter-airline-sentiment, and originaly collected at Crowdflower's Data for Everyone library. 
Pandas was used to import the tables - that were created by the queries and uploaded with the csv library. 

The number of positive, neutral and negative number of reviews, grouped by each arline were calculated and visualised with seaborn:

![](/Sentiment_Count.png)

The positive/negative sentiment ratio grouped by each arline were calculated and visualised with seaborn:

![](/PositiveNegative_Sentiment_Ratio.png)

The Functions.py file, contains helper functions for quering data, and uploading the resulting tables to csv files. The Query.py executes the query with the help og the Functions.py module, and saves the resulting table to csv file. Lastly the Analysis.py, makes the visualisations shown above.

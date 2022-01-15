# Impoty Functions module
import Functions as f

# Create/connect database "customer.db"
name = "database.sqlite"
columns = "airline_sentiment, airline_sentiment_confidence, negativereason, negativereason_confidence, airline, retweet_count"
where = "WHERE airline_sentiment = 'positive'"

# Query database (simple)
f.show(name, rows=15, columns=columns)

# Query database (advanced)
sql = """
	WITH positive_count AS (
    	SELECT COUNT(*) as pos_count, airline as airline_pos FROM Tweets 
		WHERE airline_sentiment = 'positive'
		GROUP BY 2
		ORDER BY 1 DESC
    ), neutral_count AS (
    	SELECT COUNT(*) as neu_count, airline as airline_neu FROM Tweets 
		WHERE airline_sentiment = 'neutral'
		GROUP BY 2
		ORDER BY 1 DESC
    ), negative_count AS (
    	SELECT COUNT(*) as neg_count, airline as airline_neg FROM Tweets 
		WHERE airline_sentiment = 'negative'
		GROUP BY 2
		ORDER BY 1 DESC
    ), avg_confidens AS (
    	SELECT AVG(airline_sentiment_confidence) as avg_conf, airline as airline_avg FROM Tweets 
		GROUP BY 2
		ORDER BY 1 DESC
    )
    SELECT pos_count, neu_count, neg_count, ROUND((CAST(pos_count AS REAL)/neg_count), 4), ROUND(avg_conf, 4), airline_neg
    FROM positive_count
    JOIN neutral_count
    	ON positive_count.airline_pos = neutral_count.airline_neu
    JOIN negative_count
    	ON positive_count.airline_pos = negative_count.airline_neg
    JOIN avg_confidens
    	ON positive_count.airline_pos = avg_confidens.airline_avg
    ORDER BY 4 DESC;
    """
print("\n\n Pos, Neu, Neg, Pos/Neg, Avg_conf, Airline:")
print("-----------------------------------------")
data = f.query(name, sql)

# Save tables to csv files
columns = [
'Postive reviews', 
'Neutral reviews', 
'Negative reviews', 
'Pos/Neg ratio', 
'Average confidence', 
'Airline'
]
f.table_to_csv(data, columns, filename='Airline_review.csv')
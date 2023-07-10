import statistics
from collections import Counter
import psycopg2
from psycopg2 import Error
import random

# Calculate the mean color
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
mean_color = tuple(int(statistics.mean(channel)) for channel in zip(*colors))
print("Mean Color:", mean_color)

# Get the Most Worn Color
colors = ["red", "blue", "green", "red", "red", "blue"]
color_frequencies = Counter(colors)
most_worn_color = color_frequencies.most_common(1)[0][0]
print("Most Worn Color:", most_worn_color)

# Get the median color
colors = ["red", "blue", "green", "yellow"]
sorted_colors = sorted(colors)
median_color = sorted_colors[len(sorted_colors) // 2]
print("Median Color:", median_color)

# Calculate the variance
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
mean_color = tuple(int(statistics.mean(channel)) for channel in zip(*colors))
variance = sum(sum((channel - mean) ** 2 for channel, mean in zip(color, mean_color)) for color in colors) / len(colors)
print("Variance:", variance)

# Calculate the probability
colors = ["red", "blue", "green", "red", "yellow"]
red_count = colors.count("red")
probability = red_count / len(colors)
print("Probability of choosing red:", probability)


# Save the colors and their frequencies in a PostgreSQL database
colors = ["red", "blue", "green", "red", "yellow"]
try:
    connection = psycopg2.connect(
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port",
        database="your_database"
    )

    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS color_frequencies (
        color VARCHAR(255) PRIMARY KEY,
        frequency INTEGER
    )
    """
    cursor.execute(create_table_query)
    for color, frequency in Counter(colors).items():
        insert_query = "INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s)"
        cursor.execute(insert_query, (color, frequency))
    connection.commit()
    cursor.close()
    connection.close()
    print("Colors and frequencies saved in the database.")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL:", error)


# Generate a random 4-digit number of 0s and 1s
random_number = random.choices([0, 1], k=4)
base_10_number = int("".join(map(str, random_number)), 2)
print("Random 4-digit number in base 10:", base_10_number)

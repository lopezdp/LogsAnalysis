#! /usr/bin/env python3
#
# David P. Lopez
# Logs Analysis
# 8/2017
#
# Multiple versions of each query provided to determine
# best practice and most efficient query.

import psycopg2

# Define queries
# Query: What are the most popular three articles of all time?
first_title = "\n1. What are the most popular three articles of all time?\n"

# 2nd version
# No need to check status and just count hits
top_3_articles_sql_query_v_2 = (
    "SELECT articles.title, count(*) AS hits FROM articles, log " 
    "WHERE log.path LIKE concat('%', articles.slug) "
    "GROUP BY articles.title ORDER BY hits DESC LIMIT 3")

# 3rd version
# Use any() & string_to_array() to match path to slug
top_3_articles_sql_query_v_3 = (
    "SELECT articles.title, count(*) AS hits FROM articles, log " 
    "WHERE articles.slug = any(string_to_array(log.path, '/')) " 
    "GROUP BY articles.title ORDER BY hits DESC LIMIT 3")

# Query: Who are the most popular article authors of all time?
second_title = "\n2. Who are the most popular article authors of all time?\n"

# 2nd version
# Use any() & string_to_array() to match path to slug
popular_authors_query_v_2 = (
    "SELECT authors.name, count(*) AS hits FROM authors, articles, "
    "log WHERE articles.author = authors.id AND articles.slug = "
    "any(string_to_array(log.path, '/')) GROUP BY articles.author, "
    "authors.name ORDER BY hits DESC")

# Query: On which days did more than 1% of requests lead to errors
third_title = "\n3. On which days did more than 1% of requests lead to errors: \n"

# 2nd version
# Use Sub Select to find Days with errors >= 1%
errors_query_v_2 = (
    "SELECT * FROM (SELECT date(log.time), round(100.0 * sum(CASE "
    "log.status WHEN '200 OK' THEN 0 ELSE 1 END)/count(log.status), 3) "
    "AS \"ERROR PCT\" FROM log GROUP BY date(log.time) ORDER BY \"ERROR PCT\" "
    "DESC) SS WHERE \"ERROR PCT\" >= 1")

# define function to get query results
def query_news_db(query_v_2):
  # Connect directly to news db
  db = psycopg2.connect(database="news")
  cur = db.cursor()

  # Execute v2 queries
  cur.execute(query_v_2)

  # return query results
  return cur.fetchall()

  # close database
  db.close()

# define function to print query results
def print_result_from_db(title, results):
    # Print the title
    print(title)

    # loop through results and output
    # justify results to format output
    for result in results:
        print("\t" + str(result[0]).ljust(40) + str(result[1]).ljust(10) + " hits")

if __name__ == "__main__":
  # Call functions. Get data from news db
  query_1_results_v_2 = query_news_db(top_3_articles_sql_query_v_3)
  query_2_results_v_2 = query_news_db(popular_authors_query_v_2)
  query_3_results_v_2 = query_news_db(errors_query_v_2)

  # Call functions. Print results.
  print_result_from_db(first_title, query_1_results_v_2)
  print_result_from_db(second_title, query_2_results_v_2)
  print_result_from_db(third_title, query_3_results_v_2)
    
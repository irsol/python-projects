#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""Udacity's Logs Analysis Project.
"""

import psycopg2


def db_connect():

    # Connect to database
    db = psycopg2. connect("dbname=news")
    return db


def get_query(query):
    # Connect to the "news" database
    db = db_connect()

    cursor = db.cursor()
    # Run SQL command
    cursor.execute(query)

    # Store results
    answer = cursor.fetchall()

    db.close()

    return answer


def top_three_articles():
    """Return the most popular top three articles.
    """
    
    # Define query
    first_query = """
        select
            articles.title as "Title",
            count(*) as "Views"
        from articles, log
        where log.path like concat('%', articles.slug)
        group by articles.title
        order by "Views" desc
        limit 3;
    """

    # Run query
    answer1 = get_query(first_query)

    # Print results
    print("1. What are the most popular three articles of all time?")
    for i in answer1:
        print('\t"{}" - {} views'.format(i[0], i[1]))
    return answer1


def top_authors():
    # Define query
    second_query = """
        select
            authors.name as "Author",
            count(*) as "Views"
        from authors, articles, log
        where authors.id = articles.author
        and log.path like concat('%', articles.slug)
        group by authors.name
        order by "Views" desc
        limit 4;
    """

    # Run query
    answer2 = get_query(second_query)

    # Print results
    print("2. Who are the most popular article authors of all time?")
    for i in answer2:
        print('\t{} - {} views'.format(i[0], i[1]))
    return answer2


def top_day_errors():
    # Define query
    third_query = """
        select
            q1.day,
            q1.total_errors::float/q2.total_requests::float * 100 as percent
        from (
            select
                date_trunc('day', log.time) as day,
                count(*) as total_errors
            from log
            where log.status = '404 NOT FOUND'
            group by date_trunc('day', log.time)
        ) q1 join (
            select
                date_trunc('day', log.time) as day,
            count(*) as total_requests
            from log
            group by date_trunc('day', log.time)
        ) q2
        on q1.day = q2.day
        where q1.total_errors::float / q2.total_requests::float * 100 > 1;
    """

    # Run query
    answer3 = get_query(third_query)

    # Print result
    print("3. On which days did more than 1% of requests lead to errors?")
    for i in answer3:
        print('\t{:%B %d, %Y} - {:.1f}% errors'.format((i[0]), i[1]))
    return answer3


if __name__ == '__main__':

    top_three_articles()
    print("")
    top_authors()
    print("")
    top_day_errors()

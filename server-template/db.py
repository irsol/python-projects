import psycopg2


def connect(db_name, host=None, port=None):
    """ Function creates a connection to the database and returns it. This
    connection can be used as a parameter to execute_sql() function.

    Params:
    ------

    db_name : string
        Database name

    host : string
        Database host name

    port : integer
        Database port

    Returns:
    -------

    connection : psycopg2.connection
    """

    if host:
        return psycopg2.connect("dbname={}, host={}, port={}".format(
                                db_name, host, port))
    else:
        return psycopg2.connect("dbname={}".format(db_name))


def execute_sql(sql_query, connection):
    """ Takes a text string with SQL query and database connection obtained
    from connect() function, executes it and returns results

    Params:
    ------

    sql_query : string
        SQL query to execute

    connection : psycopg2.connection
        Database connection (returned by connect)
    """

    with connection.cursor() as cursor:
        cursor.execute(sql_query)

        result = cursor.fetchall()

        return result

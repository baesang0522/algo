def sql_solution():
    sql = """
    WITH Stocks AS (
                SELECT *
				  FROM (
				        SELECT 'Leetcode' stock_name, 'Buy' operation, 1 operation_day, 1000 price FROM dual UNION ALL
				        SELECT 'Corona Masks' stock_name, 'Buy' operation, 2 operation_day, 10 price FROM dual UNION ALL
				        SELECT 'Leetcode' stock_name, 'Sell' operation, 5 operation_day, 9000 price FROM dual UNION ALL
				        SELECT 'Handbags' stock_name, 'Buy' operation, 17 operation_day, 30000 price FROM dual UNION ALL
				        SELECT 'Corona Masks' stock_name, 'Sell' operation, 3 operation_day, 1010 price FROM dual UNION ALL
				        SELECT 'Corona Masks' stock_name, 'Buy' operation, 4 operation_day, 1000 price FROM dual UNION ALL
				        SELECT 'Corona Masks' stock_name, 'Sell' operation, 5 operation_day, 500 price FROM dual UNION ALL
				        SELECT 'Corona Masks' stock_name, 'Buy' operation, 6 operation_day, 1000 price FROM dual UNION ALL
				        SELECT 'Handbags' stock_name, 'Sell' operation, 29 operation_day, 7000 price FROM dual UNION ALL
				        SELECT 'Corona Masks' stock_name, 'Sell' operation, 10 operation_day, 10000 price FROM dual
				       )
                 )
    SELECT stock_name
         , sum(CASE WHEN operation='Sell' THEN price ELSE -price end) capital_gain_loss
      FROM stocks t1
     GROUP BY stock_name
    """
    return sql

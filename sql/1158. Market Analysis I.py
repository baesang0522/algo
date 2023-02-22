def sql_solution():
    sql = """
    WITH Users AS (
                SELECT *
				  FROM (
				        SELECT 1 user_id, '2018-01-01' join_date, 'Lenovo' favorite_brand FROM dual UNION ALL
				        SELECT 2 user_id, '2018-02-09' join_date, 'Samsung' favorite_brand FROM dual UNION ALL
				        SELECT 3 user_id, '2018-01-19' join_date, 'LG' favorite_brand FROM dual UNION ALL
				        SELECT 4 user_id, '2018-05-21' join_date, 'HP' favorite_brand FROM dual
				       )
                 )
        , Orders AS (
                     SELECT *
                       FROM (
                             SELECT 1 order_id, '2019-08-01' order_date, 4 item_id, 1 buyer_id, 2 seller_id FROM dual UNION ALL
                             SELECT 2 order_id, '2018-08-02' order_date, 2 item_id, 1 buyer_id, 3 seller_id FROM dual UNION ALL
                             SELECT 3 order_id, '2019-08-03' order_date, 3 item_id, 2 buyer_id, 3 seller_id FROM dual UNION ALL
                             SELECT 4 order_id, '2018-08-04' order_date, 1 item_id, 4 buyer_id, 2 seller_id FROM dual UNION ALL
                             SELECT 5 order_id, '2018-08-04' order_date, 1 item_id, 3 buyer_id, 4 seller_id FROM dual UNION ALL
                             SELECT 6 order_id, '2019-08-05' order_date, 2 item_id, 2 buyer_id, 4 seller_id FROM dual
                            )
                        )
         , Items AS (
                     SELECT *
                       FROM (
                             SELECT 1 item_id, 'Samsung' item_brand FROM dual UNION ALL
                             SELECT 2 item_id, 'Lenovo' item_brand FROM dual UNION ALL
                             SELECT 3 item_id, 'LG' item_brand FROM dual UNION ALL
                             SELECT 4 item_id, 'HP' item_brand FROM dual
                            )
                    )
    SELECT t1.user_id as buyer_id
         , to_char(join_date) as join_date
         , nvl(t2.o_c, 0) AS orders_in_2019
      FROM Users t1
      LEFT OUTER JOIN (SELECT count(*) OVER(PARTITION BY buyer_id) AS o_c, buyer_id FROM Orders WHERE order_date > to_date('2019-01-01', 'YYYY-MM-DD')) t2
        ON t1.user_id = t2.buyer_id
     GROUP BY USER_ID, join_date, o_c
     ORDER BY buyer_id
    """
    return sql

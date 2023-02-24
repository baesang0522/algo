def sql_solution():
    sql = """
    WITH Stadium AS (
                SELECT *
				  FROM (
				        SELECT 1 id, '2017-01-01' visit_date, 10 people FROM dual UNION ALL
				        SELECT 2 id, '2017-01-02' visit_date, 109 people FROM dual UNION ALL
				        SELECT 3 id, '2017-01-03' visit_date, 150 people FROM dual UNION ALL
				        SELECT 4 id, '2017-01-04' visit_date, 99 people FROM dual UNION ALL
				        SELECT 5 id, '2017-01-05' visit_date, 145 people FROM dual UNION ALL
				        SELECT 6 id, '2017-01-06' visit_date, 1455 people FROM dual UNION ALL
				        SELECT 7 id, '2017-01-07' visit_date, 199 people FROM dual UNION ALL
				        SELECT 8 id, '2017-01-09' visit_date, 188 people FROM dual
				       )
                 )
       , tmp_tb AS (
                    SELECT ID
                      FROM (
                            SELECT id
                                 , visit_date
                                 , people
                                 , CASE WHEN ((lag(people) OVER(ORDER BY id) > 100) AND  
                                              (lead(people) OVER(ORDER BY id) > 100) AND 
                                              people > 100) THEN 1
                                        ELSE 0 END AS checker
                              FROM Stadium
                           )
                     WHERE checker = 1
                   )
    SELECT t2.id id
         , to_char(t2.visit_date) visit_date
         , t2.people people
      FROM (
            SELECT t1.id
                 , t1.visit_date
                 , lag
                 , lead
              FROM (
                    SELECT id
                         , visit_date
                         , lag(id) over(ORDER BY id) lag
                         , lead(id) over(ORDER BY id) lead
                      FROM Stadium
                   ) t1
                 , tmp_tb t2
             WHERE t1.id = t2.id
           ) t1
         , Stadium t2
     WHERE t1.id = t2.id
        OR t1.lag = t2.id
        or t1.lead = t2.id
     GROUP BY t2.id, t2.visit_date, t2.people
     ORDER BY id asc
    """
    return sql

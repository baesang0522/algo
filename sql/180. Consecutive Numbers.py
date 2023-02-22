def sql_solution():
    sql = """
    WITH Logs AS (
                SELECT *
				  FROM (
				        SELECT 1 id, '1' num FROM dual UNION ALL
				        SELECT 2 id, '1' num FROM dual UNION ALL
				        SELECT 3 id, '1' num FROM dual UNION ALL
				        SELECT 4 id, '2' num FROM dual UNION ALL
				        SELECT 5 id, '1' num FROM dual UNION ALL
				        SELECT 6 id, '2' num FROM dual UNION ALL
				        SELECT 7 id, '2' num FROM dual
				       ) a
               )
    select num ConsecutiveNums 
      from (
            select id
                 , num
                 , (case when ((lead(num) over(order by id desc)) = (lag(num) over(order by id desc))) and 
                             ((lead(num) over(order by id desc)) = num) then num
                        else NULL END) as checker
              from Logs
             order by id
           )
     where checker = num
    """
    return sql

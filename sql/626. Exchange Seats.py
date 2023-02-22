def sql_solution():
    sql = """
    WITH Seat AS (
                SELECT *
				  FROM (
				        SELECT 1 'id', 'Abbot' 'student' UNION ALL
				        SELECT 2 'id', 'Doris' 'student' UNION ALL
				        SELECT 3 'id', 'Emerson' 'student' UNION ALL
				        SELECT 4 'id', 'Green' 'student' UNION ALL
				        SELECT 5 'id', 'Jeames' 'student'
				       ) a
               )
    select case when (a.id % 2 = 1 and a.id < tot_num) then a.id + 1
                when a.id % 2 = 0 then a.id - 1
                else a.id 
            end as id
         , a.student
      from (
            select *
                 , (select count(1) from Seat) as tot_num
              from Seat
           ) a
     order by id
    """
    return sql

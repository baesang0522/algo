def sql_solution():
    sql = """
    WITH tmp_tb AS (
                SELECT *
				  FROM (
				        SELECT 1 'id', NULL 'p_id' UNION ALL
				        SELECT 2 'id', 1 'p_id' UNION ALL
				        SELECT 3 'id', 1 'p_id' UNION ALL
				        SELECT 4 'id', 2 'p_id' UNION ALL
				        SELECT 5 'id', 2 'p_id'
				       )
               )
    select a.id, a.type
      from (
            select id
                 , case when a.p_id is NULL then 'root'
                        when a.t is NULL then 'leaf'
                        else 'inner'
                    end as type
              from (
                    SELECT a.id as id
                         , a.p_id as p_id
                         , b.id as t
                      FROM tmp_tb as a
                      left outer join tmp_tb as b on a.id = b.p_id
                   ) a
           ) a
     group by a.id, a.type
    """
    return sql

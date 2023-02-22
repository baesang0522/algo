def sql_solution():
    sql = """
    WITH Scores AS (
                SELECT *
				  FROM (
				        SELECT 1 'id', 3.50 'score' UNION ALL
				        SELECT 2 'id', 3.65 'score' UNION ALL
				        SELECT 3 'id', 4.00 'score' UNION ALL
				        SELECT 4 'id', 3.85 'score' UNION ALL
				        SELECT 5 'id', 4.00 'score' UNION ALL
				        SELECT 6 'id', 3.65 'score' 
				       ) a
               )
    select score
         , dense_rank() over(order by score desc) as rank
      from Scores
    """
    return sql

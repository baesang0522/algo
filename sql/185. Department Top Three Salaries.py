def sql_solution():
    sql = """
    WITH Employee AS (
                SELECT *
				  FROM (
				        SELECT 1 id, 'Joe' name, 85000 salary, 1 departmentID FROM dual UNION ALL
				        SELECT 2 id, 'Henry' name, 80000 salary, 2 departmentID FROM dual UNION ALL
				        SELECT 3 id, 'Sam' name, 60000 salary, 2 departmentID FROM dual UNION ALL
				        SELECT 4 id, 'Max' name, 90000 salary, 1 departmentID FROM dual UNION ALL
				        SELECT 5 id, 'Janet' name, 69000 salary, 1 departmentID FROM dual UNION ALL
				        SELECT 6 id, 'Randy' name, 85000 salary, 1 departmentID FROM dual UNION ALL
				        SELECT 7 id, 'Will' name, 70000 salary, 1 departmentID FROM dual
				       )
                 )
         , Department as (
                          SELECT *
                            FROM (
                                  SELECT 1 id, 'IT' name FROM dual UNION ALL
                                  SELECT 2 id, 'Sales' name FROM dual
                                 )
                         )
    SELECT t2.name AS Department
         , t1.name AS EMPLOYEE 
         , t1.salary AS salary
      FROM (
            SELECT departmentID
                 , name
                 , salary 
                 , DENSE_RANK() over(PARTITION BY departmentID ORDER BY salary desc) AS den_rank
              FROM Employee
           ) t1
         , Department t2
     WHERE t1.departmentID = t2.id
       AND den_rank < 4
    """
    return sql

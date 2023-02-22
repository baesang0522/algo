def sql_solution():
    sql = """
    WITH Employee AS (
	                SELECT *
					  FROM (
					        SELECT 1 id, 'Joe' name, 70000 salary, 1 departmentID FROM dual UNION ALL
					        SELECT 2 id, 'Jim' name, 90000 salary, 1 departmentID FROM dual UNION ALL
					        SELECT 3 id, 'Henry' name, 80000 salary, 2 departmentID FROM dual UNION ALL
					        SELECT 4 id, 'Sam' name, 60000 salary, 2 departmentID FROM dual UNION ALL
					        SELECT 5 id, 'Max' name, 90000 salary, 1 departmentID FROM dual 
					       )
                 )
        , Department AS (
                         SELECT *
                           FROM (
                                 SELECT 1 id, 'IT' name FROM dual UNION ALL
                                 SELECT 2 id, 'Sales' name FROM dual 
                                )
                        )
    SELECT department
         , employee
         , salary
      FROM (
            SELECT t2.name AS Department
                 , t1.name AS Employee
                 , t1.salary
                 , max(t1.salary) over(PARTITION BY t2.name) AS max_sal
              FROM Employee t1
                 , Department t2
             WHERE t1.departmentID = t2.id
           )
     WHERE salary = max_sal
    """
    return sql

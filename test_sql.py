from sql_course import run as sql_run
from sql_course import check

good_query = """
select 
  CR1.course_run_id, 
  CR2.course_run_id, 
  CR1.nps, 
  CR2.nps, 
  I1.affiliation, 
  I2.affiliation, 
  CR1.start_date, 
  CR2.start_date 
from 
  (course_run as CR1 inner join instructors as I1 on (CR1.instructor_id = I1.instructor_id)) 
  inner join 
  (course_run as CR2 inner join instructors as I2 on (CR2.instructor_id = I2.instructor_id)) 
  on (CR1.nps +10 < CR2.nps 
    and CR1.start_date < CR2.start_date 
    and CR1.course_id = CR2.course_id 
    and (cast(strftime("%Y",CR1.start_date) as int) +1 >= (cast(strftime("%Y",CR2.start_date) as int)))) 
  where I1.affiliation = 'Cincinnati Financial Corp.'
"""

sql_run(good_query)
check(q2_4_2 = good_query)

row_mismatch_query = """
select 
  CR1.course_run_id, 
  CR2.course_run_id, 
  CR1.nps, 
  CR2.nps, 
  I1.affiliation, 
  I2.affiliation, 
  CR1.start_date, 
  CR2.start_date 
from 
  (course_run as CR1 inner join instructors as I1 on (CR1.instructor_id = I1.instructor_id)) 
  inner join 
  (course_run as CR2 inner join instructors as I2 on (CR2.instructor_id = I2.instructor_id)) 
  on (CR1.nps +10 < CR2.nps 
    and CR1.start_date < CR2.start_date 
    and CR1.course_id = CR2.course_id 
    and (cast(strftime("%Y",CR1.start_date) as int) +1 >= (cast(strftime("%Y",CR2.start_date) as int)))) 
--  where I1.affiliation = 'Cincinnati Financial Corp.'
"""

sql_run(row_mismatch_query)
check(q2_4_2 = row_mismatch_query)

col_mismatch_query = """
select 
  CR1.course_run_id, 
  CR2.course_run_id, 
--  CR1.nps, 
  CR2.nps, 
  I1.affiliation, 
  I2.affiliation, 
  CR1.start_date, 
  CR2.start_date 
from 
  (course_run as CR1 inner join instructors as I1 on (CR1.instructor_id = I1.instructor_id)) 
  inner join 
  (course_run as CR2 inner join instructors as I2 on (CR2.instructor_id = I2.instructor_id)) 
  on (CR1.nps +10 < CR2.nps 
    and CR1.start_date < CR2.start_date 
    and CR1.course_id = CR2.course_id 
    and (cast(strftime("%Y",CR1.start_date) as int) +1 >= (cast(strftime("%Y",CR2.start_date) as int)))) 
  where I1.affiliation = 'Cincinnati Financial Corp.'
"""

sql_run(col_mismatch_query)
check(q2_4_2 = col_mismatch_query)

cell_mismatch_query = """
  select 
    strftime("%Y",start_date) as year, 
    avg(num_learners_registered/num_tas) as learner_ta_ratio, 
    avg(num_weeks) as avg_num_weeks
  from courses 
  group by strftime("%Y",start_date)

"""
sql_run(cell_mismatch_query)
check(q_3_4 = cell_mismatch_query)


CREATE TABLE superheroes(
  -- Id of the superhero in the database
  id INTEGER PRIMARY KEY,
  -- Name of the superhero
  name VARCHAR(1024),
  -- Gender of the superhero
  gender VARCHAR(128),
  -- Eyecolor of the superhero
  eye_color VARCHAR(128),
  -- Race of the superhero
  race VARCHAR(1024),
  -- Hair color of the superhero
  hair_color VARCHAR(128),
  -- height of the superhero
  height REAL,
  -- publisher / comic brand that created the superhero
  publisher VARCHAR(1024),
  -- Skin color of the superhero
  skin_color VARCHAR(1024),
  -- Alignment of the superhero
  alignment VARCHAR(128),
  -- Weight of the superhero
  weight REAL,
  -- Timestamp when this record was created
  created_at TIMESTAMP,
  -- Timestamp of last update
  updated_at TIMESTAMP
);

create table xacts (
order_id integer primary key,
user_id integer,
user_demographic varchar(20),
product_id integer,
product_category varchar(20),
location_id integer,
location_region char(2),
purchase_date date,
list_price decimal(6,2),
sale_price decimal(6,2),
sale_margin decimal(6,2)
);


create table online_xacts (
order_id integer primary key,
user_id integer,
user_demographic varchar(20),
product_id integer,
product_category varchar(20),
marketing_channel text,
purchase_date date,
list_price decimal(6,2),
sale_price decimal(6,2),
sale_margin decimal(6,2)
);





create table courses (
course_id integer, 
course_name text,
course_desc text, 
course_category text, 
course_level text, 
start_date date, 
num_weeks integer, 
num_learners_registered integer, 
num_TAs integer,
nps integer
);




create table course_info (
course_id integer, 
course_name text,
course_desc text, 
course_category text, 
course_level text 
);


create table instructors (
instructor_id integer,
name text,
affiliation text,
teaching_experience integer
);





create table learners (
learner_id integer,
name text,
affiliation text
);




create table course_run (
course_run_id integer,
course_id integer,
instructor_id integer,
start_date date,
num_weeks integer,
num_TAs integer,
nps integer
);




create table course_registration_info (
course_run_id integer,
learner_id integer
);


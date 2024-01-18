import setuptools

setuptools.setup(
    name='sql_course',
    version='1.0.0',
    url='https://github.com/uplimit/course-intermediate-sql',
    author='Sourabh Bajaj, Reinier Koops',
    description='Run an SQL query for the "Intermediate SQL Course" on Uplimit',
    long_description=open('README.md').read(),
    license='GPL3',
    packages=['sql_course'],
    package_dir={'sql_course': 'sql_course'},
    include_package_data=True,
    package_data={'': ['data/*.csv', "data/*.sql"]},
    install_requires=['pandas'],
)

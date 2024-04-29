TIME_FOR_PROJECTS=3

name_architect = str(input())
number_projects = int(input())

required_hours = number_projects*TIME_FOR_PROJECTS
print(f"The architect {name_architect} will need "
      f"{required_hours} hours to complete {number_projects} project/s.")





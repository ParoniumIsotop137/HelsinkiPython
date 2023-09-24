from FileHandler import FileHandler
from Task import Task

first_comp = []
second_comp = []
task = Task()

first_comp = FileHandler.file_reading("B:\\Kurs\\Feladatok\\Mukorcsolya\\rovidprogram.csv", ";")
"""
print("Rövidprogram:\n")

for item in first_comp:
    print(item.__str__())
"""
second_comp = FileHandler.file_reading("B:\\Kurs\\Feladatok\\Mukorcsolya\\donto.csv", ";")

"""
print("\nDöntő:\n")

for item in first_comp:
    print(item.__str__())
"""
print(f"\n2. feladat: A rövidprogramban {len(first_comp)} induló volt.")
task.hungarian_competitor(second_comp)
name = input("\n5. feladat: Kérem a versenyző nevét: ")
task.search_for_name(first_comp, name.lower(), second_comp)

task.create_statistic(second_comp)
task.create_result_file(first_comp, second_comp)

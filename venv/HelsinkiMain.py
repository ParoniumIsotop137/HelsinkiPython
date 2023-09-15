from FileHandler import FileHandler

first_comp = []
second_comp = []

first_comp = FileHandler.file_reading("B:\\Kurs\\Feladatok\\Mukorcsolya\\rovidprogram.csv", ";")

print("Rövidprogram:\n")

for item in first_comp:
    print(item.__str__())

second_comp = FileHandler.file_reading("B:\\Kurs\\Feladatok\\Mukorcsolya\\donto.csv", ";")

print("\nDöntő:\n")

for item in first_comp:
    print(item.__str__())

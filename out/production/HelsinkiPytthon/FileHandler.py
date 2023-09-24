from io import open

from Competition import Competition


class FileHandler:

    def file_reading(file_path, separator):
        first_data = []
        i = 1
        with open(file_path, "r") as file:
            for line in file:
                data = line.strip().split(separator)
                if (i > 1):
                    comp = Competition(data[0], data[1], data[2], data[3], data[4])
                    first_data.append(comp);
                i = i + 1
            return first_data

    def save_champions_list(self, file_path, champions):

        sep = ";"

        i = 1
        with open(file_path, "w") as file:
            for item in champions:
                text = str(i) + sep + item.name + sep + item.country + sep + str(item.technical_score)
                file.write(text + "\n")
                i += 1
        print("\n8. feladat: vegredmeny.csv")

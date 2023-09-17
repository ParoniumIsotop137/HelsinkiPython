from Competition import Competition


class FileHandler:

    def file_reading(filePath, separator):
        first_data = []
        i = 1
        with open(filePath, "r") as file:
            for line in file:
                data = line.strip().split(separator)
                if (i > 1):
                    comp = Competition(data[0], data[1], data[2], data[3], data[4])
                    first_data.append(comp);
                i = i + 1
            return first_data

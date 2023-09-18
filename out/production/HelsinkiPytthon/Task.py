class Task:

    def hungarian_competitor(self, second_comp_list):
        i = 0
        while i < len(second_comp_list) and second_comp_list[i].country != "HUN":
            i = i + 1
        if i < len(second_comp_list):
            print("\n3. feladat: A magyar versenyző bejutott a kűrbe.")
        else:
            print("\n3. feladat: Nem jutott be magyar versenyző a kűrbe.")

    def search_for_name(self, first_comp, name, second_comp):

        i = 0
        while i < len(first_comp) and (first_comp[i].name).lower() != name:
            i = i + 1
        if i < len(first_comp):
            show_all_score(first_comp, i, second_comp)
        else:
            print("Ilyen nevű induló nem volt.")

    def create_statistic(self, second_comp):

        statistics = {}

        for item in second_comp:
            statistics.update({item.country: 0})

        for item in second_comp:
            for item2 in statistics:
                if item.country == item2:
                    statistics[item2] += 1
        print("\n7. feladat:\n")
        for item in statistics:
            if statistics[item] > 1:
                print(f"{item}: {statistics[item]} versenyző")


def show_all_score(first_comp, i, second_comp):
    total_score = 0

    total_score += first_comp[i].technical_score + first_comp[i].component_score

    print(f"\n6. feladat: A versenyző összpontszáma: {total_score}")

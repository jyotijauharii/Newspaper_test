def newspaper(budget):
    newspaper = {
        "TOI": [3, 3, 3, 3, 3, 5, 6],
        "Hindu": [2.5, 2.5, 2.5, 2.5, 2.5, 4, 4],
        "ET": [4, 4, 4, 4, 4, 4, 10],
        "BM": [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5],
        "HT": [2, 2, 2, 2, 2, 4, 4],
    }

    result = []

    newspaper_sums = {
        "TOI": sum(newspaper["TOI"]),
        "Hindu": sum(newspaper["Hindu"]),
        "ET": sum(newspaper["ET"]),
        "BM": sum(newspaper["BM"]),
        "HT": sum(newspaper["HT"]),
    }


    newspaper_sums = dict(sorted(newspaper_sums.items(), key=lambda item: item[1]))

    result_list = []

    for i in range(0, len(newspaper_sums)):
      for j in range(i+1, len(newspaper_sums)):
        if newspaper_sums[list(newspaper_sums)[i]] + newspaper_sums[list(newspaper_sums)[j]] <= budget:
          result_list.append([list(newspaper_sums)[i], list(newspaper_sums)[j]])
        else :
          break
    
    print (result_list)

newspaper(40)
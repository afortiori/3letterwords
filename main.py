import graph
"""
finds path between two 3 letter words using a graph and bfs
"""


def file_to_list(file_name):
    # takes the path to the file and returns a list of its contents
    file = open(file_name, "r")
    data = file.read()
    word_list = data.split("\n")
    file.close()
    return word_list


def find_neighbors(source_word, word_list):
    # returns all words in the word list that are one letter away
    # from the inputed word
    neighbors = []
    for word in word_list:
        if source_word[0] == word[0] and source_word[1] == word[1]:
            neighbors.append(word)
        if source_word[1] == word[1] and source_word[2] == word[2]:
            neighbors.append(word)
        if source_word[0] == word[0] and source_word[2] == word[2]:
            neighbors.append(word)
    return neighbors


def find_path_between_words(file_name, source_word, destination_word):
    # Given a word list and a 3 letter source & destination word, creates a
    # graph and then does BFS to find the path between, which is then returned
    words = file_to_list(file_name)

    # Bulding an adjacencies list to initalize the grpah with
    adjacencies = []
    first_degree = find_neighbors(source_word, words)
    for f in first_degree:
        adjacencies.append([source_word, f])
        second_degree = find_neighbors(f, words)
        for s in second_degree:
            adjacencies.append([f, s])
            third_degree = find_neighbors(s, words)
            for t in third_degree:
                adjacencies.append([s, t])

    new_graph = graph.Graph(adjacencies)
    state, pred = new_graph.bfs_search(source_word)
    path = new_graph.reconstruct_bfs_path(pred, destination_word)
    return path


print(find_path_between_words("threeletterwords.txt", "cut", "sob"))

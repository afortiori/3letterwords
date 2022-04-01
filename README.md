# Question 3

In order to find the paths between two three letter words, I created a graph class and then added functions to that class which implemented the pseudocode for BFS and reconstruct BFS. The graph class  uses an adjacency list style representation, where adjacencies are represented with Python collections defaultdict. The keys are a given vertex and the values are sets containing all adjecent vertexs.

Then, in the main python file, I generated a list of adjacencies using for-each loops in order to be able to initialize my graph. Then, I simply did the BFS and then printed the result from reconstruct BFS to show the path between two words.

So, with the source word 'cut' and the goal word 'sob', the following code would go at the bottom of main.py to print the path:

```python
print(find_path_between_words("threeletterwords.txt", "cut", "sob"))

```

Which would result in the following output:
```shell
['cut', 'cot', 'cob', 'sob']

```

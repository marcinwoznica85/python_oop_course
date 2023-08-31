"""
Forest class has protected attribute indicating number of trees in it
Add getter property retrieving number of trees
Add setter property disallowing reducing number of trees


"""


class Forest:
    def __init__(self) -> None:
        self._trees = 650

    ...


forest = Forest()
print(forest.trees)
forest.trees = 700
print(forest.trees)
forest.trees = 600

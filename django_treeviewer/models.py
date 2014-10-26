from django.db import models


class Tree:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.max_recursion = 2

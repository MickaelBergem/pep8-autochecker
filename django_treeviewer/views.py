from django.shortcuts import render
import os

from models import Tree


class TreeViewer:
    def __init__(self, tree_rootdir=None):
        self.tree = Tree(tree_rootdir)
        self.rendered_tree = []

    def render_to_dict(self):
        return self._render_index(self.tree.root_dir)

    def _render_index(self, folder):
        current_node = []
        for file_name in os.listdir(folder):
            file_path = os.path.join(folder, file_name)
            if file_name[0:1] == '.':
                # We don't want the hidden files / folders
                continue
            elif os.path.isdir(file_path):
                # Render folders
                node = self._render_folder(file_name, file_path)
            elif file_path[-3:] == '.py':
                # Add the Python files
                node = {
                    'name': file_name,
                    'path': file_path,
                    'node_type': 'file'
                }
            else:
                # We don't want the other files
                continue
            current_node.append(node)
        return current_node

    def _render_folder(self, folder, folder_path):
        return {
            'content': self._render_index(folder_path),
            'node_type': 'folder',
            'name': folder,
            'path': folder_path
        }

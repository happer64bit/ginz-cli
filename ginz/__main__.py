import argparse
import toml
import sys

from .algo import tree

from tqdm import tqdm
from git import Repo, RemoteProgress
from colorama import Fore, Style

class CloneProgress(RemoteProgress):
    def __init__(self):
        super().__init__()
        self.pbar = tqdm(colour="GREEN", dynamic_ncols=True)

    def update(self, op_code, cur_count, max_count=None, message=''):
        self.pbar.total = max_count
        self.pbar.n = cur_count
        self.pbar.refresh()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", "-v", action="store_true", help="Print Out Version")
    args = parser.parse_args()

    if args.version:
        print(f"{Fore.YELLOW} v1.0.0 {Fore.RESET}")
        sys.exit()

    root_tree = tree.TreeNode("Cloned Directory")

    with open("GInz.toml") as config_file:
        config = toml.load(config_file)

        for section_name, section in config.items():
            branch = section.get("branch")
            if branch is None:
                branch = "main"
            repo = Repo.clone_from(url=section.get("source"), to_path=section_name, progress=CloneProgress(), branch=branch)

            child_node = tree.TreeNode(f"{section_name} (branch: \x1b[3m {Fore.YELLOW}*{branch}*) {Fore.RESET} {Style.NORMAL}")
            root_tree.add_child(child_node)

    root_tree.print_tree()

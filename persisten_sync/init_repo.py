#
# Digital Poet
#
# Aran Moncusí Ramírez <aran@digitalpoet.info>
#
# Check if repo is init
# If not, clone repo
# git checkout to selected branch
#
import git.repo.fun
from git import Repo


def is_directory_init(path: str):
    return git.repo.fun.is_git_dir(path)


def clone_repository(path: str, repository_source: str, branch_name) -> Repo:
    return git.Repo.clone_from(to_path=path, url=repository_source, multi_options=('--recurse-submodules',),
                               branch=branch_name)


def init(path, repository, branch_name):

    if not is_directory_init(path):
        clone_repository(path, repository, branch_name)


# if __name__ == '__main__':
#     init("../t", "git@github.com:EndermanAPM/stock_updater.git", 'devel')

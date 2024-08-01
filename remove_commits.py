# remove_commits.py
from git_filter_repo import FilterRepo
from datetime import datetime

def commit_callback(commit, aux_info):
    # Define date range
    start_date = datetime(2024, 8, 1)
    end_date = datetime(2024, 12, 31)

    # Convert commit date to datetime
    commit_date = datetime.fromtimestamp(commit.committer_date)

    # Skip commits in the specified range
    if start_date <= commit_date <= end_date:
        commit.skip()

filter_repo = FilterRepo()
filter_repo.commit_callback = commit_callback
filter_repo.run()

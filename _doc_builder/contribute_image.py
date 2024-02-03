import pandas as pd
import calmap
import matplotlib.pyplot as plt
import git
from helper.lib import abs_path, PROJECT_DIR
 
repo = git.Repo(PROJECT_DIR)
commits = list(repo.iter_commits(paths='.'))
data = pd.DataFrame({
    "commit_id": [commit.hexsha for commit in commits],
    "date": [commit.committed_datetime for commit in commits],
})
data['date'] = pd.to_datetime(data['date'],utc=True).dt.date
data['date'] = pd.to_datetime(data['date'])
summary = data[['date', 'commit_id']].groupby('date').count().reset_index()
summary.set_index("date", inplace=True)
summary["commit_id"]
fig, axes = calmap.calendarplot(summary["commit_id"], fig_kws={"figsize": (12, 8)}, cmap="YlGn")
axes[0].set_title("TIL Updates", fontsize=18)
plt.savefig(abs_path("_doc_builder/til_update.png"), bbox_inches='tight')

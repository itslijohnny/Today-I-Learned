## GitHub Checkout Action Preserve File Modification Time

> https://finisky.github.io/githubactiontorestorefilemtime.en/

```yaml
- name: Checkout
  uses: actions/checkout@v3.0.0
  with:
	token: ${{ secrets.MYPAT }}
	submodules: 'true'
	persist-credentials: false
	fetch-depth: 0

- name: Restore Timestamps
  uses: chetan/git-restore-mtime-action@v1

```
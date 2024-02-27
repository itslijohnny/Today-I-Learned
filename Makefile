.PHONY: serve
serve:
	docker-compose up 

.PHONY: update-readme
update-readme:
	python ./_doc_builder/update_file_name.py
	python ./_doc_builder/update_readme.py	

.PHONY: test-action
test-action:
	act -s GITHUB_TOKEN=$GITHUB_TOKEN --artifact-server-path ./tmp/artifacts -e event.json
.PHONY: test
test:
	poetry run pytest

.PHONY: test-watch
test-watch:
	poetry run ptw -- --cov=aoc

.PHONY: test-cov
test-cov:
	poetry run pytest --cov=aoc

.PHONY: cq
cq:
	poetry run pre-commit run --all

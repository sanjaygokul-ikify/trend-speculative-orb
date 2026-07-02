install:	pip install --editable .
sanity:	pyright .
	pylint --rcfile=.pylintrc .
	poetry update
	docker-compose build
	docker-compose up -d
	sleep 5
	touch /tmp/speculative-ready
	echo 'Waiting on warmup...'
	sleep 30

bench:	python benchmarks/memory_shard.py

perf:	python benchmarks/sharing_scaling.py --concurrent 1000
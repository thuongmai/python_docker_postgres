run:
	python demo.py

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

install:
	pip3 install -r requirements.txt
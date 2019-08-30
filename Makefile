default: build

build:
	docker-compose build
dev:
	docker-compose up
test:
	docker-compose -f docker-compose.test.yml up

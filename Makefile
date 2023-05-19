APP_NAME := cron

.PHONY: docker-up
docker-up:
	docker build -t cron .
	docker run cron
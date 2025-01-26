IMAGE_NAME := mbani002/basic
VERSION := 1.0.3

.PHONY: build push

build:
	docker buildx create --use --name multi-platform-builder || true
	docker buildx build --platform linux/amd64,linux/arm64 \
		-t $(IMAGE_NAME):$(VERSION) \
		-t $(IMAGE_NAME):latest \
		--push \
		.

push: build 
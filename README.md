# FastAPI boilerplate

My intention with this is building an API template using FastAPI as a web framework and Poetry as a dependency manager.

## Runnning the application in a container

To run this app, you need to install docker first. After that you move to the folder that you have download this repo, then you should execute

```bash
docker build -t {IMAGE_NAME}
```

Where `{IMAGE_NAME}` is the name of the images that will be created. After creating the image, you can run a container using:

```bash
docker run -d --name {CONTAINER_NAME} -p 8080:8080 {IMAGE_NAME}
```

Again, `{CONTAINER_NAME}` is just the name of the container what you prefer.

Once the container starts, you can go to the swagger documentation to interact with available endpoints. You can found swagger in localhost

## TODO

- Add dockerfile to run application from container
- Add github actions:

  - To run tests
  - To get coverage

- Run graphana
- Run prometheus
- Add PRs template
- Protect develop/main branches
- Create a cookiecutter with this project? It is possible

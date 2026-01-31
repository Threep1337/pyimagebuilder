# Docker image rebuilder

This project will monitor an upstream repo and look for images to rebuild and push to a downstream repo

## General notes

Make sure to use the venv:

`source venv/bin/activate`

I will need to freeze the python requirements later

## Testing notes

To easily test this, create your own repo to act as the upstream repo, you can do this by using a docker image:

```
docker run -d \
  -p 5000:5000 \
  --name local-registry \
  registry:3
```

Pick a simple, small upstream dummy image to use as a fake upstream image that you can easily rebuild:


`docker image pull debian:bookworm-slim`

cd into the dockerTemp folder and then build the image using the docker file:

`docker build --build-arg IMAGE_VERSION=1 -t localhost:5000/upstreamimage:latest .`

To run it and see the version in this upstream image:

`docker run --rm localhost:5000/upstreamimage:latest`

You can then push this image to your local registry:

`docker image push localhost:5000/upstreamimage:latest`


To view the repos in your registry:

`curl localhost:5000/v2/_catalog`

To see the tags for your repo:

`curl localhost:5000/v2/upstreamimage/tags/list`


More docs for this:

[The Spec](https://distribution.github.io/distribution/spec/api/)

Remove the local image:
`docker image rm localhost:5000/upstreamimage:latest`

Inspect the remote image:
`docker buildx imagetools inspect localhost:5000/upstreamimage:latest`

Note that if the image uses a manifest I think I will need to use the `docker manifest inspect` commands instead.

It looks like there is also a way with the repo api, look into that more.

Rebuild the downstream image:

`docker build -t localhost:5000/downstream:latest -f Dockerfile-downstream .`

Run the downstream image:
`docker run localhost:5000/downstream:latest`

Push the downstream image:

`docker image push localhost:5000/downstream:latest`
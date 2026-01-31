FROM debian:bookworm-slim

ARG IMAGE_VERSION

RUN echo ${IMAGE_VERSION} > /tmp/imagever.txt
CMD ["cat","/tmp/imagever.txt"]

FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Work around intermittent apt failures caused by stale Yarn signing key/source.
RUN rm -f /etc/apt/sources.list.d/yarn.list

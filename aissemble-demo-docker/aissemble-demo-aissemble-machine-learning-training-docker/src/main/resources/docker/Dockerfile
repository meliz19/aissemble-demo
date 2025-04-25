# Script for creating base training service image
#
# GENERATED DOCKERFILE - please ***DO*** modify.
#
# Generated from: templates/general-docker/training.docker.file.vm

ARG DOCKER_BASELINE_REPO_ID
ARG VERSION_AISSEMBLE

# Start build stage based on aiSSEMBLE extension of Nvidia base image
FROM ${DOCKER_BASELINE_REPO_ID}boozallen/aissemble-nvidia:${VERSION_AISSEMBLE}

ENV GIT_PYTHON_REFRESH=quiet
ENV DEBIAN_FRONTEND=noninteractive
ENV ENABLE_LINEAGE=true

RUN apt-get -y update \
    && apt-get install -y software-properties-common \
    && add-apt-repository universe \
    && add-apt-repository ppa:deadsnakes/ppa

# Install Python 3.11 and related packages, and perform cleanup
RUN apt-get -y update \
    && apt install python3.11 python3.11-distutils gcc python3.11-dev curl -y \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11

# Ensure that any needed Krausening properties are copied and KRAUSENING_BASE environment variable is set!
ENV KRAUSENING_BASE /app/config
COPY target/krausening/base/ /app/config/
COPY src/main/resources/krausening/base/ /app/config/

# Install aissemble-machine-learning-training dependencies
COPY target/aissemble-machine-learning-training/dist/requirements.txt /installation/aissemble-machine-learning-training/
RUN python3.11 -m pip install --ignore-installed -r /installation/aissemble-machine-learning-training/requirements.txt

# Install aissemble-machine-learning-training
COPY target/aissemble-machine-learning-training/dist /modules/aissemble-machine-learning-training
RUN set -e && \
    cd /modules/aissemble-machine-learning-training; for x in *.whl; do pip install $x --no-cache-dir --no-deps; done

CMD python3.11 -m aissemble_machine_learning_training.example_machine_learning_pipeline_driver

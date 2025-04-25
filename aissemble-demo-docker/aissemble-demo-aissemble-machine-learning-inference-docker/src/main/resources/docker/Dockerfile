# Script for creating base inference service image
#
# GENERATED DOCKERFILE - please ***DO*** modify.
#
# Generated from: templates/general-docker/inference.docker.file.vm

ARG DOCKER_BASELINE_REPO_ID
ARG VERSION_AISSEMBLE

# Start build stage based on aiSSEMBLE extension of Nvidia base image
FROM ${DOCKER_BASELINE_REPO_ID}boozallen/aissemble-nvidia:${VERSION_AISSEMBLE}

# Set environment variables
ENV GIT_PYTHON_REFRESH=quiet
ENV DEBIAN_FRONTEND=noninteractive

# Update repositories and add necessary ones
RUN apt-get -y update \
    && apt-get install -y software-properties-common \
    && add-apt-repository universe \
    && add-apt-repository ppa:deadsnakes/ppa

# Install Python 3.11 and related packages, install python-is-python3, create symbolic link, and perform cleanup
RUN apt-get -y update \
    && apt install python3.11 python3.11-distutils gcc python3.11-dev curl -y \
    && apt-get install -y python-is-python3 \
    && rm -f /usr/bin/python \
    && ln -s /usr/bin/python3.11 /usr/bin/python \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean
    
# Download and install pip for Python 3.11
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11

# Copy Perceptor app.py file to required location
COPY src/generated/resources/perceptor/app.py /home/app/

# Ensure that any needed Krausening properties are copied and KRAUSENING_BASE environment variable is set!
ENV KRAUSENING_BASE /app/config
COPY target/krausening/base/ /app/config/
COPY src/main/resources/krausening/base/ /app/config/

#Install aissemble-machine-learning-inference dependencies
COPY target/aissemble-machine-learning-inference/dist/requirements.txt /installation/aissemble-machine-learning-inference/
RUN python -m pip install --ignore-installed -r /installation/aissemble-machine-learning-inference/requirements.txt

# Install aissemble-machine-learning-inference
COPY target/aissemble-machine-learning-inference/dist /modules/aissemble-machine-learning-inference
RUN set -e && \
    cd /modules/aissemble-machine-learning-inference; for x in *.whl; do python -m pip install $x --no-cache-dir --no-deps; done

# Start the inference API drivers for FastAPI and gRPC
CMD python -m aissemble_machine_learning_inference.inference_api_driver "fastAPI" & python -m aissemble_machine_learning_inference.inference_api_driver "grpc"
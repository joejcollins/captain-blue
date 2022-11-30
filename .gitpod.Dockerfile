FROM gitpod/workspace-python-3.10

USER gitpod

# Install custom tools, runtime, etc. using apt-get
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
#
# RUN sudo apt-get -q update && \
#     sudo apt-get install -yq bastet && \
#     sudo rm -rf /var/lib/apt/lists/*
#
# More information: https://www.gitpod.io/docs/config-docker/

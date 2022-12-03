FROM gitpod/workspace-postgres

ARG PYTHON_VERSION=3.10.7
RUN pyenv install "$PYTHON_VERSION" && \
    pyenv global "$PYTHON_VERSION"

RUN curl -sSL https://install.python-poetry.org | python3 -
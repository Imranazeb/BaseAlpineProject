FROM python:3.12-alpine as base

ARG DEV=false

COPY requirements/* tmp/

RUN python -m venv /opt/venv \
    && /opt/venv/bin/python -m pip install --upgrade pip \
    # ---------- Comment out if not installing postgresql
    # && apk add --no-cache postgresql-client \                   
    # && apk add --no-cache build-base postgresql-dev musl-dev \
    # --virtual .build-deps \
    # ---------- End Comment out
    && if [ "$DEV" = "true" ]; then \
        echo "Installing development dependencies..."; \
        /opt/venv/bin/pip install --no-cache-dir -r /tmp/dev.txt; \
    else \
        echo "Installing production dependencies..."; \
        /opt/venv/bin/pip install --no-cache-dir -r /tmp/requirements.txt; \
    fi \ 
    && rm -rf /tmp/* \
    && apk del .build-deps || true

ENV PATH="/opt/venv/bin:$PATH"


COPY src/ /src/
WORKDIR /src

CMD [ "python", "main.py" ]

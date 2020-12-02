FROM python:buster

LABEL "Maintainer" "Kevin Gomez Gonzalez"

RUN /usr/local/bin/python -m pip install --upgrade pip && \
    mkdir -p /var/www/sites/tt-2021-crud/src/ && \
    pip install virtualenv

COPY docker-entrypoint.sh /sbin/

COPY requirements.txt /var/www/sites/tt-2021-crud

COPY src/ /var/www/sites/tt-2021-crud/src/

RUN useradd tt-user -m && \
    chown tt-user:tt-user -R /var/www/sites/tt-2021-crud && \
    virtualenv /var/www/sites/tt-2021-crud && \
    . /var/www/sites/tt-2021-crud/bin/activate && \
    /var/www/sites/tt-2021-crud/bin/python -m pip install --upgrade pip && \
    pip install -r /var/www/sites/tt-2021-crud/requirements.txt && \
    deactivate && \
    chmod +x /sbin/docker-entrypoint.sh

WORKDIR /var/www/sites/tt-2021-crud/src/

EXPOSE 8080

USER tt-user

ENTRYPOINT [ "/sbin/docker-entrypoint.sh" ]
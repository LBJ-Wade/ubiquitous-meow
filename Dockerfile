FROM python:2.7

MAINTAINER Kevin Yu <thekevinyu@gmail.com>

RUN apt-get update && \
    apt-get install -y libblas-dev liblapack-dev libatlas-base-dev \
                       gfortran vim

RUN mkdir packages

# Setup totipnat (tipsy binary converter)
RUN mkdir /usr/include/sys && \
    touch /usr/include/sys/types.h /usr/include/sys/time.h
RUN cd packages && \
    git clone https://github.com/N-BodyShop/tipsy_tools.git && \
    cd tipsy_tools && \
    make && \
    ln -s /packages/tipsy_tools/totipnat /usr/local/bin/totipnat
ENV TOTIPNAT /usr/local/bin/totipnat

# Setup AHF
RUN cd packages && \
    wget http://popia.ft.uam.es/AHF/files/ahf-v1.0-084.tgz && \
    tar -xzvf ahf-v1.0-084.tgz
ADD build/Makefile.config /packages/ahf-v1.0-084/Makefile.config
RUN cd packages/ahf-v1.0-084 && \
    make && \
    ln -s /packages/ahf-v1.0-084/bin/AHF-v1.0-084 /usr/local/bin/ahf
ENV AHF /usr/local/bin/ahf

# Clone code repository
RUN cd / && git clone https://github.com/kevinyu/ubiquitous-meow.git /code

# Pip install python dependencies
RUN pip install --upgrade cython && \
    pip install numpy && \
    pip install -r /code/requirements.txt

ENV DATA_DIR /data
ENV TEMPLATES_DIR /code/templates
RUN rm /code/Notebooks/analysis && \
    ln -s /code/analysis /code/Notebooks/analysis

### From http://jupyter-notebook.readthedocs.org/en/latest/public_server.html
# Add Tini. Tini operates as a process subreaper for jupyter. This prevents
# kernel crashes.
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

EXPOSE 8888

VOLUME /data

CMD jupyter-notebook --port=8888 --no-browser --ip=0.0.0.0 --notebook-dir=/code

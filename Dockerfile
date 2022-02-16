FROM ubuntu
#FROM  nvidia/cuda:11.3.1-cudnn8-runtime-ubuntu20.04

RUN apt update && apt upgrade -y
RUN apt install -y python3-pip curl git 

# install node js for jupyter-lab plugins
RUN curl -fsSL https://deb.nodesource.com/setup_current.x | bash -
RUN apt-get install -y nodejs


RUN pip install 'jupyterlab>=3.0.0,<4.0.0a0' jupyterlab-lsp 'python-lsp-server[all]' ipykernel
#numpy pandas matplotlib scipy sklearn seaborn

# fix tz issues
ENV TZ=Europe/Oslo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


RUN python3 -m pip install ipywidgets
RUN jupyter nbextension enable --py widgetsnbextension

ARG user=jupyter
ARG group=jupyter
ARG uid=1000
ARG gid=1000
RUN groupadd -g ${gid} ${group}
RUN useradd -u ${uid} -g ${group} -s /bin/sh -m ${user}


RUN apt install -y graphviz

# RUN python3 -m ipykernel install --name=.py_env
# Switch to user
USER ${uid}:${gid}




WORKDIR home/jupyter
RUN mkdir  project
RUN mkdir  .jupyter

RUN mkdir -p /home/jupyter/.local/share/jupyter/kernels/viritual_env
# add entrypoint
COPY ./entrypoint.sh ./entrypoint.sh

WORKDIR project

EXPOSE 8888
CMD /bin/bash ./../entrypoint.sh
# CMD ["jupyter", "lab", "--port=8888", "--no-browser",  "--ip=0.0.0.0"]


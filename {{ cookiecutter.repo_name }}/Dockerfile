ARG version

FROM analytics-base:$version
LABEL maintainer="Neighborhoods <neighborhoods.engineering@neighborhoods.com>"

ARG directory

WORKDIR $directory

COPY jupyter_notebook_config.json /root/.jupyter/jupyter_notebook_config.json
ADD . $directory

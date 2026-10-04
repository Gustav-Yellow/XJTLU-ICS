FROM jupyter/minimal-notebook:3.2

MAINTAINER Piotr Szul

USER root

# Spark dependencies
ENV APACHE_SPARK_VERSION 2.1.1
ENV HADOOP_VERSION 2.7

# Install necessary packages
RUN apt-get -y update && \
    apt-get install -y --no-install-recommends openjdk-7-jre-headless python-qt4 && \
    apt-get clean

# Download pre-compiled Apache Spark
RUN wget -qO - http://d3kbcqa49mib13.cloudfront.net/spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz | tar -xz -C /usr/local/

RUN cd /usr/local && ln -s spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} spark

#Use unprivileged user provided by base image
USER jovyan

# Install Python 2 packages and kernel spec
RUN conda create --yes -p $CONDA_DIR/envs/python2 python=2.7 \
    'jupyter' \
    'pandas' \
    'matplotlib' \
    'numpy' \
    'scikit-learn' \
    'pil' \
    && conda clean -yt


#Prepare environment
ENV SPARK_HOME /usr/local/spark
ENV PATH $SPARK_HOME/bin:$PATH
ENV PYSPARK_PYTHON=$CONDA_DIR/envs/python2/bin/python2.7

# Install pyspark kernel
COPY docker/pyspark /tmp/pyspark/
RUN $CONDA_DIR/envs/python2/bin/jupyter kernelspec install /tmp/pyspark/ --user

COPY docker/ipyspark /usr/local/bin/ipyspark

USER root
#COPY and ADD don't add as the current user https://github.com/docker/docker/issues/7390, https://github.com/docker/docker/pull/13600
RUN chown jovyan:jovyan $HOME/* -R

#SparkUI
EXPOSE 4040

COPY docker/jupyter_notebook_config.py /etc/jupyter/

USER jovyan

CMD ["ipyspark"]

# syntax=docker/dockerfile:1
# ============================================================================
#  PySpark: 1,000 Examples — reader's environment
#
#  A single "runtime" target: Spark 3.5.3 + pinned JARs + pinned Python deps.
#  Matches the exact stack the book's examples were verified against.
#
#  Use it via docker compose (see docker-compose.yml) or standalone:
#     docker build -t pyspark1000 .
#     docker run --rm -it -v $(pwd):/workspace pyspark1000
# ============================================================================

FROM python:3.11-slim-bookworm

# --- pinned stack -----------------------------------------------------------
ARG SPARK_VERSION=3.5.3
ARG HADOOP_PROFILE=3
ARG SCALA_BINARY=2.12
ARG DELTA_VERSION=3.2.0
ARG SPARK_XML_VERSION=0.18.0

ENV SPARK_VERSION=${SPARK_VERSION} \
    SPARK_HOME=/opt/spark \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="${SPARK_HOME}/bin:${SPARK_HOME}/sbin:${JAVA_HOME}/bin:${PATH}"

# --- system deps ------------------------------------------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
        openjdk-17-jre-headless \
        curl \
        ca-certificates \
        procps \
        tini \
        gosu \
    && rm -rf /var/lib/apt/lists/*

# --- Spark ------------------------------------------------------------------
RUN curl -fsSL \
      "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_PROFILE}.tgz" \
      -o /tmp/spark.tgz \
    && mkdir -p ${SPARK_HOME} \
    && tar -xzf /tmp/spark.tgz -C ${SPARK_HOME} --strip-components=1 \
    && rm /tmp/spark.tgz

# --- JARs baked in ----------------------------------------------------------
ARG MAVEN=https://repo1.maven.org/maven2
RUN set -eux; \
    cd ${SPARK_HOME}/jars; \
    curl -fsSLO "${MAVEN}/org/apache/spark/spark-avro_${SCALA_BINARY}/${SPARK_VERSION}/spark-avro_${SCALA_BINARY}-${SPARK_VERSION}.jar"; \
    curl -fsSLO "${MAVEN}/com/databricks/spark-xml_${SCALA_BINARY}/${SPARK_XML_VERSION}/spark-xml_${SCALA_BINARY}-${SPARK_XML_VERSION}.jar"; \
    curl -fsSLO "${MAVEN}/io/delta/delta-spark_${SCALA_BINARY}/${DELTA_VERSION}/delta-spark_${SCALA_BINARY}-${DELTA_VERSION}.jar"; \
    curl -fsSLO "${MAVEN}/io/delta/delta-storage/${DELTA_VERSION}/delta-storage-${DELTA_VERSION}.jar"

# --- Python deps ------------------------------------------------------------
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# --- Spark config -----------------------------------------------------------
COPY conf/spark-defaults.conf ${SPARK_HOME}/conf/spark-defaults.conf
COPY conf/log4j2.properties ${SPARK_HOME}/conf/log4j2.properties

# --- non-root user matching host UID ---------------------------------------
ARG UID=1000
ARG GID=1000
RUN groupadd -g ${GID} spark 2>/dev/null || true \
    && useradd -m -u ${UID} -g ${GID} -s /bin/bash spark 2>/dev/null || true \
    && mkdir -p /workspace /workspace/spark-events /home/spark/.ivy2 \
    && chown -R ${UID}:${GID} /workspace /home/spark

WORKDIR /workspace
USER ${UID}:${GID}

EXPOSE 4040 8888

ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["bash"]

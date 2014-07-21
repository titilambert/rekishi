from ubuntu:trusty
MAINTAINER Philippe Pepos Petitclerc <philippe.pepos-petitclerc@savoirfairelinux.com>

# Install InfluxDB
RUN apt-get update
RUN apt-get install -y wget vim
RUN wget http://s3.amazonaws.com/influxdb/influxdb_latest_amd64.deb
RUN dpkg -i influxdb_latest_amd64.deb

# Copy configuration file
ADD config.toml /config/config.toml

# Remove file handle limits
RUN echo "# Removing file handle limits for influxdb" >> /etc/security/limits.conf
RUN echo "influxdb soft nofile 4096" >> /etc/security/limits.conf
RUN echo "influxdb hard nofile 65536" >> /etc/security/limits.conf

# Admin server
EXPOSE 8083

# HTTP API
EXPOSE 8086

# HTTPS API
EXPOSE 8084

# Raft port (for clustering, don't expose publicly!)
EXPOSE 8090

# Protobuf port (for clustering, don't expose publicly!)
EXPOSE 8099

# CMD ["-config=/config/config.toml"]
# ENTRYPOINT ["/usr/bin/influxdb"]

CMD ["service influxdb start"]
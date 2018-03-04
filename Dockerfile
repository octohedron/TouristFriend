# Use an official Python runtime as a parent image
FROM ubuntu:16.04

RUN apt-get update -y && \
  apt-get install python3-pip idle3 -y && \
  pip3 install --no-cache-dir --upgrade pip && \
  \
  # delete cache and tmp files
  apt-get clean && \
  apt-get autoclean && \
  rm -rf /var/cache/* && \
  rm -rf /tmp/* && \
  rm -rf /var/tmp/* && \
  rm -rf /var/lib/apt/lists/* && \
  \
  # make some useful symlinks that are expected to exist
  cd /usr/bin && \
  ln -s idle3 idle && \
  ln -s pydoc3 pydoc && \
  ln -s python3 python && \
  ln -s python3-config python-config && \
  cd /

# Set the working directory to /touristfriend
WORKDIR ./touristfriend

# Copy the current directory contents into the container at /touristfriend
ADD . /touristfriend

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Args for private keys
ARG GMAPS_KEY
ARG F_ID
ARG F_C_S
ARG G_API
ARG YELP_ID
ARG YELP_API_KEY
ARG YELP_SECRET

# Set them for the program
ENV GMAPS_KEY=$GMAPS_KEY
ENV F_ID=$F_ID
ENV F_C_S=$F_C_S
ENV G_API=$G_API
ENV YELP_ID=$YELP_ID
ENV YELP_API_KEY=$YELP_API_KEY
ENV YELP_SECRET=$YELP_SECRET
ENV FLASK_APP=touristfriend/__init__.py

# Ubuntu locale settings
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Run app.py when the container launches
CMD ["flask", "run", "--host", "0.0.0.0"]

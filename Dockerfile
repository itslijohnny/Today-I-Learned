FROM ubuntu
LABEL maintainer="Johnny"

RUN apt-get update
RUN apt-get install ruby-full build-essential zlib1g-dev -y
RUN apt install python3.11 python3-pip -y

ENV LANG=C.UTF-8
ENV APP_HOME /myapp
# RUN rm -rf $APP_HOME
# RUN mkdir $APP_HOME
# WORKDIR $APP_HOME

RUN echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
RUN echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc

COPY docker_script.sh /docker_script.sh
RUN chmod +x /docker_script.sh
ENTRYPOINT "/docker_script.sh"
# RUN bundle exec jekyll serve
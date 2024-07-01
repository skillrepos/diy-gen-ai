FROM mcr.microsoft.com/devcontainers/base:bookworm
RUN apt update && apt upgrade -y
RUN apt install meson ninja-build ffmpeg fuse pciutils -y
RUN wget https://github.com/libfuse/libfuse/releases/download/fuse-3.16.2/fuse-3.16.2.tar.gz
RUN tar xvf fuse-3.16.2.tar.gz
RUN cd fuse-3.16.2
RUN mkdir meson-build
RUN cd meson-build
RUN meson setup ../fuse-3.16.2
RUN  ninja install
RUN apt install libgconf-2-4 libatk1.0-0 libatk-bridge2.0-0 libgdk-pixbuf2.0-0 libgtk-3-0 libgbm-dev libnss3-dev libxss-dev libasound2 -y
RUN cd ~
RUN rm -rf fuse-3.16.2
RUN rm fuse-3.16.2.tar.gz

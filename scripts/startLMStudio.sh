set -x
docker compose up -d
if ! [ -e LM_Studio.AppImage ]; then
    wget https://releases.lmstudio.ai/linux/x86/0.2.26/beta/LM_Studio-0.2.26.AppImage
    mv LM_Studio-0.2.26.AppImage LM_Studio.AppImage
    chmod +x LM_Studio.AppImage
fi
./LM_Studio.AppImage &

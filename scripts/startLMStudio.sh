set -x
docker compose up -d
if ! [ -e LM_Studio.AppImage ]; then
    wget https://releases.lmstudio.ai/linux/x86/0.3.5/beta/LM_Studio-0.3.5.AppImage
    mv LM_Studio-0.3.5.AppImage LM_Studio.AppImage
    chmod +x LM_Studio.AppImage
fi
./LM_Studio.AppImage &

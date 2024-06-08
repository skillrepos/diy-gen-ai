if ! [ -e LM_Studio.AppImage ]; then
    wget https://releases.lmstudio.ai/linux/0.2.22/beta/LM_Studio-0.2.22.AppImage
    mv LM_Studio-0.2.22.AppImage LM_Studio.AppImage
    chmod +x LM_Studio.AppImage
fi
./LM_Studio.AppImage &

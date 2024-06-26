docker compose up -d
if ! [ -e LM_Studio.AppImage ]; then
    wget https://releases.lmstudio.ai/linux/x86/0.2.26/beta/LM_Studio-0.2.26.AppImage
    mv LM_Studio-0.2.26.AppImage LM_Studio.AppImage
    chmod +x LM_Studio.AppImage
fi
./LM_Studio.AppImage &
sleep 10
printf '\n======================================================\n'
printf "Your application can now be accessed at \e]8;;https://"$CODESPACE_NAME"-5800.app.github.dev/vnc.html?path=vnc&autoconnect=true&resize=scale&reconnect=true&show_dot=true&bell=false&view_only=false\e\\LM Studio\e]8;;\e"
printf '\n=======================================================\n'

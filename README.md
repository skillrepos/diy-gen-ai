# DIY Gen AI

Repository for LM Studio workshop

These instructions will guide you through configuring a GitHub Codespaces environment that you can use to run the course labs. 
If you prefer to install LM Studio directly, you can get it from https://lmstudio.ai. Note that for Mac, it is only supported on systems with the M# chips. 

If you install it yourself, some elements in the labs may be different for your setup. The instructions here will reference the codespace version.

If you wish to use the codespace environment which will provide you with a running instance of LM Studio, follow the instructions below.

**1. Click on the button below to start a new codespace from this repository.** (You may also fork the repo and create a codespace from your fork if you prefer.)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/skillrepos/diy-gen-ai?quickstart=1)

**2. Then click on the option to create a new codespace.**

![Creating new codespace from button](./images/dga01.png?raw=true "Creating new codespace from button")

This will run for several minutes while it gets everything ready.

**3. After the codespace has initialized there will be a terminal present. Run the command *./setup.sh* in the terminal.**
```
./setup.sh
```
 
![Running setup.sh](./images/dga05.png?raw=true "Running setup.sh")

This will run for several minutes as well.

**4. After setup.sh finishes, run the script *./startLMStudio.sh* in the terminal.**
```
./startLMStudio.sh
```

![Running startlmstudio.sh](./images/dga06.png?raw=true "Running startlmstudio.sh")

This will download the LM Studio image and start it running.

**5. Finally, open up the *labs.md* file so you can follow along with the labs.**
You can either open it in a separate browser instance or open it in the codespace. If you open it in the codespace, make sure to *Open Preview* so you can see it in Markdown form as intended.
![Opening labs](./images/dga07.png?raw=true "Opening labs")

**Now, you are ready for the labs!**

<br/><br/>

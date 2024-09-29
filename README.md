# DIY Gen AI

Repository for workshop with LM Studio, Hugging Face, and Ollama

These instructions will guide you through configuring a GitHub Codespaces environment that you can use to run the course labs. 
If you prefer to install LM Studio directly, you can get it from https://lmstudio.ai. Note that for Mac, it is only supported on systems with the M# chips. 

If you install it yourself, some elements in the labs may be different for your setup. The instructions here will reference running in the codespace environment.

If you wish to use the codespace environment which will provide you with a running instance of LM Studio, follow the instructions below.

**1. Click on the button below to start a new codespace from this repository.**

Click here ➡️  [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/skillrepos/diy-gen-ai?quickstart=1)

**2. Then click on the option to create a new codespace.**

![Creating new codespace from button](./images/dga01.png?raw=true "Creating new codespace from button")

This will run for up to 10 minutes while it gets everything ready.

**IMPORTANT NOTE:** If you get error dialogs that popup about codespace extension version and eventually a dialog like the one below, just click on the *Retry* button to proceed. The codespace will appear to restart but should work after that.

![Bypassing issue](./images/dga70.png?raw=true "Bypassing issue")

NOTE: At the end, after the codespace is actually started, it will still be running some post-startup scripts that will take a few more minutes to complete as shown below:

![Running post-install scripts](./images/dga66.png?raw=true "Running post-install scripts")

The codespace is ready to use when you see a prompt like the one shown below in its terminal.

![Ready to use](./images/dga67.png?raw=true "Ready to use")


**3. Open up the *labs.md* file so you can follow along with the labs.**
You can either open it in a separate browser instance or open it in the codespace. If you open it in the codespace, make sure to *Open Preview* so you can see it in Markdown form as intended.
![Opening labs](./images/dga07.png?raw=true "Opening labs")

**Now, you are ready for the labs!**

**4. (Optional, but recommended) Change your codespace's default timeout from 30 minutes to longer (60 for half-day sessions, 90 for deep dive sessions).**
To do this, when logged in to GitHub, go to https://github.com/settings/codespaces and scroll down on that page until you see the *Default idle timeout* section. Adjust the value as desired.

![Changing codespace idle timeout value](./images/dga56.png?raw=true "Changing codespace idle timeout value")

**NOTE: If your codespace times out and you need to reopen it**

1. Go to https://github.com/<your github userid>/codespaces
2. Find the codespace in the list, right-click, and select *Open in browser*
3. After the codespace opens up, run the script *./scripts/startLMStudio.sh* in the terminal. (You might need to run this more than once if restarting a codespace depending on timing.)
```
./scripts/startLMStudio.sh
```

![Running startlmstudio.sh](./images/dga06.png?raw=true "Running startlmstudio.sh")


<br/><br/>

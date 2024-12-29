# DIY Gen AI
## Setting up your own LLM host, chat, and AI server using LM Studio - half-day workshop
## Session labs 
## Revision 2.2 - 12/29/24

**Follow the startup instructions in the README.md file IF NOT ALREADY DONE!**

**NOTE 1: To copy and paste in the codespace, you may need to use keyboard commands - CTRL-C and CTRL-V.**

**NOTE 2: You may see periodic "Reconnecting" messages pop up. This is normal and they will go away shortly.**

**NOTE 3: To get a closer view of the LM Studio App, you can click on the *View* menu at the top and then click on *Zoom In*.**

![Zooming in](./images/dga72.png?raw=true "Zooming in")

**NOTE 4: To do some of the later steps in Lab 4, you will need to have a Hugging Face account. You can sign up for a free one at [huggingface/join](https://huggingface.co/join).**

</br></br>

**Lab 1 - Getting familiar with LM Studio and models**

**Purpose: In this lab, we’ll start to learn about models through working with one in LM Studio.**

1. In the Codespace's terminal, run the script *./getlink.sh*. This will output a link that you can click on to get to the LM Studio instance. Use *Ctrl/Cmd+Click* to open the browser session. 

![Getting to LM Studio](./images/dga08b.png?raw=true "Getting to LM Studio") 

</br></br>
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NOTE: Alternate method to get to LM Studio (only need to use if having trouble with above - otherwise, go to Step 2):*

*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Click on the *PORTS* tab (next to *TERMINAL*) in the lower part of the codespace screen. Hover the mouse over the *globe* icon and click on it to open up a new browser tab running noVNC.* 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Getting to LM Studio](./images/dga58.png?raw=true "Getting to LM Studio")

*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Then click on the *Connect* button.*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![Getting to LM Studio](./images/dga59.png?raw=true "Getting to LM Studio")

</br></br>

2. After that, you should see the running instance of LM Studio with a suggestion to load a model. We'll skip this intro part. Just click the *Skip onboarding -->* button in the upper right.

![LM Studio instance](./images/dga73.png?raw=true "LM Studio instance")   

3. Now we're going to search using LM Studio for a particular set of models - ones matching *llama*. Click on the search bar at the top (box that says *Select a model to load*) and enter in *llama* in the new search box that pops up. Then click on the button that says *Search more results for "llama"*.
```
llama
```

![llama search](./images/dga74.png?raw=true "llama search")   

4. After the search is run, you'll see a list of *llama* models displayed on the left and additional information about them displayed on the right. You can click on a model in the list and then scroll and click in the right-hand side to see more details about it.

![llama model info](./images/dga75.png?raw=true "llama model info")  

5. Now, let's actually download one of the models. In the top search field, enter *llama-2-7B-Chat-GGUF*.

![finding the model](./images/dga76.png?raw=true "finding the model")   
  
6. On the right side, click the *Q4_0* button in the gray bar and select the row for *Q3_K_M*. 

![picking the version](./images/dga77.png?raw=true "picking the version") 

7. Click on the green button in the lower right to download the selected model. After that, you'll see a popup dialog showing download progress.

![downloading the model](./images/dga78.png?raw=true "downloading the model")
![download progress](./images/dga79.png?raw=true "download progress")

8. Due to an issue with LM Studio, we can't load the model directly through the *Load model* buttons on the screen, so you can close the download dialogs and the *Mission Control* dialogs after the download is complete.

![close dialogs](./images/dga80.png?raw=true "close dialogs")

9. Now let's take a look at the model we downloaded on the community site https://huggingface.co/models. Open that link in a separate tab and you'll see some of the different types of models and various models available for download and use.
![huggingface](./images/dga18.png?raw=true "huggingface")

10. In the search bar on https://huggingface.co/models, enter enough of the name of the model *llama-2-chat-gguf* and select the page for the model *TheBloke/Llama-2-7B-Chat-GGUF*.

![finding the model repo](./images/dga81.png?raw=true "finding the model repo")

11. You'll now be on the *model card* page for *TheBloke/Llama-2-7B-Chat-GGUF* repository. You can scroll down and find additional details, directions for use, example uses, etc. about the models in this repository.

![exploring the model repo](./images/dga20a.png?raw=true "exploring the model repo")

12. You can also take a look at the *Files and versions* page.
    
![exploring the model repo](./images/dga21a.png?raw=true "exploring the model repo")

<p align="center">
**[END OF LAB]**
</p>
</br></br>

**Lab 2 - Chatting with our model**

**Purpose: In this lab, we'll see how to load and interact with the model through chat and terminal.**

1. First, let's switch back to the browser tab where LM Studio is running. If not already selected, click the *chat bubble* (yellow/orange) icon at the top left to get to the *AI Chat* interface in LM Studio.
   
![Switching to chat](./images/dga82.png?raw=true "Switching to chat")

2. Now, at the top center of the *AI Chat* screen, click on the down arrow next to the *Select a model to load* text and select the *llama* model we downloaded.
   
![Select model 1](./images/dga83.png?raw=true "Select model 1")
![Select model 2](./images/dga84.png?raw=true "Select model 2")
  
3. Due to an issue with LM Studio, we need to do one more step before loading. After you've clicked on the model to select it, you should see a dialog with some load options. Click on the *Context Length* select and drag it to the left to back it off from the max. (It doesn't seem to matter how much.) Then click on the *Load Model* button at the bottom right.

![extra step](./images/dga85.png?raw=true "Extra step")

4. You should see a progress bar in the top *load* area while the model is loading and then the model should be available. You'll also be able to see the system resources now used by the loaded model in the bottom right.
![loaded model](./images/dga86.png?raw=true "Loaded model")

5. Let's look at the different chat settings available. Click the *Settings* icon in the upper right (looks like a beaker). You can expand the various sub-areas and expand them to see the options. Before you go to the next step, change the *System Prompt* field to be:
```
You are an excellent summarizer. Always answer with 3 key points.
```
![opening settings](./images/dga87.png?raw=true "opening settings")
![setting system prompt](./images/dga88.png?raw=true "setting system prompt")

5. Now, let's give our loaded model a query. In the *USER* text entry area, enter your query. (An example one is shown, but you can choose your own.) Hit Enter or *Send* after inputting the query.
   
![User query](./images/dga89.png?raw=true "User query")

6. This will take a while to run given the limitations of our codespace system. Example output from the sample query is shown below. There are a number of follow-up options available under the output. For example, if you don't like the answer, you can click the *Regenerate* button to get another answer.
![output from AI](./images/dga90.png?raw=true "output from AI")

7. Now, let's have LM Studio run a local server for this model. In the lefthand bar, select the green *terminal* icon to switch to *Developer* mode.
   
![Switching to developer](./images/dga91.png?raw=true "Switching to chat")

8. You should now be on the *Local Server* screen (highlighted in top row)., click on the green *Start* button in the *Server status* section on the upper left. Afterwards, you should see activity showing the server is running.
![Starting server](./images/dga92.png?raw=true "Starting server")
![Server running](./images/dga93.png?raw=true "Server running")

9. Now, switch back to your codespace and go to a terminal. (You can add a 2nd terminal if you want via the "+" icon over in the far right of the same line as TERMINAL. Or you can right-click and select New Terminal* or *Split Terminal*.) In the terminal's command line, let's check to see which model(s) are loaded in LM Studio. You can use the following command.
```
curl http://localhost:1234/v1/models
```

10. Finally, let's try a simple query with curl. Try the query below.
```
curl http://localhost:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{ 
    "messages": [ 
      { "role": "system", "content": "Always answer in rhymes." },
      { "role": "user", "content": "Introduce yourself." }
    ], 
    "temperature": 0.7, 
    "max_tokens": -1,
    "stream": true
}'
```
![streamed output](./images/dga94.png?raw=true "streamed output")


11. To see the output in a more readable format, set the *stream* value to *false* and run the command again.
```
curl http://localhost:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{ 
    "messages": [ 
      { "role": "system", "content": "Always answer in rhymes." },
      { "role": "user", "content": "Introduce yourself." }
    ], 
    "temperature": 0.7, 
    "max_tokens": -1,
    "stream": false
}'
```
![unstreamed output](./images/dga95.png?raw=true "unstreamed output")    

<p align="center">
**[END OF LAB]**
</p>
</br></br>

**Lab 3 - Coding to LM Studio**

**Purpose: In this lab, we'll see how to do some simple Python and JavaScript code to interact with the model.**

1. While we got output from the last step of lab 2, it wasn't very useful in that form. Let's use the pre-configured python environment to do some simple coding in. 

2. Now, let's create a new file called *simple-app.py* to put our code in.
```
code simple-app.py
```

3. Enter the code below in the *simple-app.py* file and then save when done. (Again, you can change the *content* strings to whatever you want.)
```
from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="n-a")

completion = client.chat.completions.create(
    model="local-model",
    messages=[
        {"role": "system", "content": "Always answer in rhymes."},
        {"role": "user", "content": "Introduce yourself."}
    ],
    temperature=0.7,
)

print(completion.choices[0].message.content)
```
![Saving file](./images/dga60.png?raw=true "Saving file")

4. Now, run the program to see the output.
```
python simple-app.py
```
![output of run](./images/dga61.png?raw=true "Output of run")

5. Let's see what effect changing the temperature value has. Change the value for temperature in the program to 2.0 and then run the program again. (You can also change the prompt if you want. In this example, I changed it to "How do I build a house?"). Make sure to save your changes before running!

![output of run with temp = 2](./images/dga63.png?raw=true "Output of run with temp = 2")

6. Next, we'll switch to doing a simple example in JavaScript for LM Studio. First, switch to a new terminal by using one of the methods mentioned previously.

7. We need to *bootstrap* things for LM Studio by setting up the *lms* command line tool. Run the following command in the terminal.
```
~/.cache/lm-studio/bin/lms bootstrap
```
![bootstrapping lms](./images/dga32.png?raw=true "bootstrapping lms")

8. Rerun your profile file and make sure that *lms* runs there.
```
source /home/vscode/.profile
lms
```
![checking lms](./images/dga33.png?raw=true "checking lms")

9. Use the *lms* command to create a new empty project, run through it's interactive process, and then switch to it. You can pick whatever project name you want instead of the default. In the sample output below, we used "*my-proj*".
```
lms create node-javascript-empty
cd <project-name>
```
![creating new lms project](./images/dga65.png?raw=true "Creating new lms project")

10. Now, you can replace the code in your *src/index.js* file with the code below. You can open the file from the terminal via the first command below. Then **copy the code below and paste it into the file, overwriting the previous contents.** (You can change the system and/or user *role* and *content* if you want.) Be sure to save your changes before running.

```
code src/index.js
```
</br>
    
```
// index.js
import { LMStudioClient } from "@lmstudio/sdk";

async function main() {
  // Create a client to connect to LM Studio, then load a model
  const client = new LMStudioClient();
  let model; 
  // Don't load another instance of the model if there's one already loaded
  const loadedModels = await client.llm.listLoaded();
  if (loadedModels.length === 0) {
      model = await client.llm.load("llama-2-7b-chat", {
      config: { 
        contextLength: 2048,
      },
    });
  }
  else {
    model = await client.llm.get({ identifier: loadedModels[0].identifier });
  }

  // Predict!
  const prediction = model.respond([
    { role: "system", content: "You are a helpful AI assistant." },
    { role: "user", content: "What is some good advice?" },
  ]);
  for await (const text of prediction) {
    process.stdout.write(text);
  }
}

main();
```

![adding code](./images/dga97.png?raw=true "adding code")

11. As a final prep step, install a version of the sdk that is compatible with our version of LM Studio by entering the command below.
```
npm i @lmstudio/sdk@0.3.0
```

12. Save your changes if you haven't and then let's run the code! The screenshot further down shows some example output.
```
npm  start
```

![running code](./images/dga96.png?raw=true "running code")

<p align="center">
**[END OF LAB]**
</p>
</br></br>

**Lab 4 - Working with models in Hugging Face**

**Purpose: In this lab, we’ll see how to get more information about, and work directly with, models in Hugging Face.**

1. In a browser, go to *https://huggingface.co/models*.

2. Let's search for another simple model to try out. In the search bar, enter the text *DialoGPT*. Look for and select the *microsoft/DialoGPT-medium* model.
  ![model search](./images/dga44.png?raw=true "model search")

3. Let's see how we can quickly get up and running with this model. On the *Model Card* page for the *microsoft/DialoGPT-medium* model, if you scroll down, you'll see a *How to use* section with some code in it. Highlight that code and copy it so we can paste it in a file in our workspace.

![code to use model](./images/dga45.png?raw=true "code to use model")
   
4. Switch back to your codespace and the *diy-gen-ai* directory (if not there). Create a new file named dgpt-med.py (or whatever you want to call it). Paste the code you copied from the model card page into the file. You can create the new file from the terminal using:

```
code dgpt-med.py
```
![adding code](./images/dga46.png?raw=true "adding code")

5. Don't forget to save your file. Now you can run your file by invoking it with python. You'll see it start to download the files associated with the model. This will take a bit of time to run.
```
python dgpt-med.py
```
![running the model](./images/dga47.png?raw=true "running the model")

6. After the model loads, you'll see a *>> User:* prompt. You can enter a prompt or question here, and after some time, the model will provide a response.  **NOTE** This model is small and old and does not provide good responses usually or even ones that make sense. We are using it as a simple, quick demo only.

```
>> User: <prompt here>
```
![running the model](./images/dga48.png?raw=true "running the model")

7. Let's now switch to a different model. Go back to the Hugging Face search and look for *phi3.5*. Find and select the entry for *microsoft/Phi-3.5-mini-instruct*.

![finding the phi3-vision model](./images/dga98.png?raw=true "finding the phi3-vision model")

8. Switch to the *Files and versions* page to see the sizes of the files in the Git repository. Note the larger sizes of the model files themselves.
![examining the model files](./images/dga99.png?raw=true "examining the model files")

9. If you want to try the remaining steps, you will need a Hugging Face userid. To sign up for a free one, go to [huggingface/join](https://huggingface.co/join).

10. Now, let's see how we can try this model out with no setup on our part. Go back to the *Model card* tab, and on the right-hand side, you should see an *Inference API* section. In the prompt area, you can enter a prompt and hit *Send* to see the model's response.
![Invoking model on Azure AI Studio](./images/dga100.png?raw=true "Invoking the model on Azure AI Studio")

11. If you want, you can also try the *vision* version of this model by selecting the *vision-instruct* link to the right and prompt it to describe a link to an image or attach an image. An example prompt is included below. (Note that this does not always work as sometimes the model may timeout trying to load.)
```
Describe the image at https://media.istockphoto.com/id/1364253107/photo/dog-and-cat-as-best-friends-looking-out-the-window-together.jpg?s=2048x2048&w=is&k=20&c=Do171m5e2DbPIlWDs1JfHn-g8Et_Hxb2AskHg4cRYY4=
```
![Describing an image](./images/dga101.png?raw=true "Describing an image")

<p align="center">
**[END OF LAB]**
</p>
</br></br>

**Lab 5 - Using Ollama to run models locally**

**Purpose: In this lab, we’ll start getting familiar with Ollama, another way to run models locally.**

1. First, to get *ollama* downloaded, execute the command below. Then you can run the actual application to see usage.
```
curl -fsSL https://ollama.com/install.sh | sh
```
![downloading ollama](./images/dga36.png?raw=true "downloading ollama")

2. Next, start the ollama server running with the following command:
```
ollama serve &
```
![downloading ollama](./images/dga37.png?raw=true "downloading ollama")

3. Now let's find a model to use.
Go to https://ollama.com and in the *Search models* box at the top, enter *llava*.
![searching for llava](./images/dga39.png?raw=true "searching for llava")

4. Click on the first entry to go to the specific page about this model. Scroll down and scan the various information available about this model.
![reading about llava](./images/dga40a.png?raw=true "reading about llava")

5. Switch back to a terminal in your codespace. While it's not necessary to do as a separate step, first pull the model down with ollama. (This will take a few minutes.)
```
ollama pull llava
```
6. Now you can run it with the command below.
```
ollama run llava
```
7. Now you can query the model by inputting text at the *>>>Send a message (/? for help)* prompt. Since this is a multimodal model, you can ask it about an image too. Try the following prompt that references a smiley face file in the repo.
```
What's in this image?  /workspaces/diy-gen-ai/images/smiley.jpg
```
![smiley face analysis](./images/dga69.png?raw=true "Smiley face analysis")

8. Now, let's try a call with the API. You can stop the current run with a Ctrl-D or switch to another terminal. Then put in the command below. 
```
curl http://localhost:11434/api/generate -d '{
  "model": "llava",
  "prompt": "What causes wind?",
  "stream": false
}'
```

9. This will take a minute or so to run. You should a single response object returned. You can try out some other prompts/queries if you want.

<p align="center">
**[END OF LAB]**
</p>
</br></br>

**Lab 6 - Building a chatbot with Streamlit**

**Purpose: In this lab, we'll see how to use the Streamlit application to create a simple chatbot with Ollama.**

1. Let's get another model to work with - a small one. Pull the *Phi3 mini* model with Ollama.
```
ollama pull phi3:mini
```

2. Create a new file for the chatbot app.
```
code chatapp.py
```

3. In the chatapp.py file, add the initial imports we need for streamlit and ollama
```
import streamlit as st
# import ollama wrapper
import ollama
```

4. Now, we set the title and initialize the session messages. (You can change the title and "content" sections if you want.)
```
st.title("DIY Gen AI Chatbot")
# check messages variable in streamlit's session state
if "messages" not in st.session_state:
      # if no value set, (we're just starting out) then initialize with friendly message
      # role is either "user" or "assistant"
      st.session_state["messages"] = [ {"role":  "assistant",  "content":  "What can I help you with?"}]
```
5. Add code to write the msg history
```
# Write msg history
for msg in st.session_state.messages:
       st.chat_message(msg["role"]).write(msg["content"])
```

6. Now, add the generator function for responses
```
# Generator for streaming tokens
def generate_response():
        # call chat function in ollama, get response from the loaded model
        response = ollama.chat(model='phi3:mini', stream=True, messages=st.session_state.messages)
        for partial_resp in response:
               token = partial_resp["message"]["content"]
               # maintain history/context
               st.session_state["full_message"] += token
               yield token
```

7. Finally, add the code to save the messages and call the generator function

```
if prompt := st.chat_input():
      # save the message for the user role
      st.session_state.messages.append({"role": "user", "content": prompt})
      st.chat_message("user").write(prompt)
      st.session_state["full_message"] = ""
      # call the generate_response function above
      st.chat_message("assistant").write_stream(generate_response)
      # save the message for the assistant role
      st.session_state.messages.append({"role": "assistant", "content": st.session_state["full_message"]})
```

8. Now, save your file and run it with the following command. (You can just ignore the email field.)
```
streamlit run chatapp.py
```

9. After a moment this should open up a browser session with your chatbot running. You can ask it a question or prompt it as you want.
![interacting with chatbot](./images/dga50.png?raw=true "interacting with chatbot")

10. One other thing you can try if you want is having it generate code or translate code. Notice that it has a "memory" between questions for context.
![interacting with chatbot](./images/dga51.png?raw=true "interacting with chatbot")
![interacting with chatbot](./images/dga52.png?raw=true "interacting with chatbot")


<p align="center">
**[END OF LAB]**
</p>

<p align="center">
**THANKS!**
</p>

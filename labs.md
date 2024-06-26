# DIY Gen AI
## Setting up your own LLM host, chat, and AI server using LM Studio - half-day workshop
## Session labs 
## Revision 1.2 - 07/01/24

**Follow the startup instructions in the README.md file IF NOT ALREADY DONE!**

**NOTE: To copy and paste in the codespace, you may need to use keyboard commands - CTRL-C and CTRL-V.**

**NOTE: You may see periodic "Reconnecting" messages pop up. This is normal and they will go away shortly.**

**NOTE: To get a closer view of the LM Studio App, you can click on the *View* menu at the top and then click on *Zoom In*.**
![Zooming in](./images/dga42.png?raw=true "Zooming in")

**Lab 1 - Getting familiar with LM Studio and models**

**Purpose: In this lab, we’ll start to learn about models through working with one in LM Studio.**

1. In the Codespace's terminal, run the script *./getlink.sh*. This will output a link that you can click on to get to the LM Studio instance. Use *Ctrl/Cmd+Click* to open the browser session. 
 
![Getting to LM Studio](./images/dga08a.png?raw=true "Getting to LM Studio")

2. After that, you should see the running instance of LM Studio. You'll probably be at the *Release Notes* screen. Just click the *Close* button.

![LM Studio instance](./images/dga41.png?raw=true "LM Studio instance")   

3. Scroll around the home page of the app to see the examples of recent models featured there. When done, just scroll back up to the top.

![LM Studio models on home page](./images/dga10.png?raw=true "LM Studio models on home page")


4. Now we're going to search using LM Studio for a particular model - *llama*. Enter *llama* into the search bar and then click the *Go* button.
```
llama
```

![llama search](./images/dga11a.png?raw=true "llama search")   

5. After the search is run, you'll see a list of *llama* models displayed on the left and different versions of them displayed on the right. You can hover over some of the items like the *Q* identifiers in the items on the right to get more info.

![llama model info](./images/dga12a.png?raw=true "llama model info")  

6. LM Studio also displays some information to help you decide about which model version to use. There's an expandable section near the bottom under *Learn more*. Click to expand that and you read more about the differences in quantization level.

![Learning more](./images/dga13a.png?raw=true "Learning more")  

7. You can also expand the README about the model to get more details about it's attributes, license, etc. To do that, click on the expand button in the row for *README.md* and scroll through its contents.

![Viewing the README](./images/dga15a.png?raw=true "Viewing the README") 

8. Now, let's actually download one of the models. Back in the list, collapse the expanded *README* and *Learn more* sections. In the left column, select the row for the *TheBloke/Llama-2-7B-Chat-GGUF* file. In the right column, select the row for the *llama-2-7b-chat.Q3_K_M.gguf* file and click the *Download* button. You'll see a progress bar at the bottom of the screen and an indication in the row when it is completely downloaded.

![Downloading the model](./images/dga16.png?raw=true "Downloading the model") 
![Downloaded the model](./images/dga17.png?raw=true "Downloaded the model")

9. Now let's take a look at the model we downloaded on the community site https://huggingface.co/models. Open that link in a separate tab and you'll see some of the different types of models and various models available for download and use.
![huggingface](./images/dga18.png?raw=true "huggingface")

10. In the search bar on https://huggingface.co/models, enter enough of the name of the model *thebloke/llama-2-* and select the page for the model *TheBloke/Llama-2-7B-Chat-GGUF*.

![finding the model repo](./images/dga19a.png?raw=true "finding the model repo")

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

1. First, let's switch to the *AI Chat* interface in LM Studio by clicking on the third icon from the top in the left bar.
![Switching to chat](./images/dga22.png?raw=true "Switching to chat")

2. Now, at the top center of the *AI Chat* screen, click on the down arrow next to the *Select a model to load* text and select the phi2 model we downloaded.
![Switching to chat](./images/dga23a.png?raw=true "Switching to chat")
  
3. You should see a progress bar while the model is loading and then the model should show up as loaded. (If a dialog box comes up about the System Prompt, you can just choose to accept the new one.)
![Switching to chat](./images/dga24.png?raw=true "Switching to chat")
![Switching to chat](./images/dga25a.png?raw=true "Switching to chat")

4. Over in the right-hand side window, you can explore the different options. Change the *System Prompt* field to be:
```
You are an excellent summarizer. Always answer with 3 key points.
```
![Switching to chat](./images/dga26a.png?raw=true "Switching to chat")

6. Now, let's give our loaded model a query. In the *USER* text entry area, enter your query. (An example one is shown, but you can choose your own.)
![User query](./images/dga27a.png?raw=true "User query")

7. Example output from the sample query is shown below. Note that if you don't like the answer, you can click the *Regenerate* button to get another answer.
![Switching to chat](./images/dga28b.png?raw=true "Switching to chat")

8. Now, let's have LM Studio run a local server for this model. In the lefthand bar, select the next to bottom icon for the *Local Server* screen.
![Switching to chat](./images/dga29.png?raw=true "Switching to chat")

9. On the *Local Server* screen, click on the green *Start Server* button on the left side.
![Switching to chat](./images/dga30a.png?raw=true "Switching to chat")

10. Now, back in the command line, let's check to see which model(s) are loaded in LM Studio. You can use the following command.
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

<p align="center">
**[END OF LAB]**
</p>
</br></br>

**Lab 3 - Coding to LM Studio**

**Purpose: In this lab, we'll see how to do some simple Python and Javascript code to interact with the model.**

1. While we got output from the last step of lab 2, it wasn't very useful in that form. Let's setup a Python environment to do some simple coding in. Run the commands below to set things up.
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Now, let's create a new file called *simple-app.py* to put our code in.
```
code simple-app.py
```

3. Enter the code below in the *simple-app.py* file and then save when done. (Again, you can change the content to whatever you want.)
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
}

print(completion.choices[0].message.content)
```

4. Now, run the program to see the output.
```
python simple-app.py
```
TO-DO: insert example here of changing temperature of model to see response...

5. Next, we'll switch to doing a simple example in JavaScript for LM Studio. First, switch to a new terminal by clicking the "+" button at the top right to add a second terminal.


6. We need to *bootstrap* things for LM Studio by setting up the *lms* command line tool. Run the following command in the terminal.
```
~/.cache/lm-studio/bin/lms bootstrap
```
![bootstrapping lms](./images/dga32.png?raw=true "bootstrapping lms")

7. Rerun your profile file and make sure that *lms* runs there.
```
source /home/vscode/.profile
lms
```
![checking lms](./images/dga33.png?raw=true "checking lms")

8. Use the *lms* command to create a new empty project, run through it's interactive process, and then switch to it.
```
lms create node-javascript-empty
cd <project-name>
```

9. Now, you can enter code like the following in your *src/index.js* file. (You can change the content if you want.)
```
// index.js
const { LMStudioClient } = require("@lmstudio/sdk");

async function main() {
  // Create a client to connect to LM Studio, then load a model
  const client = new LMStudioClient();
  const model = await client.llm.load("theBloke/phi-2.Q2_K.gguf");

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

10. Finally, let's run the code!
```
npm  start
```
<p align="center">
**[END OF LAB]**
</p>
</br></br>

**Lab 4 - Using Ollama to run models locally**

**Purpose: In this lab, we’ll start getting familiar with Ollama, another way to run models locally.**

1. First, to get *ollama* downloaded, execute the following command:
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
![reading about llava](./images/dga40.png?raw=true "reading about llava")

5. While it's not necessary to do as a separate step, first pull the model down with ollama and then run it.
```
ollama pull llava
ollama run llava
```
6. Now you can query the model. Since this is a multimodal model, you can ask it about an image too. Try the following prompt.
```
What's in this image?  images/simple-face.jpg
```
7. Now, let's try that with the API.
```
curl http://localhost:11434/api/generate -d '{
  "model": "llava",
  "prompt":"What's in this picture?",
  "images" : "'"$( base64 images/simple-face.jpg)"'"
}'
```

8. You should get a similar answer as before. You can try out some other prompts/queries if you want.

<p align="center">
**[END OF LAB]**
</p>
</br></br>

**Lab 5 - Building a chatbot with Streamlit**

**Purpose: In this lab, we'll see how to use the streamlit application to create a simple chatbot with Ollama.**

1. Switch back to the terminal that has your virtual Python environment running in it.

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

4. Now, we can set the title and initialize the session messages if we're starting out. (You can change the title and "content" sections if you want.)
```
st.title("DIY Gen AI Chatbot")
# check messages variable in streamlit's session state
if "messages" not in st.session_state:
      # if no value set, (we're just starting out) then initialize with friendly message
      # role is either "user" or "assistant"
      st.session_state["messages"] = [ {"role":  "assistant",  "content":  "What can I help you with?"}]
```

5. Now, add the generator function for responses
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

6. Finally, add the code to save the messages and call the generator function

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

7. Now, save your file and run it with the following command.
```
streamlit run chatapp.py
```

8. After a moment this should open up a browser session with your chatbot running. You can ask it a question or prompt it as you want.
![interacting with chatbot](./images/dga50.png?raw=true "interacting with chatbot")

9. One other thing you can try if you want is having it generate code or translate code. Notice that it has a "memory" between questions for context.
![interacting with chatbot](./images/dga51.png?raw=true "interacting with chatbot")
![interacting with chatbot](./images/dga52.png?raw=true "interacting with chatbot")


<p align="center">
**[END OF LAB]**
</p>

<p align="center">
**THANKS!**
</p>

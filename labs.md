# DIY Gen AI
## Setting up your own LLM host, chat, and AI server using LM Studio - half-day workshop
## Session labs 
## Revision 1.1 - 06/08/24

**Follow the startup instructions in the README.md file IF NOT ALREADY DONE!**

**NOTE: To copy and paste in the codespace, you may need to use keyboard commands - CTRL-C and CTRL-V.**

**Lab 1 - Getting familiar with LM Studio and models**

**Purpose: In this lab, we’ll start to learn about models through working with one in LM Studio.**

1. In your codespace, in the panels at the bottom, find the *PORTS* panel (next to the *TERMINAL* one) and click on that to open the ports list. Then in the line for *port 5800*, under the *Forwarded Address* column, click on the icon that looks like a globe.
 

![Getting to LM Studio](./images/dga08.png?raw=true "Getting to LM Studio")

2. This will open up a new browser tab that is connected to the running LMStudio app. To host this as a graphical app in the codespace, we're using a trick with a tool called *noVNC*. Click on the *Connect* button.

![Click through noVNC](./images/dga09.png?raw=true "Click through noVNC")   

3. After that, you should see the running instance of LM Studio. You'll probably be at the *Release Notes* screen. Just click the *Close* button.

![LM Studio instance](./images/dga10.png?raw=true "LM Studio instance")   

4. Now we're going to search using LM Studio for a particular model - *Phi 2*. Enter *Phi 2* into the search bar and then click the *Go* button.
```
Phi 2
```

![Phi 2 search](./images/dga11.png?raw=true "Phi 2 search")   


5. After the search is run, you'll see a list of *Phi 2* models displayed on the right. You can hover over some of the items like the *Q* identifiers to get more info.

![Phi 2 model info](./images/dga12.png?raw=true "Phi 2 model info")  

6. LM Studio also displays some information to help you decide about which model version to use. There's an expandable section near the bottom under *Learn more*. Click to expand that and you read more about the differences.

![Learning more](./images/dga13.png?raw=true "Learning more")  

![Learning more](./images/dga14.png?raw=true "Learning more") 

7. You can also expand the README about the model to get more details about it's attributes, license, etc. To do that, click on the expand button in the row for *README.md* and scroll through its contents.

![Viewing the README](./images/dga15.png?raw=true "Viewing the README") 

8. Now, let's actually download one of the models. Back in the list, selet the row for the *phi-2.Q3_K_S.gguf* file and click the *Download* button. You'll see a progress bar at the bottom of the screen and an indication in the row when it is completely downloaded.

![Downloading the model](./images/dga16.png?raw=true "Downloading the model") 
![Downloaded the model](./images/dga17.png?raw=true "Downloaded the model")

9. Now let's take a look at the model we downloaded on the community site https://huggingface.co/models. Open that link in a separate tab and you'll see some of the different types of models and various models available for download and use.
![huggingface](./images/dga18.png?raw=true "huggingface")

10. In the search bar on https://huggingface.co/models, enter the name of the model repo that has our model in it *phi-2-GGUF*. Then, in the filtered results list, click on the entry for *TheBloke/phi-2-GGUF*.

![finding the model repo](./images/dga19.png?raw=true "finding the model repo")

11. You'll now be on the page for *TheBloke/phi-2-GGUF* repository. You can scroll down and find additional details, directions for use, example uses, etc. about the models in this repository.

![exploring the model repo](./images/dga20.png?raw=true "exploring the model repo")
![exploring the model repo](./images/dga21.png?raw=true "exploring the model repo")

<p align="center">
**[END OF LAB]**
</p>
</br></br>

**Lab 2 - Chatting with our model**

**Purpose: In this lab, we'll see how to load and interact with the model through chat and terminal.**

1. First, let's switch to the *AI Chat* interface in LM Studio by clicking on the third icon from the top in the left bar.
![Switching to chat](./images/dga22.png?raw=true "Switching to chat")

2. Now, at the top center of the *AI Chat* screen, click on the down arrow next to the *Select a model to load* text and select the phi2 model we downloaded.
![Switching to chat](./images/dga23.png?raw=true "Switching to chat")
  
3. You should see a progress bar while the model is loading and then the model should show up as loaded.
![Switching to chat](./images/dga24.png?raw=true "Switching to chat")
![Switching to chat](./images/dga25.png?raw=true "Switching to chat")

4. You can explore some of the options over in the right-hand side window. You don't have to change anything here.
![Switching to chat](./images/dga26.png?raw=true "Switching to chat")

5. Now, let's give our loaded model a query. In the *USER* text entry area, enter your query. (An example one is shown, but you can choose your own.)
![Switching to chat](./images/dga27.png?raw=true "Switching to chat")

6. Example output from the sample query is shown below. Note that if you don't like the answer, you can click the *Regenerate* button to get another answer.
![Switching to chat](./images/dga28.png?raw=true "Switching to chat")

7. Now, let's have LM Studio run a local server for this model. In the lefthand bar, select the next to bottom icon for the *Local Server* screen.
![Switching to chat](./images/dga29.png?raw=true "Switching to chat")

8. On the *Local Server* screen, click on the green *Start Server* button on the left side.
![Switching to chat](./images/dga30.png?raw=true "Switching to chat")

9. Now, back in the command line, let's check to see which model(s) are loaded in LM Studio. You can use the following command.
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



3. Leave the cursor at the end of the line.

![starting point](./images/cdd104.png?raw=true "starting point") 

4.

5. Pick one of the options that is longer and/or more complex (if there is one) and **Accept suggestion #**. If there's not one that's longer/more complex, just pick an alternative one and **Accept suggestion #**.

![alternative suggestions](./images/cdd34b.png?raw=true "alternative suggestions") 

6. Highlight the code and select the Chat extension icon to open the chat window.  Tell Copilot to simplify the code by typing in the chat window.
```
/simplify
```

![simplifying via chat box](./images/cdd35.png?raw=true "simplifying via chat box") 

7. Hover over the simplified text and tell Copilot to insert the suggestion at the cursor to replace the text that's currently there.

![replace from chat suggestion](./images/cdd36b.png?raw=true "replace from chat suggestion")    

8. Now, let's introduce an error into the code to see how Copilot can fix it. Pick an instance of a variable name and change it to one that doesn't exist. For example, change an instance of "n" to "x". 

![introduce error](./images/cdd37b.png?raw=true "introduce error")   

9. Notice the light bulb icon that has popped up. Click on that, scroll to the bottom (if needed), and you'll have additional options to fix or explain with Copilot.

![Copilot options inline](./images/cdd38b.png?raw=true "Copilot options inline")   

10. Go ahead and click on the "Fix using Copilot" option.

11. After a few moments, it will propose a fix that you can just accept (via the Accept button). You can also click on the *Show Changes* icon to see before/after for the proposed changes.

![Fixing with Copilot](./images/cdd107a.png?raw=true "Fixing with Copilot")       

12. (Optional) If you'd like, you can go back and make the error again, highlight the code, and then use the /fix command in the chat window to get the same results.

<p align="center">
**[END OF LAB]**
</p>

**Lab 3 - Using Copilot after the coding**

**Purpose: In this lab, we’ll see a few other ways to leverage Copilot after the initial coding is done**

1. Now that we have some code to work with, let's see what else Copilot can do for us. Let's have it explain the current code in our *prime.py* file.  Select the code. Then, use the **Cmd+I** keys to bring up the Copilot interactive chat dialog.

![Interactively telling Copilot to explain code](./images/cdd40b.png?raw=true "Interactively telling Copilot to explain code")


2. Tell Copilot to explain the code by typing the command below in the dialog. Hit Enter. Then, you should see the output in the chat window.

```
/explain
```
![Output of interactively telling Copilot to explain code](./images/cdd41b.png?raw=true "Output of interactively telling Copilot to explain code")

3. Now, let's do the same request but through a comment. In the *prime.py* file, below the code, enter the following comment and hit Enter.
```
# explain the code above line-by-line
```
4. After this, Copilot should start showing the explanation in comments. Just hit tab to accept each line and then Enter to move to the next one.

![Output of telling Copilot to explain code via comment](./images/cdd42b.png?raw=true "Output of telling Copilot to explain code via comment")

5. We can also query Copilot inline via asking a question in a comment. Delete the commented explanation and try out the question below. To be clear you can prefix it with :q but that is not required with the chat feature installed.

```
# q: what does the function above do?
```

![Prompting for what code does with q:](./images/cdd43b.png?raw=true "Prompting for what code does with q:")

6. Finally, let's see how to use the doc feature to automatically document our code. Highlight the actual code.

7. Now, enter **Cmd+I** and enter the **/doc** command. After a few moments, Copilot should generate some documentation for the code. You can go ahead and *Accept* the changes.

![Generated doc for the code](./images/cdd44d.png?raw=true "Generated doc for the code")  

8. While this is useful documentation for the start of the function, we'd like to have more extensive comments in the function body. So,let's get Copilot's help with that. Bring up the chat dialog again with **Cmd+I** and enter the text "verbosely comment this code". After Copilot completes its suggestions, if you're happy with them, you can just click *Accept*. 

![Regenerating doc](./images/cdd110.png?raw=true "Regenerating doc")  

<p align="center">
**[END OF LAB]**
</p>

**Lab 4 - Using Copilot to generate tests**

**Purpose: In this lab, we'll see some examples of having Copilot generate tests**

1. Start out in the *prime.py* file we've been using. Position the cursor below the code.

2. Enter a comment to create unit tests
```
# create a function to do 5 unit tests of the code above
```

3. *If you don't get a suggestion*, enter code below to start nudging. Otherwise you can just accept the suggestion.

```
def test_is_prime():
```
![generating tests via comment](./images/cdd46a.png?raw=true "generating tests via comment") 

4. What if we didn't know how to test the code at all? Let's ask Copilot. Highlight the *is_prime()* function.

![selecting code](./images/cdd111.png?raw=true "selecting code") 

5. Now, switch to the chat interface and ask Copilot using the following prompt:

```
#selection: How do I test this code?
```
![prompting on how to test](./images/cdd112.png?raw=true "prompting on how to test") 

6. After entering this, you should see an explanation of how to test the code along with suggested testing code. If you expand the reference in the chat output, you can see that it only used the selected lines.

![testing explanation](./images/cdd113.png?raw=true "testing explanation") 

7. Let's see what the shortcut command would do. In the chat dialog enter "/tests" and then Enter. Copilot will want to add the *@workspace* agent onto the command. Just remove the *@workspace* from the beginning of the command. **Do not hit enter yet**.
```
/tests
```
8. Type a hash/sharp sign after /tests. At this point, Copilot should present a selection dialog. Choose #file from the menu.
```
/tests #
```
   
![shortcut test command](./images/cdd140.png?raw=true "shortcut test command")

9. A dialog will pop up near the top of the codespace with a selection of files. Select the *prime.py* file to complete the command. 

![file choice dialog](./images/cdd141.png?raw=true "file choice dialog")

10. Once the command looks like */tests #file:prime.py*, go ahead and hit enter to see the suggested test results.

![file choice dialog](./images/cdd142.png?raw=true "file choice dialog")

11. We can put this into a new file by hovering over the output in the Chat window, then selecting the "..." from the pop-up menu and selecting "Insert into new file". Go ahead and select that option and then you'll have a new file in your editor with the code that you can save as needed.

![Insert tests into new file](./images/cdd115a.png?raw=true "Insert tests into new file") 


<p align="center">
**[END OF LAB]**
</p>

**Lab 5 - Using Copilot to help with SQL**

**Purpose: In this lab, we’ll see some examples of how to have Copilot help with writing SQL**

1. Create a new file named dev.sql. You can create it via entering the line below in the terminal.

```
code dev.sql
```
   
2. Afterwards this file should be open in a tab in the editor. Assume we want to work with a database or database definition that defines a dataset for students, staff, curriculums, courses, schools of study, locations, and registrations for a university system. Let's see what Copilot would generate for a query to get all students in a course - without any other context.

Enter the following comment below and press Tab to accept suggestions. Remember that you may have to hit Enter multiple times to get Copilot to prompt. Or if you don't get a suggestion or only get a comment, try "nudging" Copilot via typing "select". 

```
-- define a select statement to get all students enrolled in a course
```
3. Go ahead and save this file as part of the project.  You can do this from the "3-line" menu under File->Save, or just click on the X next to the file's name in it's tab and select to Save it.

![Save sql file](./images/cdd96.png?raw=true "Save sql file") 

4. If the file is no longer open in the tabs, you can select the "Explorer" icon at the top of the sidebar and select the file in the list to open it back up.

![Reopening the file](./images/cdd108.png?raw=true "Reopening the file")    

5. Let's see if we get any different results if we provide Copilot additional context. Open the file create-tables.sql in the editor from the GitHub repository. (You can either select and open it from the file list or use the command below from the terminal.) Scroll through it and take a quick look at the contents.

```
code create-tables.sql
```

6. Now with that file open, go back up to the top of the dev.sql file.  Highlight and delete the comment and resulting query from step 2.
  
7. Enter the same comment as before to request the query. (Basically, repeat step 2.) See what Copilot suggests this time. You can accept the suggestions or cycle through options. (If you first get a duplicate line as the query, just hit Enter and Copilot should start making more meaningful suggestions.)

```
-- define a select statement to get all students enrolled in a course
```

8. If all goes well, this second pass should generate a query with many more specific references to the names and identifiers used in *create-tables.sql*.  (If not, delete the result and try again.) Take a look at the query and then compare the names/identifiers used to the ones in the *create-tables.sql* file. This will show that Copilot picks up on context from other files available to it to make better suggestions.

![New query](./images/cdd97.png?raw=true "New query") 

   
9. In some cases, we might be able to use a separate index to speed up operations.  Let's ask Copilot to create a new index based on the last query. Add the following line after the current query in the file *dev.sql*.

```
-- write an index to improve the performance of the query
```
![index](./images/cdd98.png?raw=true "index") 

10. Let's suppose we also want to have a table to capture student attendance. We can ask Copilot to create the table definition for us.

```
-- define a table for student attendance to capture attendance by class
```

(Here again, if you don't get a meaningful response from Copilot, you may need to nudge it by typing *CREATE*.) In the definition Copilot provided, it may have added a comment for the status in the same format as the comment in the courses.registration table definition in the create-tables.sql file.

![status values](./images/cdd99.png?raw=true "status values") 

11. Copilot can also create stored procedures. Let's ask it to create a new stored procedure for getting a list of enrolled students at a particular location. Let's use the **CMD+I** shortcut. Go to the bottom of the *dev.sql* file, invoke Copilot Chat via the shortcut and then enter the line below in the dialog. You can choose to **Accept** or **Discard** the result.

```
define a stored procedure to get course enrollment by location
```
![prompt for stored procedure](./images/cdd100.png?raw=true "prompt for stored procedure") 
  
12. We can be more prescriptive with our stored procedure definition.  Let's add a more complex request. Go to the Chat interface extension via clicking on the icon on the tool bar (if its not already opened). In the Chat window, enter the prompt below.

```
define a stored procedure to get instructor details associated with a location
include instructor details, location details, and courses associated with the instructor
use instructor_id as the input parameter
```
![More extensive stored procedure definition](./images/cdd51.png?raw=true "More extensive stored procedure definition") 

13. Finally, let's see Copilot optimize a query for us. Suppose we want to get all the course registrations for September, 2023.  Enter the following query in the file.

```
select * from courses.registrations where year(registration_date) = 2023 and month(registration_date) = 9;
```

14. Ask Copilot to optimize the previous query. You can do this via highlighting the query (make sure to highlight the *entire* query), switch to the separate chat interface and entering "/optimize" in the dialog. You can Accept or Discard the suggested optimization after that.

```
/optimize
```
![Optimizing a query](./images/cdd116.png?raw=true "Optimizing a query") 

    
<p align="center">
**[END OF LAB]**
</p>

**Lab 6 - Teaching Copilot about updates**

**Purpose: In this lab, we’ll see an example of what to do when Copilot does not have the most up-to-date information**

1. Create a new file called *explore.go* via the same approach as you used to create other files.

2. This file should now be open in an editor tab. Let's say we want to seed a random number generator with Go. Let's ask Copilot to write a function to do that. Prompt it through the **CMD+I** interface using the statement below. Then you can accept the suggested code.

```
write a function to seed a random number generator
```
![Asking Copilot to write function to seed a random number generator](./images/cdd117.png?raw=true "Asking Copilot to write function to seed a random number generator") 

3. Copilot has probably generated code using the rand.Seed function. The challenge is that as of Go 1.20, the Seed function is deprecated.  Ref: https://cs.opensource.google/go/go/+/refs/tags/go1.21.0:src/math/rand/rand.go;l=394

4. Let's see if Copilot understands that this is deprecrated. We'll ask it via a query. Switch to the separate chat inferface and enter the query below.

```
Is the Seed function deprecated in Go?
```
![Is Seed function deprecated?](./images/cdd118.png?raw=true "Is Seed function deprecated?") 

5. Copilot probably responded with no and some info about the function. So one way we can help Copilot understand language updates is by providing the context in our file. So let's start again. Delete the current content in the explore.go file.

6. Now,let's provide Copilot some more direct context by copying in updated code examples. After deleting the code block from step 3, copy and paste in the following example of the replacement for the Seed deprecation into your explore.go file.  This is taken from pkg.go.dev/math/rand.

```
	// Create and seed the generator.
	// Typically a non-fixed seed should be used, such as time.Now().UnixNano().
	// Using a fixed seed will produce the same output on every run.
	// r := rand.New(rand.NewSource(99))
```

7. Now, let's try the creation of the function again. Underneath the comments and code you just pasted, invoke the dialog via **CMD+I** and enter the statement below again.
```
write a function to seed a random number generator
```

8. This time, the code should be using the same format and NewSource function as you put in the file in step 6. You can just Accept the change. (If you don't see a complete function, but just a single line, try changing the prompt to be "write a complete function to seed a random number generator".

![Updated random number gen code after including updated usage](./images/cdd119.png?raw=true "Updated random number gen code after including updated usage")

<p align="center">
**[END OF LAB]**
</p>

**Lab 7 - Kubernetes, YAML generation and the 2021 problem**

**Purpose: Show YAML generation and out of date content.**

1. Create a new file - **deployment.yaml**

```
code deployment.yaml
```

2. Bring up the Copilot Chat dialog via **CMD+I** and enter in the following request.

```
write spec for deployment in Kubernetes with 2 replicas and image from busybox
add command to run in containers: sleep 3600
add label app: myapp
add label type: front-end
```

3. After a few moments, you should see it respond with the code. You can just Accept this.
![Kubernetes manifest](./images/cdd120.png?raw=true "Kubernetes manifest")

4. Suppose we don't know how to execute this code. Let's ask Copilot. Highlight the generated YAML in the deployment.yaml file.  Then go to the larger Chat interface and ask it. Put the following in the Chat interface.

```
How do I execute this?
```

5. Copilot should respond with something like the following:

![How to execute deployment](./images/cdd121.png?raw=true "How to execute deployment")


6. While we're in the Chat interface, let's ask it for the latest K8s version. Put the following into the dialog.

```
what is the latest Kubernetes version?
```

7. Notice that it identifies the latest version as 1.22 as of September 2021. This highlights the out-of-date issue with the LLM.

![Answer to latest K8s version](./images/cdd122.png?raw=true "Answer to latest K8s version")


8. Let's have Copilot generate some code to work with Kubernetes through the API. In the chat interface, enter the following.

```
How do I call the K8s API for scaling a deployment to 5 replicas with Python?
```
9. The results may tell us that we first need to make sure something like PIP is installed. If so, we don't need to worry about this at the moment. Go to the actual generated code in the chat output. Click in that output area and paste the code into a new file via clicking on the "..." and then the *Insert into new file* menu option.

![Add code to new file](./images/cdd124.png?raw=true "Add code to new file")


10. Suppose we change our mind and want to convert this code to Go. Click in the new file, and highlight the new code. Then, in the Chat interface tell it to translate to Go. Then, look in the separate chat output and you should see the equivalent Go code available.

```
translate to Go 
```
![Go translation](./images/cdd125.png?raw=true "Go translation")


<p align="center">
**[END OF LAB]**
</p>
    
**Lab 8 - Exploring Javascript, regular expression generator, auto-generating data**

**Purpose: Show Javascript and regular expression generation, auto-generate routine mappings**

1. Create a new file as **phone.js**

```
code contact.js
```

2. Prompt Copilot to create a function with a regular expression to validate a US phone number. You can use the **CMD+I** interface and just *Accept* the results.
```
create a function to validate any global phone number using a regular expression
```
![Regex function to validate phone #](./images/cdd127.png?raw=true "regex function to validate phone #")

3. Let's tell it to document the function by highlighting the code, invoking **CMD+I** and **/doc**.  You can just Accept the results.

![Automatic doc of function](./images/cdd128.png?raw=true "Automatic doc of function")  

4. Now let's see how Copilot can generate some data and mappings for us automatically. Enter the prompt below in the main/separate chat text entry area.
```
create a mapping of all 50 states to area codes where
the key is the state abbreviation and the value
 is an array of area codes with max 10
```
5. After running this, Copilot will generate the start of a list as shown below. Hover over the output area and click to insert the updates at the cursor in the *phone.js* file. (This assumes the cursor is below the previous function in the file.)

![Automatic gen of data](./images/cdd129.png?raw=true "Automatic gen of data") 

6. Notice that the example mapping was only for the first few states. We want to get the remaining mappings for the other states. Let's craft a prompt to complete the sequence. Enter the following in the main Copilot Chat entry box and then execute it.

```
create a mapping of the remaining states to area codes where
the key is the state abbreviation and the value
 is an array of area codes with max 10
```
![Completing the mappings](./images/cdd130.png?raw=true "Completing the mappings") 

7. It is likely that the generated text in the chat is still not complete. If that's the case, we may need to find a way to narrow the amount of data that's returned back in one instance by Copilot. Let's try a prompt that limits the max values returned to 5.

```
create a complete mapping of all 50 states to area codes where
the key is the state abbreviation and the value
 is an array of area codes with max 5
```
![Better prompt for remaining mappings](./images/cdd131.png?raw=true "Better prompt for remaining mappings") 


8. You can scroll to the bottom to confirm if you got entries for all the states. If you didn't, you could create additional prompts for specific ranges of states, change the number of values downward, etc. You could then copy these into your file if you want. Notice also the disclaimer at the bottom of the output that these may not be actual values.
   
![Disclaimer on actual values](./images/cdd132.png?raw=true "Disclaimer on actual values") 

<p align="center">
**[END OF LAB]**

**Lab 9 - Agents**

**Purpose: In this lab, we'll see how to work with GitHub Copilot agents.**

1. Now let's see how Copilot can help with tasks using agents. First, we'll have Copilot help us commit a change.  Let's use the *explore.go* file we created in Lab 6. If you haven't already, make sure that file is saved. You can do this by:
   
- Select the *explore.go* file
- Click on the *three-line menu* in the top left.
- From the menu that comes up, select *File* and then select *Save* (or use the shortcut).

![Save file](./images/cdd133.png?raw=true "Save file")

2. Now, let's invoke the **@terminal** agent to ask a common question about how to stage your code changes. Go to the *chat* interface and enter the prompt below. Afterwards, the command to do the staging should show up in the chat output.

```
@terminal how do I stage explore.go?
```
![query output](./images/cdd134.png?raw=true "query output") 

3. Hover over the window with the commands in it, and then click on the icon that pops up for the terminal. Click on that to insert the command into the terminal. Then hit return.

![insert into terminal](./images/cdd135.png?raw=true "insert into terminal")


4. Now let's commit our change through the interface and have Copilot suggest a commit message for us. Click on the source control icon in the sidebar (#1 in the figure below). Your *explore.go* file should be selected. In the box titled "Message" above the *Commit bar*, click on the *sparkle icon* at the far right side (#2 in the figure below).

![insert into terminal](./images/cdd136.png?raw=true "insert into terminal")

5. After this, Copilot should (hopefully) generate an appropriate commit message in that box. You can then copy the message and paste it into a *git commit* command in the terminal. **If you started your codespace from a fork, you can hit return to complete the commit if you want. This is optional. If you started your codespace via the one-click button, you will not have permissions to commit.**
```
git commit -m "<contents of generated commit message from Copilot goes here>"
```
![commit with generated message](./images/cdd137.png?raw=true "commit with generated message")

6. Now, let's switch gears and use the **@workspace** agent to help identify where we use certain things in our code. With the *explore.go* file still active in your editor, in the separate *chat* interface , enter the following prompt:

```
Which files are using SQL?
```

7. After executing this, you'll likely have some suggested information on how to search for files that use SQL in your project with search functionality for Visual Studio Code.
   
![initial query response](./images/cdd138.png?raw=true "initial query response")   

8. This is not the kind of answer we were looking for. Let's repeat the query with the *@workspace* agent.
```
@workspace Which files are using SQL?
```

9. After executing this, you should see Copilot assessing all of the files in the workspace and then returning a more specific and expected answer.
    
![more specific response](./images/cdd139.png?raw=true "more specific response")

<p align="center">
**[END OF LAB]**
</p>

**Lab 10 - Copilot CLI**

**Purpose: In this lab, we'll finish up with Copilot by using the CLI.**
    
1. Finally, let's work with the Copilot command line interface. The codespace already has the GitHub CLI installed, so we just need to install the Copilot extension and authenticate. Enter the following in the terminal.

```
gh extension install github/gh-copilot
```

2. After this, you can invoke the copilot command line to see the options available.

```
gh copilot
```
![Copilot CLI help](./images/cdd94.png?raw=true "Copilot CLI help")

3. To authenticate, use the command below in the terminal.

```
gh auth login --web
```

4. Follow the prompts. You'll get a one-time activation code that you should copy and then paste in the browser when prompted. (If you happen to get a message about an issue with GITHUB_TOKEN, you can use the command *export GITHUB_TOKEN=* to clear that.) You'll need to click on the "Authorize GitHub" button on the next screen and then confirm your signin after this to complete the process.
```   
export GITHUB_TOKEN=
```
![Copilot CLI auth](./images/cdd95.png?raw=true "Copilot CLI auth")

5. Once you have authenticate, you can try a couple of *gh copilot* commands like the ones below to see an example of how the CLI works.

```
gh copilot explain "ps -aux"
gh copilot suggest "install terraform"
```
 
<p align="center">
**[END OF LAB]**
</p>

<p align="center">
**THANKS!**
</p>

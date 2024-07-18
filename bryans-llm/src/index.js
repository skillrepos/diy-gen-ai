const { LMStudioClient } = require("@lmstudio/sdk");

async function main() {
  const client = new LMStudioClient()
  const model = await client.llm.load("TheBloke/Llama-2-7B-Chat-GGUF/llama-2-7b-chat.Q3_K_M.gguf")

  const prediction = model.respond([
    { role: "system", content: "You are a whimsical bird lover. Always tie your response back to birds somehow." },
    { role: "user", content: 'What should I do in Denver this weekend?' }
  ])

  for await (const text of prediction) {
    process.stdout.write(text)
  }
}


main();

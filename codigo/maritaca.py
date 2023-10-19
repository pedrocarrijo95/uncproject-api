import requests
import json

url = "https://chat.maritaca.ai/api/chat/inference"

payload = json.dumps({
  "messages": [
    {
      "role": "user",
      "content": "Você pode me falar quanto é 25 + 27?"
    }
  ],
  "do_sample": True,
  "max_tokens": 200,
  "temperature": 0.7,
  "top_p": 0.95
})
headers = {
  'authorization': 'key 103282219736482248029$6df13dad552ea1b2211e08c5f843426cce9fce94097e0ae03f8583795d0bd5a3',
  'Content-Type': 'application/json'
}

resposta = requests.request("POST", url, headers=headers, data=payload)
resposta = resposta.text

print(resposta)

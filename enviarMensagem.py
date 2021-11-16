from telethon import TelegramClient


def enviarMensagem(msg):
  
  name = '' #name user telegram
  api_id = '' #api id
  api_hash = '' #api hash
  token = '' #token bot
  phone = '' #number to send [+(dd1)(ddd)(number)]
  client = TelegramClient(name, api_id, api_hash)
  
  async def main():
    await client.send_message(phone, msg)

  with client:
    client.loop.run_until_complete(main())
  
    print("Enviando mensagem: "+str(msg)+" para "+str(phone))


enviarMensagem('Hello')
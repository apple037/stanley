# Python chatbot
## runtime environment
- Windows 10, Macos
- Python 3.9.7
## requirement
```
aiohttp==3.8.5
async-timeout==4.0.2
attrs==23.1.0
chardet==5.2.0
discord.py==2.3.1
idna==3.4
multidict==6.0.4
typing-extensions==4.7.1
yarl==1.9.2
requests==2.31.0
openai==0.27.8
python-dotenv==1.0.0
pytest==7.4.0
Pillow==10.0.0
replicate==0.11.0
```
## Preliminary
1. If you want to use image generation function, you need to run a [Stable Diffusion](https://github.com/AUTOMATIC1111/stable-diffusion-webui) or other image generation server
2. Update the .env file to your own token
## Function
1. Request and parse the response from poeNinja to get poe currency price
2. Add a chatGpt textCompletion to achieve simulate chatting
3. Add a Stable Diffusion image generation function
4. Add a Blip image to text function
5. Add a random cat function 🐱
## Future work
1. 🤔
<p align="center">
  <a href="#">
    <img
      alt="Solana logo"
      src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn-1.webcatalog.io%2Fcatalog%2Fopensea%2Fopensea-icon.png&f=1&nofb=1"
      width="140"
    />
  </a>
</p>

<h1 align="center">Opensea Launchpad bot</h1>


---
# 📚 Info
This bot will help you with mint NFT from Opensea Launchpad.

## How it works ?
Easy setup which uses ChromeDriver to open up a new chrome instance and mint the nft you are looking for quicker than a human. 

---
# ✨ Features
### Functionalities

- You can **launch multiple instances of the bot to bypass minting limit / wallet**
- Support 2captcha
- Support Windows & Mac
- Launch & Go | Once launched you do not need to stay in front of your screen because everything is automated!
- Easy Setup

---
# 📝 Tutorial

1. [Download zip file](https://github.com/SniperNFTbot/Opensea-minting-bot/archive/refs/heads/main.zip)
2. Be sure you have installed Python correctly, [here is a link to download](https://www.python.org/downloads/)
3. Open CMD and install modules  `pip install selenium requests webdriver-manager`
4. Setup config

    `launchpadLink` --> Link to Opensea launchpad

    `seedPhrase` --> Passphrase wallet

    `2captchaKey` --> 2captcha API key, there is an option to enter captcha manually, then leave this field blank
    
5. Open CMD and go to directory
    `cd directory/opensea-launchpad-bot`
6. Run python file

    windows : `python main.py`

    mac : `python3 main.py`

    or just start in bot's directory : `start.bat`
    
---
# ☕️ Support
You can dm me in twitter or create issue here, also you can support me with SOL❤️
```
BQ28dY6tZ3Gwx2xZcyNjP3pVYM8JDasqxGBxhz2LDSmM
```

---
# 🚩 Troubleshooting
- I tested the bot on google-chrome version is 103.0.5060 & python 3.10.2
- If after import wallet, bot stopping, then change opensea.py 20th line from 
  `driver.switch_to.window(driver.window_handles[1])` to `driver.switch_to.window(driver.window_handles[0])`

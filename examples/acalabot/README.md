# Acala bot [![GitHub license](https://img.shields.io/badge/license-GPL3-blue)](#LICENSE)

Simple prototype search assistant based on Rasa that uses fake Acala data and capable of recommending
exchanges based on user preferences.

Note: The bot was not requested by Acala. The bot is not an endorsement of Acala.

## How to use this demo?

1. Clone repo

```bash
git clone https://github.com/ltfschoen/rasa ~/acalabot
cd ~/acalabot/examples/acalabot
```

2. Install Python 3.7.9, Rasa 3.3.1 and Docker

3. Add example questions

4. Run the following to run an instance of duckling on port 8000
   ```bash
   sudo docker run -p 8000:8000 rasa/duckling
   ```

5. Run the Rasa server:
    ```bash
    rasa train; rasa run actions&rasa run --enable-api --cors "*"
    ```
6. Interact with the assistant by:
    * Clone https://github.com/JiteshGaikwad/Chatbot-Widget
    * Open index.html in you browser
    * Click the chatbox in the lower right corner to open it and interact with the bot

## License

- Acala bot is licensed under [GPL v3.0 with a classpath linking exception](LICENSE-GPL3).

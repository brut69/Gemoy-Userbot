# We're using Ubuntu 20.10
FROM vckyouuu/geezprojects:buster

RUN git branch -m main Gemoy-Userbot
RUN git fetch origin
RUN git branch -u origin/Gemoy-Userbot Gemoy-Userbot
RUN git remote set-head origin -a


RUN git clone -b Gemoy-UserBot https://github.com/brut69/Gemoy-UserBot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

# Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/brut69/Gemoy-Userbot/Gemoy-Userbot/requirements.txt?token=AU7C53HNK4WADCHGHMO7KE3BGEM2I

CMD ["python3","-m","userbot"]

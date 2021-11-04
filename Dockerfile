# We're using Ubuntu 20.10
# FROM vckyouuu/geezprojects:buster
FROM mrismanaziz/man-userbot:buster

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
RUN git clone -b Gemoy-Userbot https://github.com/brut69/Gemoy-Userbot /root/userbot
RUN mkdir /root/userbot/.bin

COPY ./sample_config.env ./config.env* /root/userbot/

WORKDIR /root/userbot

# Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/brut69/Gemoy-Userbot/Gemoy-Userbot/requirements.txt

CMD ["python3","-m","userbot"]

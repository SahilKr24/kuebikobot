FROM python:3

WORKDIR /usr/src/app

RUN mkdir -p downloads
COPY requirements.txt ./

RUN pip install -r requirements.txt

SHELL ["/bin/bash", "-c"]

RUN curl https://rclone.org/install.sh | bash

COPY rclone.conf /root/.config/rclone/rclone.conf

COPY . .

RUN chmod +x commands.sh && chmod +x folder.sh

CMD ["python","bot.py"]


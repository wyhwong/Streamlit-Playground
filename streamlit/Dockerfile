FROM python:3.11-slim-buster

RUN python3 -m pip install --upgrade pip
RUN pip3 install pyyaml overrides seaborn matplotlib python-binance pandas streamlit
RUN pip3 install --upgrade mplfinance

ARG USERNAME
ARG USER_ID
ARG GROUP_ID
ARG TZ
ENV TZ=${TZ}
RUN groupadd --gid ${GROUP_ID} ${USERNAME} && \
    adduser --disabled-password --gecos '' --uid ${USER_ID} --gid ${GROUP_ID} ${USERNAME}

USER ${USERNAME}
WORKDIR /home/${USERNAME}/app

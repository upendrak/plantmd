FROM python:3.7.4-slim-stretch

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN mkdir -p /root/.streamlit

RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'

COPY . .
RUN pip3 install -r requirements.txt


EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "demo.py"]

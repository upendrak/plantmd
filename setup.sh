mkdir -p ~/.streamlit

echo "\
[general]\n\
email = \"\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
enableCORS = false\n\
" > ~/.streamlit/config.toml
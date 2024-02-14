import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import base64


def read_image(path):
    """image from local file"""

    file_ = open(path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    return data_url


# company logo
logo_path = R"./images/Tesla_logo.png"
logo = read_image(logo_path)

st.markdown(
    f'<img src="data:image/gif;base64,{logo}" alt="logo tesla" width="60">',
    unsafe_allow_html=True,
)


# sidebar manu displaying the headers

st.sidebar.markdown('''
# Sections
:sparkles:[Header 1](#header-1)<br>
[Header 2](#header-2)

''', unsafe_allow_html=True)


# header 1
st.header('Header 1', anchor='header-1',divider='blue')


# header 2
st.header('Header 2', anchor='header-2', divider='blue')

### css for custom-button
st.markdown('''    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" integrity="sha384-..." crossorigin="anonymous">
        <style>
            .custom-button a {
                margin: 0;
                padding: 0;
                text-align: center;
                display: flex;
                justify-content: center;
                align-items: center;
                text-decoration: none;
            }

            .custom-button button {
                background-color: transparent;
                border: none;
                cursor: pointer;
                font-size: 16px;
                display: inline-block;
            }

            .custom-button button i {
                font-size: 50px;
                margin-right: 8px;
            }

            .custom-button button:hover {
                color: orange;
            }
        </style>

    <div class="custom-button">
        <a target="_self" href="#header-1">
            <button>
                <i class="fas fa-chevron-down"></i>
            </button>
        </a>
    </div>''', unsafe_allow_html=True)

# st.header('Header 3', anchor='header-3', divider='blue')


st.markdown('''
                    <div class="custom-button">
            <a target="_self" href="#header-1">
                <button>
                    <i class="fas fa-chevron-down"></i>
                </button>
            </a>
        </div>
            ''', unsafe_allow_html=True)

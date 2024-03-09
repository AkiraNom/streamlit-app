import streamlit as st


### css for pages
st.markdown('''
            <style>
            html, body {
            height: 100%;
            }

            body {
            display: grid;
            font-family: Avenir, sans-serif;
            color: #111;
            text-align: center;

            }''', unsafe_allow_html=True)

## css for tesla html link button
st.markdown('''
            <style>)
            .cta a {
            color: #ffffff;
            }

            .cta {
            text-decoration: none;
            position: relative;
            margin: auto;
            padding: 19px 22px;
            transition: all 0.2s ease;
            }
            .cta:before {
                text-decoration: none;
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            display: block;
            border-radius: 28px;
            background: orange;
            width: 56px;
            height: 56px;
            transition: all 0.3s ease;
            }
            .cta span {
            position: relative;
            color: white;
            font-size: 16px;
            line-height: 18px;
            font-weight: 900;
            letter-spacing: 0.25em;
            text-transform: uppercase;
            vertical-align: middle;
            }
            .cta svg {
            position: relative;
            top: 0;
            margin-left: 10px;
            fill: none;
            stroke-linecap: round;
            stroke-linejoin: round;
            stroke: white;
            stroke-width: 2;
            transform: translateX(-5px);
            transition: all 0.3s ease;
            }
            .cta:hover:before {
            color: "#ffffff";
            width: 100%;
            background: orange;
            }
            .cta:hover svg {
            transform: translateX(0);
            }
            .cta:active {
            transform: scale(0.96);
            }
            </style>
                ''', unsafe_allow_html=True)

### css for company description
st.markdown('''
            <style>
            .logo {
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 50%;
            }
            .top-page p{

                font-size: 20px;
                font-weight:bold;
                text-align: center;
            }
            .top-page span {
                color: orange;
            }
            </style>
            ''', unsafe_allow_html=True)


### css for market, share, station description
st.markdown('''
            <style>
            .sankey-description,
            .market-description,
            .share-description,
            .station-description  {
                color:white;
                font-size:22px;
                font-weight:bold;
                text-align: center;
            }
            </style>
            ''', unsafe_allow_html=True)

### css for scroll-botton
st.markdown('''
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" integrity="sha384-..." crossorigin="anonymous">

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

    ''', unsafe_allow_html=True)

st.markdown('''
            <style>
            .custom-button div {
                margin: 0;
                padding: 0;
                text-align: left;
            }
            </style>
            ''', unsafe_allow_html=True)

st.markdown('''
            <style>
            .section-list {
                text-align: left;
                margin-left: 40px;
                margin-bottom:10px;
            }
            .section-list h2{
                text-align: center;
            }

            .section-list a {
                text-decoration: none;
                color: #FFFFFF;
                font-size:16px;
                font-weight:bold;
            }

            .section-list span {

                font-size: 25px;
                margin-righ: 20px;
            }
            </style>

            ''', unsafe_allow_html=True)

st.markdown('''
            <style>
            .top-button {
                text-align: center;
                }

             .top-button a {
                text-decoration: none;
                color: #FFFFFF;
                font-size:16px;
                font-weight:bold;
                }
            ''', unsafe_allow_html=True)








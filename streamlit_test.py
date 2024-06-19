import streamlit as st
from PIL import Image

st.sidebar.header("Login")
user_id = st.sidebar.text_input("ID", value="", max_chars=15)
user_pw = st.sidebar.text_input("Password", value="", type='password')

if user_id == "shuvlee" and user_pw == '17485':
    st.sidebar.header("List of Fine Arts")
    sel_options=["",'SVT Right here!', 'Girl with a Pearl Earring', 'The Starry Night', 'The Scream of Nature', 'The tree of life', '월하정인']
    name_painter=["", 'Going Seventeen','Johannes Vermeer', 'Vincent Van Gogh', 'Edvard Munch', 'Gustav Klimt', '신윤복']
    user_opt = st.sidebar.selectbox("What's your favorite fine arts?", sel_options, index=1)
    sel_index = sel_options.index(user_opt)
    st.sidebar.write("The seleted fine art is ", user_opt)
    st.sidebar.write("The painter of selected fine art is ", name_painter[sel_index])

    # main
    st.subheader("The Fine Arts")
    image_files=["",'SVTwelcome.jpg','Vermeer.png','Gogh.png', 'Munch.png', 'Klimt.jpg', 'ShinYoonbok.png']
    sel_index = sel_options.index(user_opt)
    img_file = image_files[sel_index]
    img_local = Image.open(f"img/{img_file}")
    st.image(img_local, caption=f"{user_opt} by {name_painter[sel_index]}")
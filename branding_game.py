import streamlit as st

st.title("🎮 Brand Strategy Game")

# inicializar estado del juego
if "brand_equity" not in st.session_state:
    st.session_state.brand_tom = 50
    st.session_state.brand_sr = 10
    st.session_state.image = 0

st.write("This game is under construction send all your comments and suggestions to vargastroncozoignacio@gmail.com")
st.write("You are the brand manager of a new coffee brand.")

st.subheader("Current metrics")

st.write("Brand Top-of-Mind %:", st.session_state.brand_tom)
st.write("Brand Spontaneous recall %:", st.session_state.brand_sr)
st.write("Alignment with the desired image:", st.session_state.image)

st.subheader("Decision 1: Positioning")

choice = st.radio(
    "How will you position the brand?",
    [
        "Premium artisanal coffee",
        "Sustainable ethical coffee",
        "Low price mass coffee"
    ]
)

if st.button("Make decision"):

    if choice == "Premium artisanal coffee":
        st.session_state.brand_tom += 15
        st.session_state.brand_sr -= 2
        st.session_state.image += 5
        st.success("Your brand is perceived as high quality!")

    elif choice == "Sustainable ethical coffee":
        st.session_state.brand_tom += 10
        st.session_state.brand_sr += 1
        st.session_state.image += 3
        st.success("Consumers appreciate your ethical positioning.")

    elif choice == "Low price mass coffee":
        st.session_state.brand_tom -= 5
        st.session_state.brand_sr += 5
        st.session_state.image += 7
        st.success("Your brand gained volume but lost prestige.")

st.subheader("Updated results")

st.write("Brand Top-of-Mind %:", st.session_state.brand_tom)
st.write("Brand Spontaneous recall %:", st.session_state.brand_sr)
st.write("Alignment with the desired image:",  st.session_state.image)

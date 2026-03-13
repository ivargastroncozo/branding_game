import streamlit as st

st.title("🎮 Brand Strategy Game")

# inicializar estado del juego
if "brand_equity" not in st.session_state:
    st.session_state.brand_tom = 50
    st.session_state.brand_sr = 10
    st.session_state.image = 0

st.write("This game is being developed by Ignacio Vargas. Please send all your comments and suggestions to vargastroncozoignacio@gmail.com")
st.write("You are the brand manager of a new coffee brand.")

st.subheader("Current metrics")

st.write("Brand Top-of-Mind %:", st.session_state.brand_tom)
st.write("Brand Spontaneous recall %:", st.session_state.brand_sr)
st.write("Alignment with the desired image:", st.session_state.image)

st.subheader("Decision 1: Brand Essence")

choice1 = st.radio(
    "What will be your brand essence?",
    [
        "Masterfully crafted coffee",
        "Brewing to save the world",
        "Good coffee for everyone"
    ]
)

st.success("Remember that all your decisions must reflect your essence. This is your brand DNA!")

st.subheader("Decision 2: Positioning")

choice2 = st.radio(
    "How will you position the brand?",
    [
        "Premium artisanal coffee",
        "Sustainable ethical coffee",
        "Low price mass coffee"
    ]
)

if st.button("Make decision"):

    if choice1 == "Masterfully crafted coffee" and choice2 == "Premium artisanal coffee":
        st.session_state.brand_tom += 10
        st.session_state.brand_sr -= 10
        st.session_state.image += 10
        st.success("Your brand is perceived as high quality, just as you wanted!")

    elif choice1 == "Masterfully crafted coffee" and choice2 != "Premium artisanal coffee":
        st.warning("Your positioning is inconsistent with your brand essence.")
   
    elif choice1 == "Brewing to save the world" and choice2 == "Sustainable ethical coffee":
        st.session_state.brand_tom += 3
        st.session_state.brand_sr += 2
        st.session_state.image += 5
        st.success("Consumers appreciate your ethical positioning, just as you wanted!.")
        
    elif choice1 == "Brewing to save the world" and choice2 != "Sustainable ethical coffee":
        st.warning("Your positioning is inconsistent with your brand essence.")

    elif choice1 == "Good coffee for everyone" and choice2 == "Low price mass coffee":
        st.session_state.brand_tom -= 7
        st.session_state.brand_sr += 5
        st.session_state.image += 3
        st.success("Your brand gained volume but lost prestige, just as you wanted!")

    elif choice1 == "Good coffee for everyone" and choice2 != "Low price mass coffee":
        st.warning("Your positioning is inconsistent with your brand essence.")

st.subheader("Updated results")

st.write("Brand Top-of-Mind %:", st.session_state.brand_tom)
st.write("Brand Spontaneous recall %:", st.session_state.brand_sr)
st.write("Alignment with the desired image:",  st.session_state.image)





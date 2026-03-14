import streamlit as st

st.title("🎮 Brand Strategy Game")

# inicializar estado del juego
#if "brand_equity" not in st.session_state:
#   st.session_state.brand_tom = 50
#   st.session_state.brand_sr = 10
#   st.session_state.image = 0

st.write("This game is being developed by Ignacio Vargas. Please send all your comments and suggestions to vargastroncozoignacio@gmail.com")
st.write("You are the brand manager of a new coffee brand, and you will need to make decisions to achieve your desired brand equity.")

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

st.subheader("Decision 2: Now you need to define your target market. First, select your segmentation variables.")

choice2 = st.radio(
    "What will be your segmentation variables?",
    [
        "Age – Gender",
        "Occupation status (Student, Worker, Unemployed) – Price sensitivity",
        "Income – Ethnicity",
        "Age – Physical activity (times per week)"
    ]
)


if st.button("Make decision 2"):

    if choice2 == "Age – Gender":
        st.warning("Selecting two demographic variables is not a good option. It can lead to defining one segment whose members have very diverse preferences.")

    elif choice2 == "Occupation status (Student, Worker, Unemployed) – Price sensitivity":
        st.success("This variables are a good general option! Combining demographics with psychographics characteristics.")
   
    elif choice2 == "Income – Ethnicity":
        st.warning("Selecting two demographic variables is not a good option. It can lead to defining one segment whose members have very diverse preferences.")

    elif choice2 == "Age – Physical activity (times per week)":
        st.warning("Here you are combining demographics and behavioral variables, but is physical activity relevant for your brand?")

st.subheader("Decision 3: Positioning")

choice3 = st.radio(
    "How will you position the brand?",
    [
        "Premium artisanal coffee",
        "Sustainable ethical coffee",
        "Low price mass coffee"
    ]
)

if st.button("Make decision 3"):

    if choice1 == "Masterfully crafted coffee" and choice3 == "Premium artisanal coffee":
        st.success("Your brand is perceived as high quality, just as you wanted!")

    elif choice1 == "Masterfully crafted coffee" and choice3 != "Premium artisanal coffee":
        st.warning("Your positioning is inconsistent with your brand essence.")
   
    elif choice1 == "Brewing to save the world" and choice3 == "Sustainable ethical coffee":
        st.success("Consumers appreciate your ethical positioning, just as you wanted!.")
        
    elif choice1 == "Brewing to save the world" and choice3 != "Sustainable ethical coffee":
        st.warning("Your positioning is inconsistent with your brand essence.")

    elif choice1 == "Good coffee for everyone" and choice3 == "Low price mass coffee":
        st.success("Your brand gained volume but lost prestige, just as you wanted!")

    elif choice1 == "Good coffee for everyone" and choice3 != "Low price mass coffee":
        st.warning("Your positioning is inconsistent with your brand essence.")





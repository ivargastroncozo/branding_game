import streamlit as st

if "stage" not in st.session_state:
    st.session_state.stage = 1

if st.session_state.stage == 1:
    st.title("🎮 Brand Strategy Game")

    # inicializar estado del juego
    #if "brand_equity" not in st.session_state:
    #    st.session_state.brand_tom = 50
    #    st.session_state.brand_sr = 10
    #    st.session_state.image = 0

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

    if st.button("Confirm essence"):
        st.session_state.choice1 = choice1
        st.session_state.stage = 2
        st.rerun()

if st.session_state.stage == 2:
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

    if st.button("Confirm segmentation variables"):

        if choice2 == "Age – Gender":
            st.session_state.feedback = "Selecting two demographic variables is not a good option. It can lead to defining one segment whose members have very diverse preferences."
            st.session_state.feedback_type = "warning"

        elif choice2 == "Occupation status (Student, Worker, Unemployed) – Price sensitivity":
            st.session_state.feedback = "These variables are a good general option! Combining demographics with psychographic characteristics."
            st.session_state.feedback_type = "success"

        elif choice2 == "Income – Ethnicity":
            st.session_state.feedback = "Selecting two demographic variables is not a good option. It can lead to defining one segment whose members have very diverse preferences."
            st.session_state.feedback_type = "warning"

        elif choice2 == "Age – Physical activity (times per week)":
            st.session_state.feedback = "You are combining demographic and behavioral variables, but is physical activity relevant for your brand?"
            st.session_state.feedback_type = "warning"
    
    if st.button("Continue to next decision"):
        st.session_state.choice2 = choice2
        st.session_state.stage = 3
        st.rerun()

if st.session_state.stage == 3:
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
            st.session_state.feedback = "Your brand is perceived as high quality, just as you wanted!"
            st.session_state.feedback_type = "success"

        elif choice1 == "Masterfully crafted coffee" and choice3 != "Premium artisanal coffee":
            st.session_state.feedback = "Your positioning is inconsistent with your brand essence."
            st.session_state.feedback_type = "warning"

        elif choice1 == "Brewing to save the world" and choice3 == "Sustainable ethical coffee":
            st.session_state.feedback = "Consumers appreciate your ethical positioning, just as you wanted!"
            st.session_state.feedback_type = "success"

        elif choice1 == "Brewing to save the world" and choice3 != "Sustainable ethical coffee":
            st.session_state.feedback = "Your positioning is inconsistent with your brand essence."
            st.session_state.feedback_type = "warning"

        elif choice1 == "Good coffee for everyone" and choice3 == "Low price mass coffee":
            st.session_state.feedback = "Your brand is perceived as accessible, just as you wanted!"
            st.session_state.feedback_type = "success"

        elif choice1 == "Good coffee for everyone" and choice3 != "Low price mass coffee":
            st.session_state.feedback = "Your positioning is inconsistent with your brand essence."
            st.session_state.feedback_type = "warning"

    if st.button("Restart game"):
        st.session_state.stage = 1
        st.rerun()

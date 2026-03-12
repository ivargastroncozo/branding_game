import streamlit as st

st.title("🎮 Brand Strategy Game")

# inicializar estado del juego
if "brand_equity" not in st.session_state:
    st.session_state.brand_equity = 50
    st.session_state.market_share = 10
    st.session_state.profit = 0

st.write("You are the brand manager of a new coffee brand.")

st.subheader("Current metrics")

st.write("Brand Equity:", st.session_state.brand_equity)
st.write("Market Share:", st.session_state.market_share)
st.write("Profit:", st.session_state.profit)

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
        st.session_state.brand_equity += 15
        st.session_state.market_share -= 2
        st.session_state.profit += 5
        st.success("Your brand is perceived as high quality!")

    elif choice == "Sustainable ethical coffee":
        st.session_state.brand_equity += 10
        st.session_state.market_share += 1
        st.session_state.profit += 3
        st.success("Consumers appreciate your ethical positioning.")

    elif choice == "Low price mass coffee":
        st.session_state.brand_equity -= 5
        st.session_state.market_share += 5
        st.session_state.profit += 7
        st.success("Your brand gained volume but lost prestige.")

st.subheader("Updated results")

st.write("Brand Equity:", st.session_state.brand_equity)
st.write("Market Share:", st.session_state.market_share)
st.write("Profit:", st.session_state.profit)
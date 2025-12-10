import streamlit as st
import json
from reasoner import ProductReasoner

st.title("Shopkeeper Product Substitution Assistant")

reasoner = ProductReasoner()

with open("kg.json", "r") as f:
    data = json.load(f)

product_ids = list(data["products"].keys())

req_product = st.selectbox("Select Requested Product", product_ids)
max_price = st.number_input("Max Price", min_value=1, value=100)
req_tags = st.multiselect("Required Tags", ["lactose_free", "vegan", "veg", "low_fat", "lactose"])
brand = st.text_input("Preferred Brand (optional)")

if st.button("Find Alternatives"):
    exact, subs = reasoner.find_substitutes(
        req_product, max_price, req_tags, brand
    )

    if exact:
        st.success("The requested product is in stock:")
        st.json(exact)

    else:
        if not subs:
            st.error("No substitutes found.")
        else:
            st.info("Suggested substitutes:")

            for pid, pdata, rules in subs:
                st.subheader(pdata["name"])
                st.write(f"Brand: {pdata['brand']}")
                st.write(f"Price: ₹{pdata['price']}")
                st.write(f"Tags: {', '.join(pdata['tags'])}")
                st.write("**Rules triggered:**")
                st.code("\n".join(rules))



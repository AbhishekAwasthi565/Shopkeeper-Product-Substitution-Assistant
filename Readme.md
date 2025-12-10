
# Shopkeeper Product Substitution Assistant  
### Streamlit + Knowledge Graph + Classical Reasoning (NO ML)

This project implements a *product substitution system* for small shops when a requested item is out of stock.  
It uses a **Knowledge Graph + BFS-based reasoning + explicit rule-based explanations** (no ML, no embeddings).

---

## Features

###  Streamlit Web App
- Select a product  
- Set maximum price  
- Choose required tags  
- Optional brand filter  
- Returns:
  - Exact product (if in stock)
  - OR up to **3 best alternative substitutes**

---

## Knowledge Graph (kg.json)

### Nodes
- Products  
- Categories  

### Edges
- `IS_A` (product → category)  
- `similar_category` (category ↔ category)

---

## Classical Reasoning Engine
Implemented in `reasoner.py` using:

### BFS-Based Search
- Radiates search outward from requested item  
- Prefers:
  - same category  
  - then similar category  

### Filters
- Max price  
- Required tags  
- Brand  
- Stock availability  

### Explanation Rules
- `same_category_same_brand`  
- `same_category_diff_brand`  
- `similar_category`  
- `tag_matched`  
- `cheaper_option`  
- `all_required_tags_matched`  

Each substitute includes a transparent rule-based explanation.

---

## Project Structure  

```

shopkeeper-substitution-assistant/
│
├── app.py                # Streamlit UI
├── reasoner.py           # BFS reasoning + rule engine
├── kg.json               # Knowledge Graph
├── requirements.txt      # Dependencies
└── README.md             # Documentation

````

---

## Running Locally

```bash
pip install -r requirements.txt
streamlit run app.py
````

---

## Live Application

### 🔗 **[https://shopkeeper-appuct-substitution-assistant-abhishek.streamlit.app/](https://shopkeeper-appuct-substitution-assistant-abhishek.streamlit.app/)**

---

```

---








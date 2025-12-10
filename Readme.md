README.md
#  Shopkeeper Product Substitution Assistant  
### Streamlit + Knowledge Graph + Classical Reasoning (NO ML)

This project implements a *product substitution system* for small shops when a requested item is out of stock.  
It uses a *Knowledge Graph* + *BFS-based reasoning* + *rule-based explanations*.

---

##  Features

###  Streamlit Web App
- Select product
- Set max price
- Choose required tags
- Optional brand filter
- Shows:
  - Exact product (if in stock)
  - OR up to *3 substitutes*

###  Knowledge Graph (kg.json)
- Nodes:
  - Products
  - Categories
- Edges:
  - IS_A
  - similar_category

###  Classical Reasoning Engine
- BFS graph traversal
- Filters:
  - max price  
  - tags  
  - brand  
  - stock  
- Explanation rules:
  - same_category_same_brand
  - same_category_diff_brand
  - similar_category
  - cheaper_option
  - all_required_tags_matched

---

##  Project Structure  
⚠️ *Do not modify this structure. The application will terminate if files move.*



shopkeeper-substitution-assistant/
│
├── app.py # Streamlit UI
├── reasoner.py # BFS reasoning + rule engine
├── kg.json # Knowledge Graph
├── requirements.txt # Dependencies
└── README.md # Documentation


---

##  Running Locally

```bash
pip install -r requirements.txt
streamlit run app.py



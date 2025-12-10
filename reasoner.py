import json
import networkx as nx

class ProductReasoner:
    def __init__(self, kg_path="kg.json"):
        with open(kg_path, "r") as f:
            self.kg = json.load(f)

        self.G = nx.Graph()
        self._build_graph()

    def _build_graph(self):
        for pid, pdata in self.kg["products"].items():
            self.G.add_node(pid, **pdata, node_type="product")

        for cat, related in self.kg["categories"].items():
            self.G.add_node(cat, node_type="category")
            for r in related:
                self.G.add_node(r, node_type="category")
                self.G.add_edge(cat, r, relation="similar_category")

        for pid, pdata in self.kg["products"].items():
            self.G.add_edge(pid, pdata["category"], relation="IS_A")

    def _match_constraints(self, pdata, max_price, req_tags, brand):
        if not pdata["in_stock"]:
            return False

        if pdata["price"] > max_price:
            return False

        if brand and pdata["brand"].lower() != brand.lower():
            return False

        for t in req_tags:
            if t not in pdata["tags"]:
                return False

        return True

    def _explain(self, req_prod, alt_prod):
        rules = []
        if req_prod["category"] == alt_prod["category"]:
            if req_prod["brand"] == alt_prod["brand"]:
                rules.append("same_category_same_brand")
            else:
                rules.append("same_category_diff_brand")
        else:
            rules.append("similar_category")

        if alt_prod["price"] <= req_prod["price"]:
            rules.append("cheaper_option")

        rules.append("all_required_tags_matched")
        return rules

    def find_substitutes(self, req_product_id, max_price, req_tags, brand=None):
        if req_product_id not in self.kg["products"]:
            return None, []

        req_prod = self.kg["products"][req_product_id]

        if req_prod["in_stock"]:
            return req_prod, []

        visited = set()
        queue = [(req_product_id, 0)]
        substitutes = []

        while queue and len(substitutes) < 3:
            node, depth = queue.pop(0)
            visited.add(node)

            for neighbor in self.G.neighbors(node):
                if neighbor in visited:
                    continue

                visited.add(neighbor)

                if neighbor in self.kg["products"]:
                    pdata = self.kg["products"][neighbor]

                    if self._match_constraints(pdata, max_price, req_tags, brand):
                        explanation = self._explain(req_prod, pdata)
                        substitutes.append((neighbor, pdata, explanation))

                        if len(substitutes) == 3:
                            break

                queue.append((neighbor, depth + 1))

        return None, substitutes


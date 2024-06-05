class FuzzySet:
    def __init__(self, elements, membership_function):
        self.elements = elements
        self.membership_function = membership_function

    def union(self, other_set):
        union_elements = list(set(self.elements + other_set.elements))
        union_membership = max(self.membership_function(e) for e in union_elements)
        return FuzzySet(union_elements, lambda x: union_membership)

    def intersection(self, other_set):
        intersection_elements = list(set(self.elements).intersection(other_set.elements))
        intersection_membership = min(self.membership_function(e) for e in intersection_elements)
        return FuzzySet(intersection_elements, lambda x: intersection_membership)

    def complement(self, universe):
        complement_elements = list(set(universe).difference(self.elements))
        complement_membership = max(1 - self.membership_function(e) for e in complement_elements)
        return FuzzySet(complement_elements, lambda x: complement_membership)

    def difference(self, other_set):
        difference_elements = list(set(self.elements).difference(other_set.elements))
        difference_membership = min(self.membership_function(e) for e in difference_elements)
        return FuzzySet(difference_elements, lambda x: difference_membership)

    @staticmethod
    def cartesian_product(set1, set2):
        cartesian_elements = [(a, b) for a in set1.elements for b in set2.elements]
        return cartesian_elements

    @staticmethod
    def max_min_composition(rel1, rel2):
        composed_relation = {}
        for (a, b) in rel1:
            for (c, d) in rel2:
                if b == c:
                    composed_relation[(a, d)] = min(rel1[(a, b)], rel2[(c, d)])
        return composed_relation

# Example usage
if __name__ == "__main__":
    # Example fuzzy sets
    set1 = FuzzySet([1, 2, 3], lambda x: 1 if x <= 3 else (5 - x) / 2 if 3 < x <= 5 else 0)
    set2 = FuzzySet([3, 4, 5], lambda x: 1 if x <= 3 else (5 - x) / 2 if 3 < x <= 5 else 0)
    universe = [1, 2, 3, 4, 5, 6]

    # Union
    union_set = set1.union(set2)
    print("Union:", union_set.elements)

    # Intersection
    intersection_set = set1.intersection(set2)
    print("Intersection:", intersection_set.elements)

    # Complement
    complement_set = set1.complement(universe)
    print("Complement:", complement_set.elements)

    # Difference
    difference_set = set1.difference(set2)
    print("Difference:", difference_set.elements)

    # Cartesian product
    cartesian_product = FuzzySet.cartesian_product(set1, set2)
    print("Cartesian Product:", cartesian_product)

    # Fuzzy Relations
    relation1 = {('A', 'X'): 0.7, ('B', 'Y'): 0.4, ('C', 'Z'): 0.9}
    relation2 = {('X', 'M'): 0.6, ('Y', 'N'): 0.8, ('Z', 'O'): 0.5}

    # Max-min composition
    composition = FuzzySet.max_min_composition(relation1, relation2)
    print("Max-min Composition:", composition)

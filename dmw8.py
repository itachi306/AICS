from collections import defaultdict
from itertools import combinations

def generate_candidates(itemset, k):
    """
    Generate candidate itemsets of size k from the given itemset.
    """
    candidates = set()
    for item1 in itemset:
        for item2 in itemset:
            if len(item1.union(item2)) == k:
                candidates.add(item1.union(item2))
    return candidates

def support_count(transactions, itemset):
    """
    Calculate the support count of an itemset in the transactions.
    """
    count = 0
    for transaction in transactions:
        if itemset.issubset(transaction):
            count += 1
    return count

def apriori(transactions, min_support):
    """
    Run the Apriori algorithm to find frequent itemsets.
    """
    itemset = set()
    for transaction in transactions:
        for item in transaction:
            itemset.add(frozenset([item]))
    
    frequent_itemsets = []
    k = 1
    while itemset:
        frequent_itemsets_k = []
        candidates = generate_candidates(itemset, k)
        for candidate in candidates:
            support = support_count(transactions, candidate) / len(transactions)
            if support >= min_support:
                frequent_itemsets_k.append((candidate, support))
        frequent_itemsets.extend(frequent_itemsets_k)
        itemset = set([itemset for itemset, support in frequent_itemsets_k])
        k += 1
    return frequent_itemsets

if __name__ == "__main__":
    # Example usage
    transactions = [
        {'bread', 'milk', 'butter'},
        {'bread', 'milk'},
        {'bread', 'diapers', 'beer', 'eggs'},
        {'milk', 'diapers', 'beer', 'cola'},
        {'bread', 'milk', 'diapers', 'beer'},
    ]
    min_support = 0.4
    frequent_itemsets = apriori(transactions, min_support)
    for itemset, support in frequent_itemsets:
        print(f"Itemset: {itemset}, Support: {support}")

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

class AssociationAnalyzer:

    def __init__(self, transaction_dataframe):
        self.transaction_dataframe = transaction_dataframe

    def discover_patterns(self):
        try:
            frequent_itemsets = apriori(
                self.transaction_dataframe,
                min_support=0.05,
                use_colnames=True
            )

            rules = association_rules(
                frequent_itemsets,
                metric="lift",
                min_threshold=1.0
            )

            rules = rules.sort_values(
                by="lift",
                ascending=False
            )

            print("\nTop Association Rules:\n")
            print(
                rules[
                    [
                        "antecedents",
                        "consequents",
                        "support",
                        "confidence",
                        "lift"
                    ]
                ].head(20)
            )

            return rules
        except Exception as error:
            print(
                f"Error during association analysis: {error}"
            )
class CostTracker:

    def __init__(self):

        self.calls = 0
        self.input_tokens = 0
        self.output_tokens = 0

    def record(self,
               input_tokens,
               output_tokens):

        self.calls += 1
        self.input_tokens += input_tokens
        self.output_tokens += output_tokens

    def compute_cost(self,
                     input_price=0.000001,
                     output_price=0.000002):

        return (
            self.input_tokens * input_price
            +
            self.output_tokens * output_price
        )
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        res = []
        found = False
        for i, s in enumerate(input):
            if s in '+-*':
                found = True
                lres = self.diffWaysToCompute(input[:i])
                rres = self.diffWaysToCompute(input[i+1:])

                for lv in lres:
                    for rv in rres:
                        v = 0
                        if input[i] == '+':
                            v = lv + rv
                        elif input[i] == '-':
                            v = lv - rv
                        else:
                            v = lv * rv
                        res.append(v)
        if not found:
            res.append(int(input))
        return res
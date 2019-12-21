

class Demographic(object):

    def __init__(self, name, baseline_rate, category="all"):
        self.base_graduation_rate = baseline_rate
        self.current_graduation_rate = baseline_rate
        self.name = name
        self.graduation_rate = baseline_rate
        self.category = category

    def updateGraduationRate(self, policyList):

        if(policyList is None):
            return
        self.getPolicyImpactPercentages(policyList)

        new_rate = self.base_graduation_rate

        for policy in policyList:
            if policy.enabled:
                #print("Policy percentage impact: " + str(policy.percentage_rate_impact_for_current_demographic))
                new_rate = new_rate + policy.percentage_rate_impact_for_current_demographic
        self.current_graduation_rate = new_rate
        #print("New graduation rate: " + str(self.current_graduation_rate))



    def getPolicyImpactPercentages(self, policyList):
        for policy in policyList:
            if policy.enabled:
                if "all" in policy.benefited_demographics or self.name in policy.benefited_demographics:
                    policy.percentage_rate_impact_for_current_demographic = policy.general_percentage_rate_impact * 0.05
                elif "all" in policy.harmed_demographics or self.name in policy.harmed_demographics:
                    policy.percentage_rate_impact_for_current_demographic = policy.general_percentage_rate_impact * -0.05
                else:
                    policy.percentage_rate_impact_for_current_demographic = policy.general_percentage_rate_impact * 0.025

#fuzzy cognitive map

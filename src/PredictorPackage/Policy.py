class Policy(object):

    def __init__(self, name, percentage_rate_impact=1, helped_groups=[], harmed_groups=[]):
        self.name = name
        self.general_percentage_rate_impact = percentage_rate_impact
        self.benefited_demographics = helped_groups
        self.harmed_demographics = harmed_groups
        self.percentage_rate_impact_for_current_demographic = None
        self.enabled = False


    def changeState(self):
        self.enabled = not self.enabled

    def disable(self):
        self.enabled = False

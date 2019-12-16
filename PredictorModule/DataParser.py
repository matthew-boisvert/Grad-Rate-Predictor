import csv
import re
from . import Policy
from . import Demographic

def generateDemographicsList(input_file):
    demographics_list = []
    with open(input_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count >= 1:
                demographic_name = row[0]
                demographic_category = row[1]
                demographic_base_rate = float(row[2])
                if(demographic_category == ""):
                    demographics_list.append(Demographic.Demographic(demographic_name, demographic_base_rate))
                else:
                    demographics_list.append(Demographic.Demographic(demographic_name, demographic_base_rate, demographic_category))
            line_count += 1
    return demographics_list

def generatePolicyList(input_file):
    policy_list = []
    with open(input_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count >= 1:
                policy_name = row[0]
                benefitted_demographics = parsePolicyString(row[1])
                harmed_demographics = parsePolicyString(row[2])
                if(benefitted_demographics is None and harmed_demographics is None):
                    policy_list.append(Policy.Policy(policy_name))
                elif(benefitted_demographics is None):
                    policy_list.append(Policy.Policy(policy_name, harmed_groups=harmed_demographics))
                elif(harmed_demographics is None):
                    policy_list.append(Policy.Policy(policy_name, helped_groups=benefitted_demographics))
                else:
                    policy_list.append(Policy.Policy(policy_name, helped_groups=benefitted_demographics, harmed_groups=harmed_demographics))
            line_count += 1
    return policy_list

def parsePolicyString(str):
    if(len(str) == 0):
        return None
    return str.split("/")
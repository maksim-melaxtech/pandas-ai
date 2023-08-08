""" Prompt to generate Python code for multiple dataframes """


import pandas as pd

from pandasai.constants import END_CODE_TAG, START_CODE_TAG
from .base import Prompt


class MultipleDataframesPrompt(Prompt):
    """Prompt to generate Python code"""

    text: str = """
You are provided with the following pandas dataframes:"""
    instruction: str = """
This is column descriptions for df1:
npi: National Provider Identifier - a unique identification number for healthcare providers.
physician_name: Name of the physician or healthcare provider.
specialty: The medical specialty or field in which the physician practices.
physician_phone: Contact phone number for the physician.
physician_degrees: Academic degrees or qualifications held by the physician.
physician_disease_tiers: Tiers or categories of diseases the physician specializes in treating.
physician_existing_site_yes: Indicates whether the physician has an existing medical site ("yes" or "no").
physician_existing_site_zip3: The zip code prefix of the existing medical site location.
physician_trialtrove_profile: Presence of a physician's profile on TrialTrove, likely a medical research platform.
state_full_name: Full name of the state in which the physician practices.
physician_primary_practice_address: Main address of the physician's primary practice.
primary_organization_affiliation: Main healthcare organization the physician is affiliated with.
organization_classification: Classification or type of healthcare organization.

This is column descriptions for df2:
npi: National Provider Identifier - a unique identification number for healthcare providers.
num_pt: Number of patients (individuals) in the dataset.
num_pt_Other: Number of patients of other or unspecified racial backgrounds.
num_pt_White: Number of patients identified as White.
num_pt_Black: Number of patients identified as Black.
num_pt_Asian: Number of patients identified as Asian.
num_pt_Race_Unknown: Number of patients with unknown racial information.
num_pt_Race_Non_White: Number of patients belonging to non-White racial groups.
num_pt_Hispanic: Number of patients identified as Hispanic.
num_pt_Not_Hispanic: Number of patients not identified as Hispanic.
num_pt_Ethnicity_Unknown: Number of patients with unknown ethnicity information.
When asked about the data, your response should include a python code that describes the dataframes provided.
Using the provided dataframes and no other dataframes, return the python code and make sure to prefix the requested 
python code with {START_CODE_TAG} exactly and suffix the code with {END_CODE_TAG} exactly to get the answer to the following question:
"""  # noqa: E501

    def __init__(self, dataframes: list[pd.DataFrame]):
        for i, dataframe in enumerate(dataframes, start=1):
            row, col = dataframe.shape

            self.text += f"""
This is the metadata of the dataframe df{i}:
{dataframe}"""

        self.text += self.instruction
        self.text = self.text.format(
            START_CODE_TAG=START_CODE_TAG,
            END_CODE_TAG=END_CODE_TAG,
        )

    def __str__(self):
        return self.text

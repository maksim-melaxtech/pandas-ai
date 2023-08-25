""" Prompt to generate Python code for multiple dataframes """


import pandas as pd

from pandasai.constants import END_CODE_TAG, START_CODE_TAG
from .base import Prompt


class MultipleDataframesPrompt(Prompt):
    """Prompt to generate Python code"""

    text: str = """
You are provided with the following pandas dataframes:"""
    instruction: str = """

    These are column descriptions for df1:
npi: National Provider Identifier.
physician_name: Name of the physician or healthcare provider.
specialty: Medical specialty or field of practice.
physician_email: Email address of the physician.
physician_phone: Phone number of the physician.
physician_degrees: Academic degrees held by the physician.
state_full_name: Full name of the state where the physician practices.
physician_primary_practice_address: Primary practice address of the physician.
physician_zip3: Zip code prefix of the physician's practice location.
Primary_Hco_Affiliation: Main healthcare organization the physician is affiliated with.
Org_Type: Type of healthcare organization.
Classification: Classification of the healthcare organization.
test_pt: Number of children with lipid testing seen by this physician
untest_pt: Number of children without lipid testing seen by this physician
total_pt: Total number of children seen by this physician
unscreen_rate: Percent not receiving lipid testing seen by this physician. 
num_trials_total: Total number of clinical trials associated with the physician.
num_trials_ongoing: Number of ongoing clinical trials associated with the physician.
num_trials_past: Number of completed or past clinical trials associated with the physician.
num_pub_total: Total number of publications associated with the physician.
num_pub_last5yr: Number of publications in the last five years associated with the physician.
physician_trialtrove_url: URL to the physician's profile on TrialTrove.

These are column descriptions for df2. Use this dataframe if asked about unique patients:
ZIP3: Zip code prefix of a physician's practice location.
test_pt_zip3: Number of unique children patients with lipid testing in the zip code prefix.
total_pt_zip3: Number of unique total children patients in the zip code prefix.
untest_pt_zip3: Number of unique children patients without lipid testing in the zip code prefix.
unscreen_rate_zip3: Percent of patients not receiving lipid testing in the zip code prefix.

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

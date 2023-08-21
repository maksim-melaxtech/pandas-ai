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
physician_disease_tiers: Disease tiers specialized by the physician.
state_full_name: Full name of the state where the physician practices.
physician_primary_practice_address: Primary practice address of the physician.
physician_zip3: Zip code prefix of the physician's practice location.
primary_organization_affiliation: Main healthcare organization the physician is affiliated with.
organization_type: Type of healthcare organization.
organization_classification: Classification of the healthcare organization.
num_pt: Total number of patients associated with the physician.
num_pt_Other: Number of patients of other or unspecified racial backgrounds.
num_pt_White: Number of patients identified as White.
num_pt_Black: Number of patients identified as Black.
num_pt_Asian: Number of patients identified as Asian.
num_pt_Race_Unknown: Number of patients with unknown racial information.
num_pt_Race_Non_White: Number of patients belonging to non-White racial groups.
num_pt_Hispanic: Number of patients identified as Hispanic.
num_pt_Not_Hispanic: Number of patients not identified as Hispanic.
num_pt_Ethnicity_Unknown: Number of patients with unknown ethnicity information.
num_trials_total: Total number of clinical trials associated with the physician.
num_trials_ongoing: Number of ongoing clinical trials associated with the physician.
num_trials_past: Number of completed or past clinical trials associated with the physician.
num_pub_total: Total number of publications associated with the physician.
num_pub_last5yr: Number of publications in the last five years associated with the physician.
physician_trialtrove_url: URL to the physician's profile on TrialTrove.

These are column descriptions for df2. Use this dataframe if asked about unique patients in zip3 areas:
physician_zip3: Zip code prefix of a physician's practice location.
num_pt_zip3: Total number of unique patients associated with the zip code prefix.
num_pt_Asian_zip3: Count of unique patients with Asian racial background in the zip code prefix.
num_pt_Black_zip3: Count of unique patients with Black racial background in the zip code prefix.
num_pt_Other_zip3: Count of unique patients with other or unspecified racial backgrounds in the zip code prefix.
num_pt_White_zip3: Count of unique patients identified as White in the zip code prefix.
num_pt_Race_Unknown_zip3: Count of unique patients with unknown racial information in the zip code prefix.
num_pt_Hispanic_zip3: Count of unique patients identified as Hispanic in the zip code prefix.
num_pt_Not_Hispanic_zip3: Count of unique patients not identified as Hispanic in the zip code prefix.
num_pt_Ethnicity_Unknown_zip3: Count of unique patients with unknown ethnicity information in the zip code prefix.

These are column descriptions for df3. Use this dataframe if asked about unique patients in States:
state_full_name: Full name of the state where the physician practices.
num_pt_state: Total number of unique patients associated with the state.
num_pt_Asian_state: Count of unique patients with Asian racial background in the state.
num_pt_Black_state: Count of unique patients with Black racial background in the state.
num_pt_Other_state: Count of unique patients with other or unspecified racial backgrounds in the state.
num_pt_White_state: Count of unique patients identified as White in the state.
num_pt_Race_Unknown_state: Count of unique patients with unknown racial information in the state.
num_pt_Hispanic_state: Count of unique patients identified as Hispanic in the state.
num_pt_Not_Hispanic_state: Count of unique patients not identified as Hispanic in the state.
num_pt_Ethnicity_Unknown_state: Count of unique patients with unknown ethnicity information in the state.

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

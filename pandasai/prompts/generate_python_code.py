""" Prompt to generate Python code
```
You are provided with a pandas dataframe (df) with {num_rows} rows and {num_columns} columns.
This is the metadata of the dataframe:
{df_head}.

When asked about the data, your response should include a python code that describes the
dataframe `df`. Using the provided dataframe, df, return the python code and make sure to prefix
the requested python code with {START_CODE_TAG} exactly and suffix the code with {END_CODE_TAG}
exactly to get the answer to the following question:
```
"""  # noqa: E501


from pandasai.constants import END_CODE_TAG, START_CODE_TAG
from .base import Prompt


class GeneratePythonCodePrompt(Prompt):
    """Prompt to generate Python code"""

    text: str = """
You are provided with a pandas dataframe (df) with {num_rows} rows and {num_columns} columns.
This is the metadata of the dataframe:
{df_head}.
These are column descriptions:

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

num_pt: Number of total patients physician is treating.
num_pt_Other: Number of patients of other or unspecified racial backgrounds.
num_pt_White: Number of patients identified as White.
num_pt_Black: Number of patients identified as Black.
num_pt_Asian: Number of patients identified as Asian.
num_pt_Race_Unknown: Number of patients with unknown racial information.
num_pt_Race_Non_White: Number of patients belonging to non-White racial groups.
num_pt_Hispanic: Number of patients identified as Hispanic.
num_pt_Not_Hispanic: Number of patients not identified as Hispanic.
num_pt_Ethnicity_Unknown: Number of patients with unknown ethnicity information.

num_trials_total: Total number of clinical trials associated with the healthcare provider.
num_trials_ongoing: Number of ongoing clinical trials associated with the healthcare provider.
num_trials_past: Number of completed or past clinical trials associated with the healthcare provider.

num_pub_total: Total number of publications associated with a physician or healthcare provider.
publications_last_5_years: Number of publications associated with a physician or healthcare provider in the last five years.
physician_pubmed_url: URL or link to the physician's profile or publications on the PubMed database.

When asked about the data, your response should include a python code that describes the dataframe `df`.
Using the provided dataframe, df, return the python code and make sure to prefix the requested python code with {START_CODE_TAG} exactly and suffix the code with {END_CODE_TAG} exactly to get the answer to the following question:
"""  # noqa: E501

    def __init__(self, **kwargs):
        super().__init__(
            **kwargs, START_CODE_TAG=START_CODE_TAG, END_CODE_TAG=END_CODE_TAG
        )

# Allows variables to be declared with a specific set of values that can be accepted
from typing import Literal
# BaseModel coordinates the validation of the data and validates the AI model's output
from pydantic import BaseModel, Field

# The code below is the "data contract" for the agent.  It tells Pydantic and Gemini what info to extract from unstrctured text, what format it has to be in, and what rules (inside the Field(...)) it has to follow. The description gives instructions to Gemini about what the field represents so that it knows how to categorize the information correctly.

# A custom class (blueprint) is created called EnterpriseTicketExtraction and using BaseModel, turns this into an automated validation engine so that all of the defined rules in the class are checked.

# Within this class, there are 4 attributes that Gemini will pull out of the raw data.  It will decide and return a value from one of the preset options (if defined) and/or provide some text output which follows the rules stated in the description.

class EnterpriseTicketExtraction(BaseModel):
    category: Literal["Hardware", "Software", "Security", "Billing", "General Inquiry"] = Field(
        description="The primary domain or technical category of the ticket."
    )
    urgency_level: Literal["Low", "Medium", "High", "Critical"] = Field(
        description="The priority or urgency level based on business impact."
    )
    summary: str = Field(
        description="A concise 1-2 sentence summary of the core issue."
    )
    action_items: list[str] = Field(
        description="A list of actionable steps or next actions required to resolve the ticket."
    )
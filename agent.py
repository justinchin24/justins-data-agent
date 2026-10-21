# Imports Python's built-in operating system module (used behind the scenes by dotenv to look at your computer's environment variables).
import os
# Imports Python's logging module, which provides messages, warnings, and errors with timestamps and severity levels (e.g., INFO, WARNING, ERROR)
import logging
# Imports the load_dotenv function, which reads your .env file and securely loads the GEMINI_API_KEY into the script's environment.
from dotenv import load_dotenv
# Imports the official, modern Google GenAI SDK (google-genai), which lets you interact with Gemini models.
from google import genai
# Imports your custom Pydantic class from your schemas.py file so the agent knows what structure to expect back from the AI.
from schemas import EnterpriseTicketExtraction

# Look for the .env file and find the API key to make it accessible to the application
load_dotenv()

# Attach API key to each request
client = genai.Client()

# Organizes the output logs into a nicely formatted audit trail for severity levels of INFO or higher.  It will show the date and time, severity level, and actual error message.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# This function takes raw text as input, sends it to Gemini, and returns output using the class that was defined in schemas.py
def process_support_ticket(raw_ticket_text: str) -> EnterpriseTicketExtraction:

# This prompt/instruction is for the AI agent to use when taking in the text from the user.
    prompt = f"""
    Analyze the following IT support ticket and extract the required structured information.
    
    Support Ticket:
    {raw_ticket_text}
    """

    # This tells Python to try running the code below, which prints a log message using the basic config format declared above.  If there is an issue, don't crash the program but go down to the 'except' block of code
    try:
        logging.info("Sending support ticket to Gemini for extraction...")

    # Call Gemini and tells it to return the output in a structured format and follow the fields, types, and rules in EnterpriseTicketExtraction
        response = client.models.generate_content(
            model='gemini-3.5-flash-lite',
            contents=prompt,
            config={
                'response_mime_type': 'application/json',
                'response_schema': EnterpriseTicketExtraction,
            },
        )

    # Prints another log message with INFO as the severity and the specific message below after the raw data is sent to Gemini
        logging.info("Successfully extracted and validated structured data.")
    # Returns the output in the format specified in the defined class (in schemas.py)
        return response.parsed

    # except Exception tells Python to catch any runtime errors that took place inside the 'try' code block above
    except Exception as e:
        logging.error(f"An error occurred while processing the support ticket: {e}")
        raise

# Code below runs only when testing directly in the terminal
if __name__ == "__main__":
    sample_ticket = "My computer is stuck on a blue screen and I am unable to work.  Please investigate and resolve."
    
    print("Sending sample ticket to Gemini...")
    result = process_support_ticket(sample_ticket)
    
    print("\n--- Extracted Structured Result ---")
    print(f"Category: {result.category}")
    print(f"Urgency: {result.urgency_level}")
    print(f"Summary: {result.summary}")
    print(f"Action Items: {result.action_items}")
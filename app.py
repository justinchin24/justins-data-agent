import streamlit as st
# Imports the function of the same name from agent.py
from agent import process_support_ticket

# Configures browser tab settings - page title, emoji, and using the full width of the screen
st.set_page_config(page_title="Enterprise Support Data Agent", page_icon="🤖", layout="wide")

# Displays a title and instructions
st.title("🤖 Enterprise Support Data Agent")
st.markdown("Paste an unformatted IT support ticket below to extract structured JSON data via Gemini and Pydantic.")

# Interactive text box for the user to type in content. It defines the field name, size, and helper text that is displayed by default in the box itself before the user types anything in. What is entered here is passed to raw_ticket_text in agent.py 
raw_ticket = st.text_area("Raw Support Ticket Input", height=150, placeholder="Paste your IT support ticket here...")

# Displays a clickable button called "Process Ticket" with primary styling.
if st.button("Process Ticket", type="primary"):
    # Validates that the user has entered text and takes away any leading or trailing spaces
    if raw_ticket.strip():
        # Displays an animated spinner icon while the code in agent.py is running to show the user that something is happening
        with st.spinner("Analyzing ticket with Gemini..."):
            try:
                # Call your core function from agent.py
                result = process_support_ticket(raw_ticket)

                # Shows a green success banner at the top of the screen
                st.success("Successfully extracted and validated structured data!")
                
                # Display structured results in 2 columns
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("Extracted Details")
                    st.metric(label="Category", value=result.category)
                    st.metric(label="Urgency Level", value=result.urgency_level)
                    st.markdown(f"**Summary:** {result.summary}")
                
                with col2:
                    st.subheader("Action Items")
                    # Lists the action items in sequential order
                    for idx, item in enumerate(result.action_items, 1):
                        st.markdown(f"{idx}. {item}")

                # Creates a collapsable dropdown menu which automatically formats and displays the JSON using the model defined in schemas.py        
                with st.expander("View Raw JSON Output"):
                    st.json(result.model_dump())

            # Displays an error message to the end user on the web page if something goes wrong        
            except Exception as e:
                st.error(f"Failed to process ticket: {e}")
    # Asks the user to type in text if they try to submit a blank form
    else:
        st.warning("Please enter a support ticket before processing.")
# ########################
# testing gemini code
#
#
#########################
from pyscript.dom import Element
import js

# Define the functions that are called by the button's 'onclick' handler.
# These functions MUST be available in the global scope (i.e., not nested inside a class).
def startup_function():
    # This import should now succeed
    output_element = Element('output') 
    
    output_element.write("✅ PyScript DOM is working! Run on startup successful.")
    js.console.log("pyscript.dom check passed.")
def handle_query_1():
    """
    Function to run a specific database query (Query A) and update the HTML.
    """
    print("--- Running Function A: Handle Query 1 ---")
    
    # *** Add your main logic here ***
    # e.g., db_result = run_db_query("SELECT * FROM table_a")
    
    # Get the output area element
    output_element = Element("output-area")
    
    # Update the content of the HTML <p id="output-area"></p> tag
    output_element.write("✅ Query A has been executed and results are displayed.")
    
    # Optional: Alert the user using the browser's alert box
    js.alert("Query A complete!")

def handle_query_2():
    """
    Function to run a different database query (Query B).
    """
    print("--- Running Function B: Handle Query 2 ---")
    
    # *** Add your main logic here ***
    # e.g., db_result = run_db_query("INSERT INTO log VALUES ('Button Clicked')")
    
    output_element = Element("output-area")
    output_element.write("➕ Query B has been executed.")
    js.alert("Query B complete!")
    
# You can define other utility functions here that are not directly linked to a button
def setup_application():
    print("Application initialized. Waiting for button clicks...")

# Call setup function to run on start
setup_application()

# When PyScript runs, it automatically makes functions defined at the top level
# (like handle_query_1 and handle_query_2) accessible to the JavaScript environment,
# which is why the HTML 'onclick' attribute can call them directly.
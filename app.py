import gradio as gr

# Define your function
def greet(name):
    return f"Hello {name}!"

# Create the Gradio interface
demo = gr.Interface(
    fn=greet,                 # Function to call
    inputs="image",            # Input type
    outputs="image"            # Output type
)

# Launch the app
demo.launch()


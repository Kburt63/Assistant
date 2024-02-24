# Description: This file contains the code to create an assistant using the OpenAI API.
from argparse import FileType
from calendar import c
from email import message
from genericpath import exists
from mailbox import Message
from math import e
from re import A
import re
from ssl import Purpose
from threading import Thread
from click import File
#from nbconvert import PDFExporter
from openai import OpenAI
#from sk import my_sk
import time
import os
import json

api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is available
if api_key is None:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Create an OpenAI client
client = OpenAI(api_key=api_key)

# Create a list to store the file IDs
file_ids = []

existing_ids = []

exists_flag = 0

thread = Thread()

run = None

user_message = ""

file1 = File()
file2 = File()
file3 = File()
file4 = File()
file5 = File()
file6 = File()
file7 = File()
file8 = File()
file9 = File()

def check_id_file_exists():
    try:
        with open('file_ids.txt', 'r') as file:
            for line in file:
                existing_ids.append(line.strip())  # Remove newline characters
            exists_flag = 1
    except FileNotFoundError:
        print("File not found. Will create a new one if a new ID is added.")
        exists_flag = 0
    return exists_flag, existing_ids

def save_file_ids(file_ids):
    # Specify the path to the file where you want to save the IDs
    file_path = 'file_ids.txt'    
    # Open the file in write mode (this will overwrite existing content)
    with open(file_path, 'w') as file:
        # Iterate over each ID in the list of file IDs
        for file_id in file_ids:
            # Write each ID to the file, followed by a newline character
            file.write(file_id + '\n')   
        print(f"File IDs have been saved to {file_path}")

def upload_files():
    if exists_flag == 1:
        print("File exists")
        # Read the file IDs from the file
        file_ids = existing_ids
        return file_ids   
    elif exists_flag == 0:    
        # upload files
        with open("files/How_to_Coach_author_Mind_Tools.pdf", "rb") as file:
            response = client.files.create(file=file, purpose="assistants")
        file_ids.append(response.id)
        
        with open("C:/Users/k-bur/Desktop/python_work/Assistant/files/4 Coaching Fundamentals author Ana Karakusevic.pdf", "rb") as file:
            response = client.files.create(file=file, purpose="assistants")
        file_ids.append(response.id)
        
        with open("C:/Users/k-bur/Desktop/python_work/Assistant/files/1. Book Psychiatry Author Dr Harsh Vardhan Dr Jagdish Prasad Dr R C Jiloha.pdf", "rb") as file:
            response = client.files.create(file=file, purpose="assistants")
        file_ids.append(response.id)
        
        with open("C:/Users/k-bur/Desktop/python_work/Assistant/files/3 Mentoring and coaching author Alexa Michae.pdf", "rb") as file:
            response = client.files.create(file=file, purpose="assistants")
        file_ids.append(response.id)
        
        with open("C:/Users/k-bur/Desktop/python_work/Assistant/files/5 Critical Psychiatry A Brief Overview Author Hugh Middleton Joanna Moncrieff.pdf", "rb") as file:
            response = client.files.create(file=file, purpose="assistants")
        file_ids.append(response.id)
        
        with open("C:/Users/k-bur/Desktop/python_work/Assistant/files/8 Coaching Employees Toward better performarce author Helpside.pdf", "rb") as file:
            response = client.files.create(file=file, purpose="assistants")
        file_ids.append(response.id)
        
        with open("C:/Users/k-bur/Desktop/python_work/Assistant/files/12 Coaching Employees to Reach Optimal Performance author  Deloitte US.pdf", "rb") as file:
            response = client.files.create(file=file, purpose="assistants")
        file_ids.append(response.id)
        
        with open("C:/Users/k-bur/Desktop/python_work/Assistant/files/19 Emotion Coaching author Media & File Management.pdf", "rb") as file:
            response = client.files.create(file=file, purpose="assistants")
        file_ids.append(response.id)
        
        with open("C:/Users/k-bur/Desktop/python_work/Assistant/files/21 Coaching to personality types author Mnia.pdf", "rb") as file:
            response = client.files.create(file=file, purpose="assistants")
        file_ids.append(response.id)
        
        file1 = client.files.retrieve(file_ids[0])
        file2 = client.files.retrieve(file_ids[1])
        file3 = client.files.retrieve(file_ids[2])
        file4 = client.files.retrieve(file_ids[3])
        file5 = client.files.retrieve(file_ids[4])
        file6 = client.files.retrieve(file_ids[5])
        file7 = client.files.retrieve(file_ids[6])
        file8 = client.files.retrieve(file_ids[7])
        file9 = client.files.retrieve(file_ids[8])
        
        # Save the file IDs to a file
        save_file_ids(file_ids),
        return file1, file2, file3, file4, file5, file6, file7, file8, file9
    else:
        print("Error")

def create_assistant():
    
    assistant_id_file = "files/assistant_id_4.txt"
    
    # Check if the assistant ID file exists
    if os.path.exists(assistant_id_file):
    # Read the assistant ID from the file
        with open(assistant_id_file, "r") as file:
            assistant_id = file.read().strip()
    else:
        # Create an Assistant with custom function definitions
        assistant = client.beta.assistants.create(
            name="Coach Psych",
            description="A personal psychiatric coch to help you with your mental health issues.",
            instructions="""
                Functioning as a HELPFUL, friendly, psychiatric coach, you provide SUPPORT to the user in ways like: by helping them to understand their diagnosis, 
                helping them prepare for a visit with one of their providers, and providing them with FEEDBACK when they want to explore ideas. A provider would be 
                a psychiatrist, a therapist, or a human psychiatric coach. As you are not a provider, you would not provide psychiatric advice. You would however 
                provide information and support. The user has c-ptsd. and has a psychiatric coach named Megan, a Therapist named Gail, and a nurse practitioner named Rachael.

                You reply in a CONVERSATIONAL way.
                """,
            tools=[{"type": "retrieval"}],
            file_ids=[file1.id, file2.id, file3.id, file4.id, file5.id, file6.id, file7.id, file8.id, file9.id],
            model="gpt-3.5-turbo-0125",
        )

        print(f"Assistant created with ID: {assistant.id}")
        assistant_id = assistant.id
        # Write the assistant ID to a file
        with open(assistant_id_file, "w") as file:
          file.write(assistant.id)
        print(f"Assistant ID written to file: {assistant_id_file}")

    assistant = client.beta.assistants.retrieve(assistant_id)
    print(f"Assistant retrieved with ID: {assistant.id}")
          
    return assistant
    
    # create thread (i.e. object that handles conversation between user and assistant)
def create_thread():
    print("Creating a Thread for a new user conversation...")
    thread = client.beta.threads.create()
    print(f"Thread created with ID: {thread.id}")
    return thread

#def create_message(thread, user_message):
#    print(f"Adding user's message to the Thread: '{user_message}'") 
#    message = client.beta.threads.messages.create(
##        thread_id=thread.id,
#        role="user",
##        content=user_message
#)

def send_message_and_run_assistant(thread, assistant, user_message):
    print(f"Adding user's message to the Thread: '{user_message}'")
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_message,
    )
    print("Running the Assistant to process the message..."),
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )
    print(f"Assistant run created with ID: {run.id}")
    return run

# Poll the Run status and handle function calls
def poll_run_status(thread, run):
    while True:
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        if run.status in ['completed', 'failed', 'cancelled']:
            break
        elif run.status == 'requires_action':
            handle_required_actions(thread, run)
        else:
            print("Waiting for the Assistant to process...")
            time.sleep(5)
    return run

# Handle the required actions for function calls
def handle_required_actions(thread, run):
    print("Assistant requires function calls...")
    required_actions = run.required_action.submit_tool_outputs
    with open("required_actions.json", "w") as f:
                required_actions_json = required_actions.model_dump()
                json.dump(required_actions_json, f, indent=4)
    tool_outputs = []

    for action in required_actions.tool_calls:
        func_name = action.function.name
        arguments = json.loads(action.function.arguments)
        if func_name == "retrieval":
            output = "I am a retrieval function"
        else:    
            raise ValueError(f"Unknown function: {func_name}")

        print(f"Function '{func_name}' called with arguments: {arguments}, output: {output}")
        tool_outputs.append({
            "tool_call_id": action.id,
            "output": output
        })

    print("Submitting function call outputs back to the Assistant...")
    client.beta.threads.runs.submit_tool_outputs(
        thread_id=thread.id,
        run_id=run.id,
        tool_outputs=tool_outputs,
    )

def display_final_response(thread, run):
    messages = client.beta.threads.messages.list(
    thread_id=thread.id,
    )
    run_steps = client.beta.threads.runs.steps.list(
      thread_id=thread.id,
      run_id=run.id
    )
    message_retrieved = client.beta.threads.messages.retrieve(
         thread_id=thread.id,
         message_id=messages.data[0].id
    )
    #from PIL import Image
    #import io
    # Initialize a list to store updated messages
    updated_messages = []

    image_counter = 0
    # Process each message in the messages list
    for message in messages.data:
        if message.content:
            citations = []
            for content_part in message.content:
                if content_part.type == 'text':
                    annotations = content_part.text.annotations
                    text_value = content_part.text.value
                    for index, annotation in enumerate(annotations):
                        text_value = text_value.replace(annotation.text, f' [{index}]')
                        if (file_citation := getattr(annotation, 'file_citation', None)):
                            cited_file = client.files.retrieve(file_citation.file_id)
                            citations.append(f'[{index}] {file_citation.quote} from {cited_file.filename}')
                        #elif (file_path := getattr(annotation, 'file_path', None)):
                         #   cited_file = client.files.retrieve(file_path.file_id)
                         #   citations.append(f'[{index}] Click <here> to download {cited_file.filename}')
                            #image_file_id = cited_file.id
                            #image_data: bytes = client.files.with_raw_response.retrieve_content(image_file_id).content
                            #image = Image.open(io.BytesIO(image_data))
                            #image.show()
                            # save the image to a file
                            #image.save(f"image_{image_counter}.png")
                            #image_counter += 1     
                    text_value += '\n' + '\n'.join(citations)
                    content_part.text.value = text_value
                #elif content_part.type == 'image_file':
                    #image_file_id = content_part.image_file.file_id
                    #image_data: bytes = client.files.with_raw_response.retrieve_content(image_file_id).content
                    #image = Image.open(io.BytesIO(image_data))
                    #image.show()
                    # save the image to a file
                    #image.save(f"image_{image_counter}.png")
                    #image_counter += 1
            updated_messages = [message]+updated_messages
    for updated_message in updated_messages:
        print(message.content)

if __name__ == "__main__":
    client = OpenAI(api_key=api_key)
    
    # Initialize the Assistant and Thread
    assistant = create_assistant()
    thread = create_thread()
    exists_flag, existing_ids = check_id_file_exists()
    # Upload files
    upload_files()

    while True:
        # Get user input
        user_message = input("Enter your message: ")
        
        # Check if the user wants to quit
        if user_message.lower() == "quit":
            break
        
        # Send a message and run the Assistant
        run = send_message_and_run_assistant(thread, assistant, user_message)
        
        # Poll the run for status updates and handle function calls
        run = poll_run_status(thread, run)
        
        # Display the final response
        display_final_response(thread, run)

if exists_flag == 0:
    #delete the file
    file1.id = file_ids[0]
    file2.id = file_ids[1]
    file3.id = file_ids[2]
    file4.id = file_ids[3]
    file5.id = file_ids[4]
    file6.id = file_ids[5]
    file7.id = file_ids[6]
    file8.id = file_ids[7]
    file9.id = file_ids[8]

    client.files.delete(file1.id)
    client.files.delete(file2.id)
    client.files.delete(file3.id)
    client.files.delete(file4.id)
    client.files.delete(file5.id)
    client.files.delete(file6.id)
    client.files.delete(file7.id)
    client.files.delete(file8.id)
    client.files.delete(file9.id)
    print("Files deleted")
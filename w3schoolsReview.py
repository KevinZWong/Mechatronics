# Python Lab - Scratch Pad
# Use this template to try some code... Use it as a scratch pad.
# Remember To Copy Your Edited Code To Your GitHub
# https://github.com/

# Add Any Header Comments, Versioning & License
# Add a Comment Here to describe/explain what you are doing 
# What is the purpose of this code… Document It

# Your Code Starts Here:
# Include any Libraries
# Declare Any Global Variables


'''
Hi Mr. Burnham this is a program that recursively generates topics and stores them in a tree structure.
I designed it to make it super easy to generate topics that were related to each other.

'''
    
import os
import json
from openai import OpenAI
import os
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
from dotenv import load_dotenv
class ScriptGenerator:
    def __init__(self, engine="gpt-4"):
        load_dotenv(dotenv_path='/home/kevin/Desktop/PARSE/VMAC/.env')
        self.engine = engine

    def generate_topics(self, topic , amount ,max_tokens=4000, temperature=1):
        prompt = f"""Write a list of {amount} interesting topics related to {topic}. 
        The style of topics is intresting. Respond with just the topics separated 
        by a comma, no numbers."""

        completion = client.chat.completions.create(model="gpt-4", messages=[{"role": "user", "content": prompt}])
        return  completion.choices[0].message.content

    def generate_script(self, prompt ,max_tokens=4000, temperature=1):
        completion = client.chat.completions.create(model="gpt-4", messages=[{"role": "user", "content": prompt}])
        return  completion.choices[0].message.content
        return response.choices[0].text.strip()
    def generate_image_description(self, segment ,max_tokens=4000, temperature=1):
        prompt = """
Your are now an ai program designed to turn simple sentences into descriptions of an art piece.
You will give responses that answer the following questions

How is the photo composed?
What is the emotional vibe of the image?
How much depth of field
How is the subject lit? Where from? How much light?
Artificial or natural light? What color? What time of day?
Where is this shot? In a studio or out in the world?

Example 1:
Given sentence:
“Steve jobs was a visionary”
Response:
A close-up, black & white studio photographic portrait of steve jobs, dramatic background

Example 2:
Given sentence:
“The sun is such a beautiful time to walk your dog”
Response:
“A vibrant photograph of a corgi dog, wide shot, outdoors, sunset photo at golden hour, wide-angle lens, soft focus”

You must follow the following orders
mimic these examples as closely as possible
Limit your responses to a maximum of 30 words
The art pieces you describe should be on earth 
The art pieces you describe must be a scenic view outdoors
They must be extremely lifelike and realistic
Your first sentence is:


        """
        #prompt += ". digital art"
        prompt += segment
        completion = client.chat.completions.create(model="gpt-4", messages=[{"role": "user", "content": prompt}])
        return  completion.choices[0].message.content
        return response.choices[0].text.strip()


    def manualSelection(self, data):
        returnList = []
        for story in data:
            print(story[0])
            print(story[1])
            input1 = input("Y or N: ")
            if (input1.upper() == "Y"):
                returnList.append(story)
        return returnList
    
    
    def construct_upload_string(self, file_path, title, description, keywords, category, privacy_status):
        upload_string = 'python upload_video.py '

        upload_string += '--file="{}" '.format(file_path)
        upload_string += '--title="{}" '.format(title)
        upload_string += '--description="{}" '.format(description)
        upload_string += '--keywords="{}" '.format(keywords)
        upload_string += '--category="{}" '.format(category)
        upload_string += '--privacyStatus="{}"'.format(privacy_status)

        return upload_string
    



class TopicTree:
    def __init__(self, topic):
        self.topic = topic
        self.children = []
        self.ScriptGen = ScriptGenerator()

    def add_child(self, child):
        self.children.append(child)

    def expand_recursively_helper(self, levels, num_children, level=0):
        if levels <= 0:
            return
        subtopicsList = self.ScriptGen.generate_topics(self.topic, num_children)
        subtopicsList = subtopicsList.split(",")
        for i, subtopic in enumerate(subtopicsList):
            indent = "  " * level
            print(f"{indent}Generated Level {levels}: {subtopic}")
            child = TopicTree(f"{subtopic}")
            self.add_child(child)
            child.expand_recursively(levels - 1, num_children, subtopic, level + 1)

    def expand_recursively(self, levels, num_children, given_subtopic, level=0):
        if levels <= 0:
            return
        subtopicsList = self.ScriptGen.generate_topics(given_subtopic, num_children)
        subtopicsList = subtopicsList.split(",")
        for i, subtopic in enumerate(subtopicsList):
            indent = "  " * level
            print(f"{indent}Generated Level {levels}: {subtopic}")
            child = TopicTree(f"{subtopic}")
            self.add_child(child)
            child.expand_recursively(levels - 1, num_children, subtopic, level + 1)


    def save_to_file(self, filename):
        def serialize(node):
            return {'topic': node.topic, 'children': [serialize(child) for child in node.children]}

        with open(filename, 'w') as file:
            json.dump(serialize(self), file, indent=4)
    @staticmethod
    def load_from_file(filename):
        def deserialize(node_data):
            node = TopicTree(node_data['topic'])
            for child_data in node_data['children']:
                node.add_child(deserialize(child_data))
            return node

        with open(filename, 'r') as file:
            data = json.load(file)
            return deserialize(data)
    def get_leaf_nodes(self):
        """
        Retrieves all leaf nodes in the tree.
        """
        # If the current node has no children, it's a leaf node.
        if not self.children:
            return [self]

        # Otherwise, collect leaf nodes from all children.
        leaves = []
        for child in self.children:
            leaves.extend(child.get_leaf_nodes())
        
        return leaves

    def __str__(self, level=0):
        ret = "  " * level + str(self.topic) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    

'''
# Example Usage
root = TopicTree("Science")

# Expand the tree for 3 levels with each node having 2 children
root.expand_recursively_helper(3, 3)
root.save_to_file("tree.json")

# Print the tree structure
print(root)
'''
'''
loaded_tree = TopicTree.load_from_file("tree.json")

# Print the loaded tree structure
leaves = loaded_tree.get_leaf_nodes()
for i in leaves:
    print(i.topic)
'''

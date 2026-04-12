# Importing pyGitHub API
from github import Github, Auth
import config as config

# Secure way to use API key from config.py
# Couldnt get auth working so added AUTH.TOKEN
auth = Auth.Token(config.apikeys["githubkey"])
g = Github(auth=auth)

# Get the repository
repo = g.get_user().get_repo('WSAA-coursework')

# Get the file content
file_content = repo.get_contents("assignments/file.txt")
#print(file_content.decoded_content.decode("utf-8")) 

# Getting bytes content and decoding it to string
decoded_content = file_content.decoded_content.decode("utf-8")
#print(decoded_content)

# Replace "Andrew" with my name
updated_content = decoded_content.replace("Andrew", "Dima")
print(updated_content)

# Using sha, as it is required by GitHub API to prevent conflicts
# Update the file in the repository
repo.update_file(file_content.path, "Updated file.txt", updated_content, file_content.sha)



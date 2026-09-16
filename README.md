# Git & GitHub Assignment — Flask and MongoDB Project

## 1. Project Overview

This project demonstrates a complete Git and GitHub workflow using a Flask web application integrated with MongoDB.

The project was developed to practice practical Git operations such as SSH authentication, repository cloning, branch creation, commits, pushing, merging, merge conflict resolution, sequential commits, soft reset, and rebasing.

The Flask application also provides a JSON API, a To-Do frontend, and a MongoDB-backed To-Do submission API.

---

## 2. Project Details

**Student Name:** Narinder Kumar  
**Project Name:** Git_and_GitHub_Narinder  
**GitHub Username:** Narinder-code17

**GitHub Repository:**

https://github.com/Narinder-code17/Git_and_GitHub_Narinder

**SSH Repository:**

git@github.com:Narinder-code17/Git_and_GitHub_Narinder.git

---

## 3. Objectives

The main objectives of this assignment are:

- Create and configure a GitHub repository.
- Configure SSH authentication with GitHub.
- Clone a repository using SSH.
- Create and manage Git branches.
- Add and commit project files.
- Push branches and commits to GitHub.
- Merge branches into the main branch.
- Create and resolve merge conflicts.
- Work with multiple development branches.
- Implement a Flask To-Do frontend.
- Implement a Flask POST API.
- Store To-Do data in MongoDB.
- Create multiple sequential commits.
- Practice `git reset --soft`.
- Practice Git rebase.
- Maintain proper Git history.
- Document the complete workflow using screenshots.

---

## 4. Technologies Used

- Python
- Flask
- MongoDB
- PyMongo
- python-dotenv
- HTML
- Git
- GitHub
- Git Bash
- Visual Studio Code
- SSH

---

## 5. Project Structure

Git_and_GitHub_Narinder/
│
├── app.py
├── data.json
├── requirements.txt
├── .gitignore
├── .env.example
│
├── templates/
│   └── todo.html
│
├── screenshots/
│   ├── 01_ssh_key_added.png
│   ├── 02_ssh_connection.png
│   ├── 03_repository_clone.png
│   ├── 04_flask_server.png
│   ├── 05_flask_home.png
│   ├── 06_flask_api.png
│   ├── 07_git_configuration.png
│   ├── 08_username_branch.png
│   ├── 09_git_add_files.png
│   ├── 10_initial_commit.png
│   ├── 11_username_branch_push.png
│   ├── 12_main_branch_created.png
│   ├── 13_task1_merge.png
│   ├── 14_json_update_new_branch.png
│   ├── 15_json_update_commit.png
│   ├── 16_new_branch_push.png
│   ├── 17_main_json_change.png
│   ├── 18_main_json_commit.png
│   ├── 19_main_change_push.png
│   ├── 21_conflict_resolved.png
│   ├── 22_conflict_staged.png
│   ├── 23_conflict_merge_commit.png
│   ├── 24_task2_merge_push.png
│   ├── 25_task2_git_history.png
│   ├── 26_master1_branch.png
│   ├── 27_todo_frontend.png
│   ├── 28_master1_git_add.png
│   ├── 29_master1_commit.png
│   ├── 30_master1_push.png
│   └── Additional Task 3 and Task 4 screenshots
│
└── Git_and_GitHub_Narinder_Documentation.docx

---

# TASK 1 — GitHub Repository, SSH, Branching and Merging

## 6. GitHub Repository Creation

A new GitHub repository was created with the following details:

**Repository Name:**

Git_and_GitHub_Narinder

The repository was created to store the complete Flask project and demonstrate the required Git workflow.

---

## 7. SSH Key Generation

An ED25519 SSH key was generated for secure authentication with GitHub.

Command used:

ssh-keygen -t ed25519 -C "narinderkumar1517@gmail.com"

The generated files were:

- `id_ed25519`
- `id_ed25519.pub`

The private key was kept on the local system and was not shared.

The public key was added to GitHub.

---

## 8. Adding SSH Key to GitHub

The generated public key was added to:

GitHub → Settings → SSH and GPG keys → New SSH key

The SSH key was named:

My Windows PC

This allowed the local computer to authenticate with GitHub without using a GitHub password for Git operations.

---

## 9. Testing SSH Connection

SSH authentication was tested using:

ssh -T git@github.com

Successful output:

Hi Narinder-code17! You've successfully authenticated, but GitHub does not provide shell access.

This confirmed that SSH authentication was working correctly.

---

## 10. Cloning the Repository

The GitHub repository was cloned using the SSH URL.

Command:

git clone git@github.com:Narinder-code17/Git_and_GitHub_Narinder.git

The project directory was then opened:

cd Git_and_GitHub_Narinder

---

## 11. Git Configuration

Git username and email were configured using:

git config --global user.name "Narinder Kumar"

git config --global user.email "narinderkumar1517@gmail.com"

The configuration was verified using:

git config --list

---

## 12. Creating the Username Branch

A branch named after the GitHub username was created.

Command:

git switch -c Narinder-code17

The branch name was:

Narinder-code17

This branch was used for the initial Flask project implementation.

---

## 13. Flask Project Files

The initial Flask project included:

- `app.py`
- `data.json`
- `requirements.txt`
- `.gitignore`
- Flask application files

The files were added to Git using:

git add .

---

## 14. Initial Commit

The initial Flask project was committed using:

git commit -m "Add initial Flask project"

The initial commit was:

75d8bcf Add initial Flask project

---

## 15. Pushing Username Branch

The username branch was pushed to GitHub:

git push -u origin Narinder-code17

The branch was successfully uploaded to the remote GitHub repository.

---

## 16. Creating the Main Branch

The main branch was created from the initial project history:

git switch -c main

The main branch was then pushed:

git push -u origin main

---

## 17. Merging the Username Branch

The username branch was merged into main:

git merge Narinder-code17

Git reported:

Already up to date.

This occurred because the username branch and main branch pointed to the same commit at that stage, so there were no additional changes to merge.

---

# TASK 2 — New Branch, JSON Update and Merge Conflict

## 18. Creating the New Branch

A new branch was created from main:

git switch main

git pull

git switch -c Narinder-code17_new

The new branch was:

Narinder-code17_new

---

## 19. Updating data.json on the New Branch

The `data.json` file was modified on the `Narinder-code17_new` branch.

A third student record was added:

{
    "id": 3,
    "name": "Student 3",
    "course": "Computer Science"
}

The modified file was staged:

git add data.json

---

## 20. Committing the JSON Update

The changes were committed:

git commit -m "Update API JSON data"

Commit created:

51d226e Update API JSON data

---

## 21. Pushing the New Branch

The new branch was pushed to GitHub:

git push -u origin Narinder-code17_new

---

## 22. Creating a Different Change on Main

The main branch was checked out:

git switch main

A different modification was made to `data.json`.

The course value for Student 2 was changed to:

Electronics and Communication Engineering

The change was committed:

git add data.json

git commit -m "Update main API data"

Commit created:

9e76303 Update main API data

---

## 23. Creating the Merge Conflict

The `Narinder-code17_new` branch was merged into main:

git merge Narinder-code17_new

Git detected a merge conflict in:

data.json

The conflict occurred because both branches had modified overlapping content in the same JSON file.

---

## 24. Resolving the Merge Conflict

The conflict was resolved by accepting the incoming changes from the `Narinder-code17_new` branch as required by the assignment.

The resolved file was then staged:

git add data.json

---

## 25. Creating the Conflict Resolution Commit

The merge conflict was completed with:

git commit -m "Merge Narinder-code17_new and resolve conflict"

Merge commit:

cb2436d Merge Narinder-code17_new and resolve conflict

---

## 26. Pushing the Resolved Main Branch

The updated main branch was pushed:

git push origin main

The conflict resolution was therefore stored in the GitHub repository.

---

## 27. Git History After Task 2

The Git history showed the following important commits:

cb2436d Merge Narinder-code17_new and resolve conflict

51d226e Update API JSON data

9e76303 Update main API data

75d8bcf Add initial Flask project

The history demonstrates the use of two branches, independent changes, conflict creation, conflict resolution, and a merge commit.

---

# TASK 3 — master_1 and master_2

## 28. Creating master_1

The latest main branch was checked out:

git switch main

git pull

A new branch was created:

git switch -c master_1

The `master_1` branch was used for the To-Do frontend.

---

## 29. Creating the To-Do Frontend

A new HTML file was created:

templates/todo.html

The frontend contains a To-Do form with:

- Item Name
- Item Description
- Submit button

The form uses:

<form action="/submittodoitem" method="POST">

The frontend is connected to the Flask backend POST endpoint.

---

## 30. Adding the To-Do Route

The Flask application was updated to include:

@app.route("/todo")
def todo():
    return render_template("todo.html")

The `render_template` function was imported from Flask.

The frontend was tested through:

http://127.0.0.1:5000/todo

---

## 31. Committing master_1 Changes

The frontend changes were staged:

git add templates/todo.html app.py

The changes were committed:

git commit -m "Create To-Do frontend"

Commit:

0088c98 Create To-Do frontend

---

## 32. Pushing master_1

The branch was pushed to GitHub:

git push -u origin master_1

---

# TASK 3 — master_2

## 33. Creating master_2

The main branch was checked out:

git switch main

git pull

The second development branch was created:

git switch -c master_2

The `master_2` branch was used to implement the MongoDB backend.

---

## 34. Installing MongoDB Dependencies

The following Python packages were installed:

Flask==3.0.2

pymongo==4.18.1

python-dotenv==1.0.1

The dependencies were recorded in:

requirements.txt

---

## 35. MongoDB Configuration

MongoDB Atlas was used for database storage.

The MongoDB connection string was stored in a local `.env` file.

The `.env` file was added to `.gitignore` to prevent credentials from being uploaded.

The `.env.example` file was created as a safe configuration template:

MONGO_URI=your_mongodb_connection_string_here

The actual MongoDB connection string was not included in the GitHub repository.

---

## 36. MongoDB Database and Collection

The Flask application connects to MongoDB using PyMongo.

Database:

git_github_db

Collection:

todo_items

The connection uses:

from pymongo import MongoClient

from dotenv import load_dotenv

The MongoDB URI is read from the environment:

mongo_uri = os.getenv("MONGO_URI")

The client is created using:

client = MongoClient(mongo_uri)

---

## 37. Implementing the POST API

The following endpoint was implemented:

POST /submittodoitem

The endpoint accepts:

- itemName
- itemDescription

The submitted information is stored in MongoDB.

The API validates that both fields are provided.

If either field is missing, the API returns:

{
    "error": "itemName and itemDescription are required"
}

with HTTP status:

400 Bad Request

---

## 38. MongoDB Insert Operation

The To-Do item is inserted using:

result = todo_collection.insert_one({
    "itemName": item_name,
    "itemDescription": item_description
})

The generated MongoDB ObjectId is returned to the client.

---

## 39. Successful API Response

The POST endpoint was successfully tested.

Example response:

{
    "itemId": "6aaa6b80dc6ef1b94f775519",
    "message": "To-Do item submitted successfully"
}

HTTP status:

201 Created

This confirms that the API successfully accepted the To-Do item and stored it in MongoDB.

---

## 40. master_2 Commit

The MongoDB backend implementation was committed:

git add app.py requirements.txt .env.example

git commit -m "Add MongoDB To-Do submission API"

Commit:

d273b20 Add MongoDB To-Do submission API

The branch was pushed to GitHub.

---

## 41. Merging master_1 and master_2

The development branches were merged into main.

During the merge, a conflict occurred in:

app.py

The conflict occurred because both branches modified the Flask application.

The conflict was resolved by retaining both required functionalities:

- `/todo`
- `/submittodoitem`

The resolved files were staged:

git add app.py .env.example requirements.txt

---

## 42. Merge Commit

The merge was completed using:

git commit -m "Merge master_2 into main"

Merge commit:

d68e32c Merge master_2 into main

The updated main branch was pushed:

git push origin main

---

# TASK 4 — Sequential Commits, Reset and Rebase

## 43. Adding Item ID

The `master_1` branch was used for the first Task 4 change.

An Item ID field was added to the To-Do form.

The Item ID field was made read-only.

The change was staged:

git add templates/todo.html

The first separate commit was created:

git commit -m "Add Item ID to To-Do form"

Commit:

e528291 Add Item ID to To-Do form

This was the first independent Task 4 commit.

---

## 44. Adding Item UUID

The Item UUID field was added separately below the Item ID.

The field contains a UUID value and is read-only.

The change was committed separately:

git add templates/todo.html

git commit -m "Add Item UUID to To-Do form"

Commit:

f4ceb6e Add Item UUID to To-Do form

This demonstrates the requirement of maintaining separate commits for separate changes.

---

## 45. Adding Item Hash

The Item Hash field was then added separately.

The hash field is read-only and contains a SHA-256-style hexadecimal value.

The change was staged:

git add templates/todo.html

The third separate commit was created:

git commit -m "Add Item Hash to To-Do form"

The three Task 4 changes were therefore developed as separate commits:

1. Add Item ID to To-Do form
2. Add Item UUID to To-Do form
3. Add Item Hash to To-Do form

---

## 46. Merging master_1 into Main

After completing the three individual commits, the `master_1` branch was merged into main.

The purpose of this merge was to bring the Task 4 changes into the main branch before performing the required reset operation.

---

## 47. Git Reset --soft

The assignment required rolling back main to the commit where only Item ID had been added.

The soft reset command used was:

git reset --soft e528291

The `--soft` option moves the branch pointer to the specified commit while keeping subsequent changes staged in the Git index.

The status was checked using:

git status

The staged changes could therefore be reviewed before creating the required re-commit.

---

## 48. Re-commit After Soft Reset

After the soft reset, the resulting Item UUID and Item Hash changes were re-committed as required.

Commit message used:

Re-commit Item UUID and Item Hash changes

The purpose of this step was to demonstrate that `git reset --soft` can move the branch to an earlier commit while retaining changes for another commit.

---

## 49. Rebase Operation

The final Git operation was rebasing `master_1` onto the updated main branch.

Required command:

git rebase main master_1

The rebase operation reapplies the branch commits on top of the updated main history.

The Task 4 development commits were maintained as individual commits rather than intentionally squashing the three original development commits into one.

---

# 50. Flask Application Routes

The completed Flask application provides the following routes:

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Displays Flask application status |
| `/api` | GET | Returns JSON data from `data.json` |
| `/todo` | GET | Displays the To-Do frontend |
| `/submittodoitem` | POST | Stores To-Do information in MongoDB |

---

# 51. Main Flask Application

The application includes Flask, JSON handling, HTML rendering, MongoDB connectivity, and environment-variable loading.

Main components include:

- Flask application initialization
- MongoDB connection
- JSON API
- To-Do frontend route
- To-Do POST API
- MongoDB insertion
- Validation of submitted data

---

# 52. JSON API

The `/api` endpoint reads data from:

data.json

The file contains student information in JSON format.

The API loads the file using Python's JSON module and returns the information using Flask's `jsonify()` function.

Example:

@app.route("/api")
def api():
    with open("data.json", "r") as file:
        data = json.load(file)

    return jsonify(data)

---

# 53. To-Do Frontend

The To-Do frontend is located at:

templates/todo.html

The form contains:

- Item ID
- Item UUID
- Item Hash
- Item Name
- Item Description

The Item ID, Item UUID, and Item Hash fields are read-only.

The Item Name and Item Description fields are used for entering To-Do information.

The form submits the information to:

/submittodoitem

using the POST method.

---

# 54. MongoDB POST API

The endpoint:

POST /submittodoitem

reads:

itemName

itemDescription

The data is validated and inserted into the MongoDB collection:

todo_items

The generated MongoDB ID is returned as part of the response.

---

# 55. Requirements

The project dependencies are defined in:

requirements.txt

Contents:

Flask==3.0.2
pymongo==4.18.1
python-dotenv==1.0.1

To install the dependencies:

pip install -r requirements.txt

---

# 56. Security

Sensitive credentials were protected using environment variables.

The `.env` file is ignored by Git.

`.gitignore` contains:

venv/
__pycache__/
*.pyc
.env

A safe `.env.example` file is included:

MONGO_URI=your_mongodb_connection_string_here

The real MongoDB connection string should never be committed to GitHub.

---

# 57. Running the Application

## Step 1 — Clone the repository

git clone git@github.com:Narinder-code17/Git_and_GitHub_Narinder.git

## Step 2 — Enter the project directory

cd Git_and_GitHub_Narinder

## Step 3 — Install dependencies

pip install -r requirements.txt

## Step 4 — Create the `.env` file

Create a local `.env` file and add:

MONGO_URI=your_mongodb_connection_string

## Step 5 — Run Flask

python app.py

The application can then be accessed at:

http://127.0.0.1:5000/

---

# 58. Testing

The following components were tested:

### Flask Home

URL:

http://127.0.0.1:5000/

Expected output:

Flask application is running successfully.

### JSON API

URL:

http://127.0.0.1:5000/api

The endpoint returns the contents of `data.json`.

### To-Do Frontend

URL:

http://127.0.0.1:5000/todo

The To-Do form is displayed.

### MongoDB POST API

Endpoint:

POST http://127.0.0.1:5000/submittodoitem

The endpoint successfully inserted a To-Do item into MongoDB and returned HTTP 201.

---

# 59. Git Commands Practiced

## Check Git status

git status

## View branches

git branch

## Create a branch

git switch -c branch_name

## Switch branches

git switch branch_name

## Add files

git add .

## Commit changes

git commit -m "Commit message"

## Push branch

git push -u origin branch_name

## Pull changes

git pull

## Merge branch

git merge branch_name

## View commit history

git log --oneline --graph --all

## Soft reset

git reset --soft <commit-id>

## Rebase

git rebase main master_1

---

# 60. Important Commit History

Important commits created during the assignment include:

75d8bcf — Add initial Flask project

51d226e — Update API JSON data

9e76303 — Update main API data

cb2436d — Merge Narinder-code17_new and resolve conflict

0088c98 — Create To-Do frontend

d273b20 — Add MongoDB To-Do submission API

d68e32c — Merge master_2 into main

e528291 — Add Item ID to To-Do form

f4ceb6e — Add Item UUID to To-Do form

Add Item Hash to To-Do form — Item Hash commit

---

# 61. Branches Used

The project used the following branches:

### main

The primary integration branch containing the combined project.

### Narinder-code17

The username-based branch used for the initial Flask project.

### Narinder-code17_new

The branch used for the JSON update and merge conflict exercise.

### master_1

The branch used for the To-Do frontend and Task 4 sequential commits.

### master_2

The branch used for the MongoDB backend and POST API.

---

# 62. Screenshot Documentation

The project contains screenshots documenting the Git workflow and application implementation.

The screenshots provide evidence of:

- SSH key creation and configuration
- Successful GitHub SSH authentication
- Repository cloning
- Flask server execution
- Flask home page
- JSON API
- Git configuration
- Username branch creation
- Adding project files
- Initial commit
- Branch push
- Main branch creation
- Branch merging
- JSON modification
- JSON commits
- Merge conflict
- Conflict resolution
- Conflict staging
- Merge commit
- Git history
- master_1 creation
- To-Do frontend
- Git staging
- Commits
- Branch push
- master_2 implementation
- MongoDB integration
- Task 4 Item ID
- Task 4 Item UUID
- Task 4 Item Hash
- Git reset --soft
- Re-commit
- Git rebase
- Final Git history

A total of approximately 40 screenshots were prepared as evidence for the assignment workflow.

# 64. Final Repository

GitHub Repository:

https://github.com/Narinder-code17/Git_and_GitHub_Narinder

The repository contains the Flask application, JSON data, HTML frontend, MongoDB API implementation, Git configuration files, and Git history required for the assignment.

---

# 65. Conclusion

The Git and GitHub assignment was completed using a Flask and MongoDB application.

The project demonstrates the complete software development workflow using Git, including SSH authentication, repository cloning, branching, committing, pushing, merging, conflict resolution, sequential commits, soft reset, and rebasing.

The application functionality was also implemented and tested through the Flask home route, JSON API, To-Do frontend, and MongoDB-backed POST API.

The project is supported by screenshots documenting the major implementation and Git workflow steps.

The final project is organized for submission as:

Git_and_GitHub_Narinder.zip

and the corresponding GitHub repository is:

https://github.com/Narinder-code17/Git_and_GitHub_Narinder

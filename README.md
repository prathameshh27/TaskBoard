# TaskBoard App (APIs Only)

The TaskBoard app is a collaborative project management tool designed to help teams streamline their workflow and track tasks efficiently. It provides API Endpoints for creating and managing tasks within customizable boards. Users can create boards for different projects or teams, add team members, and assign tasks to individuals. The app allows users to create, update, and delete tasks, as well as track their progress through different status options. Additionally, users can retrieve information about boards, tasks, and team members, facilitating effective communication and coordination among team members. With the TaskBoard app, teams can stay organized, prioritize tasks, and collaborate 


## Installation

1. Ensure you have Python 3.x and pip installed on your system.

2. Clone the Taskboard App repository to your local machine:
   ```shell
   git clone https://github.com/your-username/taskboard-app.git
   ```

3. Navigate to the project directory:
   ```shell
   cd taskboard-app
   ```

4. Set up a virtual environment (optional but recommended) to isolate dependencies:
   ```shell
   python -m venv env
   source env/bin/activate   # On macOS/Linux
   env\Scripts\activate      # On Windows
   ```

5. Install the required packages using pip:
    ```shell
    pip install -r requirements.txt
    ```

6. Apply the database migrations:
    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```

7. Create a super user
    ```shell
    python manage.py createsuperuser
    ```


## Usage

To run the development server and access the Taskboard App, execute the following command:
    ```shell
    python manage.py runserver
    ```

Once the server is running, you can access the API endpoints using a tool like cURL or Postman.

### Base URL

The base URL for all API endpoints is: `http://127.0.0.1:8000/api/v1`

## Endpoints

Below are some examples on how to use each endpoint in detail with sample request bodies where applicable.

### User

- **Create User**
  - Endpoint: `POST /user/create`
  - Description: Creates a new user.
  - Constraint:
    - user name must be unique
    - name can be max 64 characters
    - display name can be max 64 characters
  - Fields: 
  - Request Body:
    ```
    {
        "name": "prathameshh27",
        "display_name": "Prathamesh"
    }
    ```

- **Update User**
  - Endpoint: `PATCH /user/update`
  - Description: Updates an existing user.
  - Constraint:
    - name cannot be updated
    - display name can be max 128 characters
    - Fields:
  - Request Body:
    ```
    {
        "id": "751350f2",
        "name": "prathameshh27",
        "display_name": "Prathamesh Pavnoji"
    }
    ```

- **Describe User**
  - Endpoint: `GET /user/describe`
  - Description: Retrieves information about a specific user by passing a user_id.
  - Request Body:
    ```
    {
        "id": "bc789701"
    }
    ```

- **List Users**
  - Endpoint: `GET /user/list`
  - Description: Retrieves a list of all users.


- **List User Teams**
  - Endpoint: `GET /user/list_teams`
  - Description: Retrieves a list of teams that a user belongs to. Pass a user_id.
  - Request Body:
    ```
    {
        "id": "bc789701"
    }
    ```


### Team

- **Create Team**
  - Endpoint: `POST /team/create`
  - Description: Creates a new team.
  - Constraint:
    - Team name must be unique
    - Name can be max 64 characters
    - Description can be max 128 characters
  - Request Body:
    ```
    {
        "name": "Web Development",
        "description": "This team handles the frontend",
        "admin": "4db041b3"
    }
    ```

- **Update Team**
  - Endpoint: `PATCH /team/update`
  - Description: Updates an existing team.
  - Constraint:
    - Team name cannot be edited
    - Name can be max 64 characters
    - Description can be max 128 characters
  - Request Body:
    ```
    {
        "id": "c12251f8",
        "team": {
            "name": "Web Development",
            "description": "This team is responsible for handling the frontend components of any web applications",
            "admin": "4db041b3"
        }
    }
    ```

- **Describe Team**
  - Endpoint: `GET /team/describe`
  - Description: Retrieves information about a specific team.
  - Request Body:
    ```
    {
        "id": "39e23a1f"
    }
    ```

- **List Teams**
  - Endpoint: `GET /team/list`
  - Description: Retrieves a list of all teams.


- **List Users in Team**
  - Endpoint: `GET /team/list_users`
  - Description: Retrieves a list of users in a team by passing a team id.
  - Request Body:
    ```
    {
        "id": "39e23a1f"
    }
    ```

- **Add Users to Team**
  - Endpoint: `GET /team/add_users`
  - Description: Adds users to a team.
  - Constraint:
    - At most 50 users can be added to a team. (Limit can be changed from the Model)
  - Request Body:
    ```
    {
        "id": "39e23a1f",
        "users": ["24996731", "751350f2"]
    }
    ```

- **Remove Users from Team**
  - Endpoint: `GET /team/remove_users`
  - Description: Removes users from a team.
  - Request Body:
    ```
    {
        "id": "39e23a1f",
        "users": ["24996731", "751350f2"]
    }
    ```


### Board

- **Create Board**
  - Endpoint: `POST /board/create`
  - Description: Creates a new board.
  - Constraint:
    - Board name must be unique for a team
    - Board name can be max 64 characters
    - Description can be max 128 characters
  - Fields:
  - Request Body:
    ```
    {
        "name": "Kanban Board",
        "team_id": "39e23a1f",
        "description": "This baord tracks the daily tasks for the Web Development team"
    }
    ```

- **List Boards**
  - Endpoint: `GET /board/list`
  - Description: Retrieves a list of all boards for a perticular team.
  - Request Body:
    ```
    {
        "id" : "39e23a1f"
    }
    ```

- **Close Board**
  - Endpoint: `GET /board/close`
  - Description: Close the board if the tasks are completed.
  - Constraint:
    - You can only close boards with all tasks marked as COMPLETE
  - Request Body:
    ```
    {
        "id" : "39e23a1f"
    }
    ```

- **Export Board**
  - Endpoint: `GET /board/export`
  - Description: Export a board in the out folder. The output will be a CSV file.
  - Request Body:
    ```
    {
        "id" : "39e23a1f"
    }
    ```
  - Response Body:
    ```
    {
        "out_file" : "<name of the file created>"
    }
    ```

- **Create Task**
  - Endpoint: `POST /board/add_task`
  - Description: Creates a new task in a board.
  - Constraint:
    - Task title must be unique for a board
    - Title name can be max 64 characters
    - Description can be max 128 characters
    - Can only add task to an OPEN board
  - Request Body:
    ```
    {
        "board_id": "8a5e6109",
        "title": "Task 1",
        "description": "Complete the homepage design",
        "user_id": "24996731"
    }
    ```

- **Update Task status**
  - Endpoint: `PATCH /board/update_task_status`
  - Description: Update the task status for the given task.
  - Constraint:
    - Status allowed (small case works): "OPEN | IN_PROGRESS | COMPLETE"
  - Request Body:
    ```
    {
        "id": "8a5e6109",
        "status" : "in_progress"
    }
    ```
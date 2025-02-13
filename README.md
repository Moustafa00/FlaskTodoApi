# Todo API

A simple RESTful API for managing todos, built with Flask and deployed on Render.

## Live API
Access the live API at: [https://todo-api-z65c.onrender.com](https://todo-api-z65c.onrender.com)

## Endpoints
- **GET /todos**: Retrieve all todos.
- **POST /todos**: Add a new todo. Send a JSON body: `{"task": "Your task here"}`.
- **DELETE /todos/<todo_id>**: Delete a todo by ID.

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Test the API at `http://127.0.0.1:5000/`.

## Deployment
Deployed on [Render](https://render.com/). To deploy your own version:
1. Fork this repository.
2. Create a new web service on Render and connect your GitHub repository.
3. Render will automatically deploy the app.

## Technologies Used
- **Flask**: Web framework.
- **Render**: Cloud platform.
- **Python**: Programming language.

## Author
[Moustafa Jarjour](https://moustafa00.github.io/)

import { useEffect, useState } from "react";
import { fetchTodos, addTodo } from "./api";
import "./App.css";

function App() {
  const [todos, setTodos] = useState([]);
  const [task, setTask] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  useEffect(() => {
    loadTodos();
  }, []);

  const loadTodos = () => {
    setLoading(true);
    fetchTodos()
      .then((data) => {
        setTodos(data);
        setLoading(false);
      })
      .catch(() => {
        setError("Failed to load todos");
        setLoading(false);
      });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (task.trim() === "") {
      setError("Task cannot be empty");
      return;
    }

    setError("");
    setSubmitting(true);

    addTodo(task)
      .then(() => {
        loadTodos();
        setTask("");
      })
      .catch(() => setError("Failed to add todo"))
      .finally(() => setSubmitting(false));
  };

  return (
    <div className="App">
      <div>
        <h1>List of TODOs</h1>
        {loading ? (
          <p>Loading...</p>
        ) : todos.length === 0 ? (
          <p>No todos found.</p>
        ) : (
          todos.map((t, i) => <li key={i}>{t.task}</li>)
        )}
      </div>
      <div>
        <h1>Create a ToDo</h1>
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor="todo">ToDo: </label>
            <input
              type="text"
              value={task}
              onChange={(e) => setTask(e.target.value)}
              style={{
                border: error ? "1px solid red" : "1px solid #ccc",
              }}
            />
          </div>
          {error && (
            <p style={{ color: "red", fontSize: "14px", marginTop: "5px" }}>
              {error}
            </p>
          )}
          <div style={{ marginTop: "5px" }}>
            <button type="submit" disabled={submitting}>
              {submitting ? "Adding..." : "Add ToDo!"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default App;
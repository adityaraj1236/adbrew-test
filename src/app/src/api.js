export const API_URL = "http://localhost:8000";

export async function fetchTodos() {
  const res = await fetch(`${API_URL}/todos/`);
  if (!res.ok) throw new Error("Failed to fetch todos");
  return res.json();
}

export async function addTodo(task) {
  const res = await fetch(`${API_URL}/todos/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ task }),
  });

  if (!res.ok) throw new Error("Failed to add todo");
  return res.json();
}
const url = "http://localhost:8787";
export const getUsers = () => fetch(`${url}/users`);
export const getDogs = () => fetch(`${url}/dogs`);
export const getPoops = () => fetch(`${url}/poops`);
export const createPoop = (params: { color: string; shape: string }) =>
  fetch(`${url}/poops`, {
    body: JSON.stringify(params),
    method: "POST",
  });

import { useEffect, useState } from "react"

function App() {
  let get_local = JSON.parse(localStorage.getItem("data"));

  useEffect(() => {
    get_local === null
      ? localStorage.setItem("data", JSON.stringify([]))
      : null;
  }, []);
};
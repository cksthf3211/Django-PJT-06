import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

useEffect(() => {
  if (get_local == null) {
    get_local = [];
  } else {
    get_local = JSON.parse(get_local);
  }

  get_local.push(props.article[pk].name);
  get_local = new Set(get_local);
  get_local = [...get_local];
  localStorage.setItem("data", JSON.stringify(get_local));
}, []);
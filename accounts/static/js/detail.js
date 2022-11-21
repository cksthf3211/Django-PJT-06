import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

const Detail = (props) => {
  let { id } = useParams();

  useEffect(() => {
    let get_local = localStorage.getItem("viewed");

    if (get_local == null) {
      get_local = [];
    } else {
      get_local = JSON.parse(get_local);
    }
    get_local.push(props.article[id].name);
    get_local = new Set(get_local);
    get_local = [...get_local];
    localStorage.setItem("viewed", JSON.stringify(get_local));
  }, []);
};
export default Detail;
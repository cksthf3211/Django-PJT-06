import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
const DetailPage = (props) => {
  let { id } = useParams();

  useEffect(() => {
    let get_local = localStorage.getItem('data');

    if (get_local == null) {
      get_local = [];
    } else {
      get_local = JSON.parse(get_local);
    }

    get_local.push();
    get_local = new Set(get_local);
    get_local = [...get_local];
    localStorage.setItem("data", JSON.stringify())

  }, []);
}
export default DetailPage;
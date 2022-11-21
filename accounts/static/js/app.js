import { useEffect, useState } from "react"
import Detail from "./detail"

class App extends Component {
  render() {
    <div className="App">
      <Detail />
      {get_local !== null
        ? get_local.map((a, i) => {
          return (
            <div className="card mx-1" style="width: 10rem;">
              <img src="{{ article.image.url }}" width="100%" />
              <div className="card-body">
                <p>{get_local[i]}</p>
              </div>
            </div>
          );
        })
        : null}
    </div>
  }
}

function App() {
  let get_local = JSON.parse(localStorage.getItem("viewed"));

  useEffect(() => {
    get_local === null
      ? localStorage.setItem("data", JSON.stringify([]))
      : null;
  }, []);
};

export default App;
import React, { Component } from "react";
import { render } from "react-dom";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import LoginPage from "./Components/LoginPage";
import RegisterPage from "./Components/RegisterPage";
import "bootstrap/dist/css/bootstrap.min.css";

class App extends Component {
  render() {
    return (
      <div>
        <Router>
          <Switch>
            <Route exact path="/" component={LoginPage}></Route>
            <Route path="/register" component={RegisterPage}></Route>
          </Switch>
        </Router>
      </div>
    );
  }
}

export default App;

const container = document.getElementById("root");
render(<App />, container);

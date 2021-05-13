import React from "react";
import ReactDOM from "react-dom";
import './index.css'
import { HashRouter, Route, Switch } from "react-router-dom";
import Header from "./components/templates/Header";
import EmployeesIndex from "./components/pages/employees/search/index";
import EmployeesInfo from "./components/pages/employees/info/index";
import TrainingsIndex from "./components/pages/trainings/search/index";
import TrainingsInfo from "./components/pages/trainings/info/index";
import TrainingsRegister from "./components/pages/trainings/register/index";
import MainMenu from "./components/pages/menu/index";

const App = () => {
  return (
    <>
      <Header />
        <HashRouter>
          <Switch>
            <Route exact path="/" component={MainMenu} />
            <Route exact path="/employees" component={EmployeesIndex} />
            <Route exact path="/employees/:employeeId" component={EmployeesInfo} />
            <Route exact path="/trainings" component={TrainingsIndex} />
            <Route exact path="/register" component={TrainingsRegister} />
            <Route exact path="/trainings/:trainingId" component={TrainingsInfo} />
            <Route exact path="/trainings/:trainingId" component={TrainingsInfo} />
          </Switch>
        </HashRouter>
    </>
  );
};

ReactDOM.render(<App />, document.getElementById("root"));

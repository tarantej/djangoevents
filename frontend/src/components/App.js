import React, {Component, Fragment} from 'react';
import ReactDOM from 'react-dom';
import HD from "./layout/HD";
import Dashboard from "./events/dashboard";

class App extends Component{
    render() {
        // return <h1>React App</h1>
        return(
            <Fragment>
               <HD />
               <div className="container">
                   <Dashboard />
               </div>

            </Fragment>


        )
    }
}
ReactDOM.render(<App />, document.getElementById('app'));
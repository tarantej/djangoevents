import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import {Drawer, Button, List, ListItem, ListItemIcon, ListItemText, Divider} from '@material-ui/core';
import {BrowserRouter as Router, Route, Switch, Link} from 'react-router-dom';
import HomeIcon from '@material-ui/icons/Home';
import './App.css';
const useStyles = makeStyles({
  list: {
      display:'flex',
    width: 250,
  },
link:{
textDecoration:'none',

},
  fullList: {
    width: 'auto',
  },
});
function App() {
    const classes = useStyles();
  return (
      <Router>
          <div style={{display:'flex'}}>
              <Drawer style={{classes:classes.list}}
                      anchor = "left"
                      open={true}>
                  <List>
			<Link to="/" className={classes.link}>
                      <ListItem button>
                          <ListItemIcon>
                              <HomeIcon />
                          </ListItemIcon>
                          <ListItemText primary={"Home"} />
                      </ListItem>
			</Link>
			<Link to="/about" className={classes.link}>
                      <ListItem button>
                          <ListItemIcon>
                              <HomeIcon />
                          </ListItemIcon>
                          <ListItemText primary={"About"} />
                      </ListItem>
			</Link>
			<Link to="/contact" className={classes.link}>
                      <ListItem button>
                          <ListItemIcon>
                              <HomeIcon />
                          </ListItemIcon>
                          <ListItemText primary={"Contact"} />
                      </ListItem>
			</Link>
                  </List>

              </Drawer>

          </div>
      </Router>
    // <div className="App">
    //   <header className="App-header">
    //     <img src={logo} className="App-logo" alt="logo" />
    //     <p>
    //       Edit <code>src/App.js</code> and save to reload.
    //     </p>
    //     <a
    //       className="App-link"
    //       href="https://reactjs.org"
    //       target="_blank"
    //       rel="noopener noreferrer"
    //     >
    //       Learn React
    //     </a>
    //   </header>
    // </div>
  );
}

export default App;

import React, {Component} from 'react';
import StatsContainer from './StatsContainer';

import {Switch, Route} from "react-router-dom";
import MapContainer from "./MapContainer";

import datamap from './datamap.png'
import AddScript from "./AddScript";


class Main extends Component {


    render() {
        return (
            <Switch>
                <Route path='/stats' component={StatsContainer}/>
                <Route path='/map' component={MapContainer}/>
                <Route path='/datamap' render={() => <img style={{width:"100%"}} src={datamap} alt="Datamap" />}/>
                <Route path='/addscript' component={AddScript}/>
            </Switch>
        );
    }
}

export default Main;
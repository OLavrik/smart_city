import React, {Component} from 'react';
import StatsContainer from './StatsContainer';

import {Switch, Route} from "react-router-dom";



class Main extends Component {


    render() {
        return (
            <Switch>
                <Route path='/stats' component={StatsContainer}/>
            </Switch>
        );
    }
}

export default Main;
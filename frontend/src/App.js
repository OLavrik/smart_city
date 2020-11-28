import React, {Component} from 'react';
import './App.css';

import {BrowserRouter} from 'react-router-dom';
import Main from './components/Main.js'
import Header from './components/Header.js'
import {MDBContainer} from "mdbreact";
import Cookies from 'js-cookie';
import {ToastContainer, toast} from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

class App extends Component {

    constructor(props) {
        super(props);
    }


    render() {
        return (
            <BrowserRouter>
                <div>
                    <Header/>
                    <MDBContainer className="mt-5 pt-5">
                        <Main/>
                        <ToastContainer hideProgressBar={true}/>
                    </MDBContainer>
                </div>
            </BrowserRouter>
        );
    }
}

export default App;

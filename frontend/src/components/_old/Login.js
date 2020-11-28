import React, {Component} from 'react';
import {MDBBtn} from "mdbreact";
import {Link, withRouter} from 'react-router-dom';
import {login} from "../Api";
import {toast} from 'react-toastify';


class Login extends Component {
    constructor(props) {
        super(props);
        this.state = {
            login: '',
            password: '',
        };
    }

    handleChange = event => {
        this.setState({
            [event.target.id]: event.target.value
        });
    };

    handleSubmit = async (event) => {
        event.preventDefault();
        const resp = await login({
            login: this.state.login,
            password: this.state.password
        });
        if (resp && resp.token) {
            this.props.setUserInfo(resp);
            toast.success(`Token expires ${resp.token_expire}`);
            this.props.history.push({
                pathname: '/profile/' + resp.user_id,
            });
        }
    };

    render() {
        return (
            <div>
                <form onSubmit={this.handleSubmit}>
                    <label htmlFor="login" className="grey-text font-weight-light">
                        Login
                    </label>
                    <input type="text" placeholder="Enter account name"
                           id="login" className="form-control"
                           value={this.state.login}
                           onChange={this.handleChange}/>
                    <br/>
                    <label htmlFor="password" className="grey-text font-weight-light">
                        Login
                    </label>
                    <input type="password" placeholder="Password"
                           id="password" className="form-control"
                           value={this.state.password}
                           onChange={this.handleChange}/>
                    <div className="text-center py-4 mt-3">
                        <MDBBtn outline color="success" type="submit">
                            Log in!
                        </MDBBtn>
                        <br/><br/>
                        <h4>Do not have an account yet?</h4>
                        <Link to="/register">Click here to register</Link>
                    </div>
                </form>
            </div>
        );
    }
}

export default withRouter(Login);
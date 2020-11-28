import React, {Component} from 'react';
import {MDBBtn} from "mdbreact";
import {Link, withRouter} from 'react-router-dom';
import {register} from "../Api";
import {toast} from 'react-toastify';


class Register extends Component {
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
        const resp = await register({
            login: this.state.login,
            password: this.state.password
        });
        if (resp) {
            toast.success(`You are in!`);
            this.props.history.push({
                pathname: '/login/',
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
                        Password
                    </label>
                    <input type="password" placeholder="Password"
                           id="password" className="form-control"
                           value={this.state.password}
                           onChange={this.handleChange}/>
                    <div className="text-center py-4 mt-3">
                        <MDBBtn outline color="success" type="submit">
                            Register!
                        </MDBBtn>
                        <br/><br/>
                        <h4>Already have an account?</h4>
                        <Link to="/login">Click here to log in</Link>
                    </div>
                </form>
            </div>
        );
    }
}

export default withRouter(Register);
import React, {Component} from 'react';
import '../App.css';
import {withRouter} from 'react-router-dom';
import {MDBInputGroup, MDBBtn} from 'mdbreact'
class SearchBar extends Component {
    state = {
        searchStr: ""
    };

    handleChange = (event) => {
        this.setState({
            [event.target.id]: event.target.value
        });
        this.props.onSearchChange(event.target.value, false);
    };

    handleSubmit = (event) => {
        event.preventDefault();
        this.props.onSearchChange(this.state.searchStr, true);
    };

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <MDBInputGroup
                    append={<MDBBtn type="submit" size="sm" className="m-0 px-3 py-2 z-depth-0">Search</MDBBtn>}
                    inputs={
                        <input size="lg" type="text" id="searchStr" className="form-control" placeholder="Search"
                               value={this.state.searchStr}
                               onChange={this.handleChange}/>
                    }
                />
            </form>
        );
    }
}

export default withRouter(SearchBar);
import React, {Component} from "react";
import {
    MDBContainer,
    MDBIcon,
    MDBBtn,
} from 'mdbreact';
import './StorageDetailed.css'
import {addNewStorage} from "../Api";
import {toast} from "react-toastify";


class AddStoreForm extends Component {
    state = {
        name: "",
        location: "",
        description: "",
        owner_id: 2,
    };

    onSubmit = async (event) => {

        const body = {
            name: this.state.name,
            location: this.state.location,
            description: this.state.description,
            owner_id: this.state.owner_id
        };
        event.preventDefault();

        const resp = await addNewStorage(body);
        if (resp) {
            toast.success(`Storage created`);
            this.props.history.push({
                pathname: '/storages/' + resp.id,
            });
        }
    };

    onChangeName = (event) => {
        this.setState({name: event.target.value});
    };

    onChangeLocation = (event) => {
        this.setState({location: event.target.value});
    };

    onChangeDescription = (event) => {
        this.setState({description: event.target.value});
    };

    onChangeOwnerId = (event) => {
        this.setState({owner_id: event.target.value});
    };

    render() {

        return (
            <MDBContainer className="w-75">
                <form onSubmit={this.onSubmit}>
                    <p className="h4 text-center py-4">Provide new storage info</p>
                    <label htmlFor="defaultFormCardNameEx" className="grey-text font-weight-light">
                        Name
                    </label>
                    <input type="text" name="name" id="defaultFormCardNameEx" className="form-control"
                           value={this.state.name}
                           onChange={this.onChangeName}/>
                    <br/>

                    <label htmlFor="defaultFormContactMessageEx" className="grey-text">
                        Location
                    </label>
                    <textarea type="text" id="defaultFormContactMessageEx" className="form-control" rows="3"
                              value={this.state.location}
                              onChange={this.onChangeLocation}/>

                    <label htmlFor="defaultFormContactMessageEx" className="grey-text">
                        Description
                    </label>
                    <textarea type="text" id="defaultFormContactMessageEx" className="form-control" rows="3"
                              value={this.state.description}
                              onChange={this.onChangeDescription}/>

                    <label htmlFor="defaultFormContactMessageEx" className="grey-text">
                        Owner
                    </label>
                    <input type="number" id="defaultFormContactMessageEx" className="form-control"
                              value={this.state.owner_id}
                              onChange={this.onChangeOwnerId}/>

                    <div className="text-center py-4 mt-3">
                        <MDBBtn className="btn btn-outline-purple" type="submit">
                            Add!
                            <MDBIcon far icon="paper-plane" className="ml-2"/>
                        </MDBBtn>
                    </div>
                </form>
            </MDBContainer>
        )
    }
}

export default AddStoreForm;